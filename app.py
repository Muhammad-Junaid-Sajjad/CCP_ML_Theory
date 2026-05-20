# =============================================================================
# CELL 1 — PROJECT TITLE & DESCRIPTION
# =============================================================================
# Project  : Chronic Kidney Disease (CKD) Prediction System
# File     : app.py  –  Flask REST API Backend
# Dataset  : UCI CKD Dataset (399 patients, 24 features)
# Purpose  : This file serves as the backend API that:
#              • Loads trained ML models and preprocessing objects
#              • Accepts patient data from the web interface
#              • Preprocesses the input (encode → impute → scale)
#              • Runs prediction through the best ensemble model
#              • Returns prediction + probability + risk level as JSON
# Run with : python app.py
# API Base : http://localhost:5000
# =============================================================================


# =============================================================================
# CELL 2 — IMPORT LIBRARIES
# =============================================================================
# Standard & third-party libraries required for the Flask API

from flask import Flask, request, jsonify, send_from_directory   # Web framework
from flask_cors import CORS                                       # Allow cross-origin requests from browser
import numpy as np                                                # Numerical operations
import pandas as pd                                               # DataFrame handling for input processing
import joblib                                                     # Load saved .pkl model files
import json                                                       # Read results_summary.json
import os                                                         # File path checks
import traceback                                                  # Detailed error logging

print("[✓] All libraries imported successfully.")


# =============================================================================
# CELL 3 — FLASK APP INITIALIZATION
# =============================================================================
# Create the Flask application instance.
# static_folder  → serves plots from static/plots/
# template_folder → serves index.html from the root directory

app = Flask(__name__, static_folder="static", template_folder=".")
CORS(app)   # Enable CORS so the HTML front-end can call the API from any origin

print("[✓] Flask app initialized with CORS enabled.")


# =============================================================================
# CELL 4 — FEATURE CONFIGURATION
# =============================================================================
# Define which features are numeric vs categorical.
# This mirrors the column structure of the UCI CKD dataset.
# Used during preprocessing of incoming patient data from the web form.

# All 24 feature names in dataset order
ALL_FEATURES = [
    'age', 'bp', 'sg', 'al', 'su',           # Basic measurements
    'rbc', 'pc', 'pcc', 'ba',                # Urine analysis (categorical)
    'bgr', 'bu', 'sc', 'sod', 'pot',         # Blood chemistry
    'hemo', 'pcv', 'wbcc', 'rbcc',           # Blood count
    'htn', 'dm', 'cad', 'appet', 'pe', 'ane' # Clinical observations (categorical)
]

# Categorical (non-numeric) feature names
CATEGORICAL_COLS = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']

# Human-readable labels for the web form
FEATURE_LABELS = {
    "age"  : "Age (years)",
    "bp"   : "Blood Pressure (mm/Hg)",
    "sg"   : "Specific Gravity",
    "al"   : "Albumin (0-5)",
    "su"   : "Sugar (0-5)",
    "rbc"  : "Red Blood Cells",
    "pc"   : "Pus Cell",
    "pcc"  : "Pus Cell Clumps",
    "ba"   : "Bacteria",
    "bgr"  : "Blood Glucose Random (mgs/dl)",
    "bu"   : "Blood Urea (mgs/dl)",
    "sc"   : "Serum Creatinine (mgs/dl)",
    "sod"  : "Sodium (mEq/L)",
    "pot"  : "Potassium (mEq/L)",
    "hemo" : "Hemoglobin (gms)",
    "pcv"  : "Packed Cell Volume",
    "wbcc" : "WBC Count (cells/cumm)",
    "rbcc" : "RBC Count (millions/cmm)",
    "htn"  : "Hypertension",
    "dm"   : "Diabetes Mellitus",
    "cad"  : "Coronary Artery Disease",
    "appet": "Appetite",
    "pe"   : "Pedal Edema",
    "ane"  : "Anemia",
}

# Valid options for each categorical field (used by /feature_info endpoint)
CATEGORICAL_OPTIONS = {
    "rbc"  : ["normal", "abnormal"],
    "pc"   : ["normal", "abnormal"],
    "pcc"  : ["present", "notpresent"],
    "ba"   : ["present", "notpresent"],
    "htn"  : ["yes", "no"],
    "dm"   : ["yes", "no"],
    "cad"  : ["yes", "no"],
    "appet": ["good", "poor"],
    "pe"   : ["yes", "no"],
    "ane"  : ["yes", "no"],
}

print("[✓] Feature configuration defined.")
print(f"    Total features    : {len(ALL_FEATURES)}")
print(f"    Numeric features  : {len(ALL_FEATURES) - len(CATEGORICAL_COLS)}")
print(f"    Categorical feat. : {len(CATEGORICAL_COLS)}")


# =============================================================================
# CELL 5 — LOAD TRAINED MODEL & PREPROCESSING OBJECTS
# =============================================================================
# Load all artifacts saved during ckd_pipeline.py training:
#
#   best_model.pkl       → best ensemble classifier (RandomForest by default)
#   imputer.pkl          → SimpleImputer (median strategy) for missing values
#   scaler.pkl           → StandardScaler for feature normalization
#   label_encoders.pkl   → LabelEncoders for all 10 categorical columns
#   feature_names.pkl    → ordered feature name list (ensures correct column order)
#   results_summary.json → metrics for all 4 models (used by /results route)
#
# NOTE: If files are missing, the server still starts but /predict returns 503.
#       Fix → run  python ckd_pipeline.py  first to generate models/

try:
    MODEL           = joblib.load("models/best_model.pkl")
    IMPUTER         = joblib.load("models/imputer.pkl")
    SCALER          = joblib.load("models/scaler.pkl")
    LABEL_ENCODERS  = joblib.load("models/label_encoders.pkl")
    FEATURE_NAMES   = joblib.load("models/feature_names.pkl")

    with open("models/results_summary.json") as f:
        RESULTS_SUMMARY = json.load(f)

    print("[✓] Model & preprocessing objects loaded successfully.")
    print(f"    Model type        : {MODEL.__class__.__name__}")
    print(f"    Features expected : {len(FEATURE_NAMES)}")
    print(f"    Models in summary : {list(RESULTS_SUMMARY.keys())}")

except FileNotFoundError as e:
    print(f"[!] WARNING: Could not load model files → {e}")
    print("    Run  python ckd_pipeline.py  first to train and save models.")
    MODEL           = None
    IMPUTER         = None
    SCALER          = None
    LABEL_ENCODERS  = None
    FEATURE_NAMES   = ALL_FEATURES
    RESULTS_SUMMARY = {}


# =============================================================================
# CELL 6 — DATA PREPROCESSING FUNCTION FOR LIVE INPUT
# =============================================================================
# Transforms raw patient data received from the web form into the exact
# format the trained model expects. Must mirror ckd_pipeline.py steps.
#
# Preprocessing pipeline (applied in this exact order):
#   Step 1 → Parse numeric fields   : cast to float, empty/invalid → NaN
#   Step 2 → Encode categoricals    : use saved LabelEncoders, unknown → NaN
#   Step 3 → Build ordered DataFrame: correct column order is critical
#   Step 4 → Impute missing values  : median strategy (same as training)
#   Step 5 → Normalize features     : StandardScaler (same as training)
#
# Returns: numpy array shape (1, 24) — ready for model.predict()

def preprocess_input(data: dict) -> np.ndarray:
    """
    Preprocess a single patient's raw input for model inference.

    Parameters
    ----------
    data : dict
        Raw key-value pairs submitted from the web form.

    Returns
    -------
    np.ndarray
        Scaled feature array of shape (1, n_features).
    """

    row = {}
    numeric_cols = [c for c in FEATURE_NAMES if c not in CATEGORICAL_COLS]

    # ── Step 1: Parse all numeric fields ────────────────────────────────────
    for col in numeric_cols:
        val = data.get(col, "")
        try:
            row[col] = float(val) if val not in ("", None, "nan") else np.nan
        except (ValueError, TypeError):
            row[col] = np.nan       # Unparseable input treated as missing

    # ── Step 2: Label-encode all categorical fields ──────────────────────────
    for col in CATEGORICAL_COLS:
        val = str(data.get(col, "")).strip().lower()
        le  = LABEL_ENCODERS.get(col) if LABEL_ENCODERS else None
        if le is not None and val in le.classes_:
            row[col] = float(le.transform([val])[0])
        else:
            row[col] = np.nan       # Unknown/missing category → NaN

    # ── Step 3: Assemble DataFrame with correct column order ─────────────────
    df = pd.DataFrame([row], columns=FEATURE_NAMES)

    # ── Step 4: Impute missing values using saved median imputer ─────────────
    X_imputed = IMPUTER.transform(df)

    # ── Step 5: Normalize using saved StandardScaler ─────────────────────────
    X_scaled = SCALER.transform(X_imputed)

    return X_scaled

print("[✓] preprocess_input() function defined.")


# =============================================================================
# CELL 7 — API ROUTE: Serve Web Interface  (GET /)
# =============================================================================
# Serves the main HTML file (index.html) when the user opens the browser.
# index.html contains:
#   • Tab 1 → Patient input form (24 fields) + prediction result display
#   • Tab 2 → Model Results (metrics table fetched from /results)
#   • Tab 3 → Analytics (EDA & evaluation plots fetched from /static/plots/)

@app.route("/")
def index():
    """Serve the main web interface (index.html)."""
    return send_from_directory(".", "index.html")


# =============================================================================
# CELL 8 — API ROUTE: Serve Static Plot Images  (GET /static/plots/<filename>)
# =============================================================================
# Serves EDA and model evaluation plots generated by ckd_pipeline.py.
# The Analytics tab fetches these images using <img src="/static/plots/...">
#
# Available plots:
#   class_dist.png            → CKD vs Not-CKD bar chart
#   missing_heatmap.png       → Heatmap of missing values across features
#   numeric_distributions.png → Histograms of numeric features split by class
#   correlation_heatmap.png   → Pearson correlation matrix of numeric features
#   model_comparison.png      → Accuracy/Precision/Recall/F1 bar chart (4 models)
#   confusion_matrices.png    → 2×2 confusion matrix for each model
#   cv_accuracy.png           → 5-fold cross-validation accuracy comparison
#   feature_importance.png    → Top 15 features by Random Forest importance

@app.route("/static/plots/<path:filename>")
def serve_plot(filename):
    """Serve a saved plot image from the static/plots/ directory."""
    return send_from_directory("static/plots", filename)


# =============================================================================
# CELL 9 — API ROUTE: CKD Prediction  (POST /predict)
# =============================================================================
# Core prediction endpoint — called when user submits the patient form.
#
# Request  : POST JSON body with 24 patient feature key-value pairs
# Response : JSON object containing:
#
#   Field            Type     Description
#   ─────────────────────────────────────────────────────────────────
#   prediction       string   "CKD" or "Not CKD"
#   prediction_code  int      1 = CKD, 0 = Not CKD
#   confidence       float    max(prob_ckd, prob_notckd) as %
#   risk_level       string   "High" / "Medium" / "Low"
#   prob_ckd         float    Probability of CKD (%)
#   prob_notckd      float    Probability of Not CKD (%)
#
# Risk Level thresholds:
#   High   → prob_ckd ≥ 70%
#   Medium → prob_ckd 40–69%
#   Low    → prob_ckd < 40%

@app.route("/predict", methods=["POST"])
def predict():
    """Accept patient clinical data and return CKD prediction with probabilities."""

    # Guard: refuse if model was not loaded at startup
    if MODEL is None:
        return jsonify({
            "error": "Model not loaded. Please run  python ckd_pipeline.py  first."
        }), 503

    try:
        # ── Step 1: Read JSON body from the HTTP request ─────────────────────
        data = request.get_json(force=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Invalid input data."}), 400

        if all(str(data.get(col, "")).strip().lower() in ("", "nan") for col in FEATURE_NAMES):
            return jsonify({"error": "No patient data provided. Please fill at least one field."}), 400

        # ── Step 2: Preprocess input (encode + impute + scale) ───────────────
        X_scaled = preprocess_input(data)

        # ── Step 3: Run the ensemble model to get class + probabilities ───────
        prediction = int(MODEL.predict(X_scaled)[0])
        proba      = MODEL.predict_proba(X_scaled)[0].tolist()
        # Index 0 → P(Not CKD),  Index 1 → P(CKD)

        # ── Step 4: Build the response payload ───────────────────────────────
        label      = "CKD" if prediction == 1 else "Not CKD"
        confidence = round(max(proba) * 100, 1)
        risk_level = (
            "High"   if proba[1] >= 0.70 else
            "Medium" if proba[1] >= 0.40 else
            "Low"
        )

        return jsonify({
            "prediction"     : label,
            "prediction_code": prediction,
            "confidence"     : confidence,
            "risk_level"     : risk_level,
            "prob_ckd"       : round(proba[1] * 100, 1),
            "prob_notckd"    : round(proba[0] * 100, 1),
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# =============================================================================
# CELL 10 — API ROUTE: Model Comparison Results  (GET /results)
# =============================================================================
# Returns the saved performance metrics of all 4 trained ensemble models.
# The "Model Results" tab in the web interface calls this on tab-open.
#
# Response: JSON object where each key is a model name and the value
#           contains: accuracy, precision, recall, f1, auc, cv_acc, cm
#
# Example response structure:
# {
#   "Random Forest":       { "accuracy": 1.0, "f1": 1.0, ... },
#   "Gradient Boosting":   { "accuracy": 0.99, ... },
#   "AdaBoost":            { ... },
#   "Voting Classifier":   { ... }
# }

@app.route("/results", methods=["GET"])
def results():
    """Return evaluation metrics for all 4 ensemble classifiers."""
    if not RESULTS_SUMMARY:
        return jsonify({"error": "Results not available. Run ckd_pipeline.py first."}), 503
    return jsonify(RESULTS_SUMMARY)


# =============================================================================
# CELL 11 — API ROUTE: Feature Metadata  (GET /feature_info)
# =============================================================================
# Returns metadata about all 24 features to the web interface.
# Used to dynamically build the patient input form without hardcoding
# field names and options in index.html.
#
# Response fields:
#   features            → ordered list of all 24 feature keys
#   labels              → dict mapping key → human-readable label
#   categorical         → list of categorical feature keys
#   categorical_options → dict of valid dropdown values per categorical feature

@app.route("/feature_info", methods=["GET"])
def feature_info():
    """Return feature names, labels, and categorical dropdown options."""
    return jsonify({
        "features"            : FEATURE_NAMES,
        "labels"              : FEATURE_LABELS,
        "categorical"         : CATEGORICAL_COLS,
        "categorical_options" : CATEGORICAL_OPTIONS,
    })


# =============================================================================
# CELL 12 — START THE FLASK DEVELOPMENT SERVER
# =============================================================================
# Runs the Flask app when this file is executed directly with:
#   python app.py
#
# Server configuration:
#   host  = "0.0.0.0"  → listens on all network interfaces (LAN accessible)
#   port  = 5000       → default Flask development port
#   debug = True       → auto-reloads on code save, shows full error tracebacks
#
# Available endpoints after startup:
#   http://localhost:5000/              → Web interface
#   http://localhost:5000/predict       → POST prediction API
#   http://localhost:5000/results       → GET model metrics
#   http://localhost:5000/feature_info  → GET feature metadata
#   http://localhost:5000/static/plots/ → GET EDA/evaluation plots

if __name__ == "__main__":
    print()
    print("=" * 58)
    print("   CKD Prediction System — Flask API Server")
    print("=" * 58)
    print("   Web Interface  →  http://localhost:5000/")
    print("   Predict API    →  POST /predict")
    print("   Model Results  →  GET  /results")
    print("   Feature Info   →  GET  /feature_info")
    print("   Plots          →  GET  /static/plots/<filename>")
    print("=" * 58)
    print()
    app.run(debug=True, host="0.0.0.0", port=5000)
