"""
================================================================================
CHRONIC KIDNEY DISEASE (CKD) PREDICTION SYSTEM - FLASK REST API
================================================================================
Project: CKD Prediction Web Application
Purpose: Backend API for real-time CKD risk prediction
Author: BSCS-6th Semester, Machine Learning CCP

This Flask application provides:
- REST API endpoints for CKD prediction
- Web interface serving
- Model performance metrics
- Static plot visualization serving

API Endpoints:
- GET  /                  → Serve web interface (index.html)
- POST /predict           → Accept patient data, return CKD prediction
- GET  /results           → Return model performance metrics
- GET  /feature_info      → Return feature metadata for form building
- GET  /static/plots/<f>  → Serve visualization plots

================================================================================
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import numpy as np
import pandas as pd
import joblib
import json
import os
import traceback

print("="*80)
print("CKD PREDICTION API - INITIALIZING")
print("="*80)

# ============================================================================
# FLASK APP INITIALIZATION
# ============================================================================
app = Flask(__name__, static_folder="static", template_folder=".")
CORS(app)
print("✓ Flask app initialized with CORS enabled")

# ============================================================================
# FEATURE CONFIGURATION
# ============================================================================
ALL_FEATURES = [
    'age', 'bp', 'sg', 'al', 'su',
    'rbc', 'pc', 'pcc', 'ba',
    'bgr', 'bu', 'sc', 'sod', 'pot',
    'hemo', 'pcv', 'wbcc', 'rbcc',
    'htn', 'dm', 'cad', 'appet', 'pe', 'ane'
]

NUMERIC_COLS = ['age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc',
                'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc']

CATEGORICAL_COLS = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad',
                    'appet', 'pe', 'ane']

FEATURE_LABELS = {
    "age": "Age (years)",
    "bp": "Blood Pressure (mm/Hg)",
    "sg": "Specific Gravity",
    "al": "Albumin (0-5)",
    "su": "Sugar (0-5)",
    "rbc": "Red Blood Cells",
    "pc": "Pus Cell",
    "pcc": "Pus Cell Clumps",
    "ba": "Bacteria",
    "bgr": "Blood Glucose Random (mgs/dl)",
    "bu": "Blood Urea (mgs/dl)",
    "sc": "Serum Creatinine (mgs/dl)",
    "sod": "Sodium (mEq/L)",
    "pot": "Potassium (mEq/L)",
    "hemo": "Hemoglobin (gms)",
    "pcv": "Packed Cell Volume",
    "wbcc": "WBC Count (cells/cumm)",
    "rbcc": "RBC Count (millions/cmm)",
    "htn": "Hypertension",
    "dm": "Diabetes Mellitus",
    "cad": "Coronary Artery Disease",
    "appet": "Appetite",
    "pe": "Pedal Edema",
    "ane": "Anemia",
}

CATEGORICAL_OPTIONS = {
    "rbc": ["normal", "abnormal"],
    "pc": ["normal", "abnormal"],
    "pcc": ["present", "notpresent"],
    "ba": ["present", "notpresent"],
    "htn": ["yes", "no"],
    "dm": ["yes", "no"],
    "cad": ["yes", "no"],
    "appet": ["good", "poor"],
    "pe": ["yes", "no"],
    "ane": ["yes", "no"],
}

print(f"✓ Feature configuration loaded: {len(ALL_FEATURES)} features")

# ============================================================================
# LOAD TRAINED MODELS AND PREPROCESSING OBJECTS
# ============================================================================
print("Loading trained models and preprocessing objects...")

try:
    # Load best model
    MODEL = joblib.load("models/best_model.pkl")
    print(f"✓ Best model loaded: {MODEL.__class__.__name__}")

    # Load preprocessing objects
    IMPUTER = joblib.load("models/imputer.pkl")
    SCALER = joblib.load("models/scaler.pkl")
    LABEL_ENCODERS = joblib.load("models/label_encoders.pkl")
    FEATURE_NAMES = joblib.load("models/feature_names.pkl")
    RFE = joblib.load("models/rfe.pkl")
    print(f"✓ Preprocessing objects loaded")
    print(f"  - Imputer: {IMPUTER.__class__.__name__}")
    print(f"  - Scaler: {SCALER.__class__.__name__}")
    print(f"  - Label Encoders: {len(LABEL_ENCODERS)} encoders")
    print(f"  - RFE: {RFE.n_features_to_select} features selected")

    # Load results summary
    with open("models/results_summary.json") as f:
        RESULTS_SUMMARY = json.load(f)
    print(f"✓ Results summary loaded: {len(RESULTS_SUMMARY)} models")

    MODEL_LOADED = True

except FileNotFoundError as e:
    print(f"⚠ WARNING: Could not load model files")
    print(f"  Error: {e}")
    print(f"  Please run: python ckd_pipeline.py")
    MODEL = None
    IMPUTER = None
    SCALER = None
    LABEL_ENCODERS = None
    FEATURE_NAMES = ALL_FEATURES
    RFE = None
    RESULTS_SUMMARY = {}
    MODEL_LOADED = False

print("="*80)
print()

# ============================================================================
# PREPROCESSING FUNCTION FOR LIVE PREDICTIONS
# ============================================================================
def preprocess_input(data: dict) -> np.ndarray:
    """
    Preprocess raw patient input for model inference.

    This function applies the EXACT same preprocessing pipeline used during
    training to ensure consistency:
    1. Parse numeric fields → float (NaN for missing)
    2. Label encode categorical fields using saved encoders
    3. Build DataFrame with correct column order
    4. Impute missing values using saved imputer
    5. Scale features using saved scaler
    6. Apply RFE feature selection

    Parameters
    ----------
    data : dict
        Raw patient data from web form (24 key-value pairs)

    Returns
    -------
    np.ndarray
        Preprocessed feature array ready for model.predict()
        Shape: (1, n_selected_features)
    """

    row = {}

    # Step 1: Parse numeric fields
    for col in NUMERIC_COLS:
        val = data.get(col, "")
        try:
            row[col] = float(val) if val not in ("", None, "nan", "NaN") else np.nan
        except (ValueError, TypeError):
            row[col] = np.nan

    # Step 2: Label encode categorical fields
    for col in CATEGORICAL_COLS:
        val = str(data.get(col, "")).strip().lower()
        le = LABEL_ENCODERS.get(col)

        if le is not None:
            try:
                # Transform using saved encoder
                row[col] = float(le.transform([val])[0])
            except (ValueError, KeyError):
                # Unknown category → treat as missing
                row[col] = np.nan
        else:
            row[col] = np.nan

    # Step 3: Build DataFrame with correct column order
    df = pd.DataFrame([row], columns=FEATURE_NAMES)

    # Step 4: Impute missing values
    X_imputed = IMPUTER.transform(df)

    # Step 5: Scale features
    X_scaled = SCALER.transform(X_imputed)

    # Step 6: Apply RFE feature selection
    X_selected = RFE.transform(X_scaled)

    return X_selected


# ============================================================================
# API ROUTES
# ============================================================================

@app.route("/")
def index():
    """Serve the main web interface (index.html)"""
    return send_from_directory(".", "index.html")


@app.route("/static/plots/<path:filename>")
def serve_plot(filename):
    """Serve visualization plots from static/plots/ directory"""
    return send_from_directory("static/plots", filename)


@app.route("/predict", methods=["POST"])
def predict():
    """
    CKD Prediction Endpoint

    Accepts patient clinical data and returns CKD risk prediction.

    Request Body (JSON):
    --------------------
    {
        "age": 48,
        "bp": 80,
        "sg": 1.020,
        ...
        (24 features total)
    }

    Response (JSON):
    ----------------
    {
        "prediction": "CKD" or "Not CKD",
        "prediction_code": 1 or 0,
        "confidence": 95.5,
        "risk_level": "High" / "Medium" / "Low",
        "prob_ckd": 95.5,
        "prob_notckd": 4.5
    }
    """

    # Check if model is loaded
    if not MODEL_LOADED:
        return jsonify({
            "error": "Model not loaded. Please run: python ckd_pipeline.py"
        }), 503

    try:
        # Read JSON request body
        data = request.get_json(force=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Invalid input format. Expected JSON object."}), 400

        # Check if at least some data is provided
        if all(str(data.get(col, "")).strip() in ("", "nan", "NaN")
               for col in FEATURE_NAMES):
            return jsonify({
                "error": "No patient data provided. Please fill at least one field."
            }), 400

        # Preprocess input
        X_processed = preprocess_input(data)

        # Make prediction
        prediction = int(MODEL.predict(X_processed)[0])
        proba = MODEL.predict_proba(X_processed)[0]

        # Build response
        label = "CKD" if prediction == 1 else "Not CKD"
        confidence = round(max(proba) * 100, 1)

        # Risk level based on CKD probability
        if proba[1] >= 0.70:
            risk_level = "High"
        elif proba[1] >= 0.40:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        return jsonify({
            "prediction": label,
            "prediction_code": prediction,
            "confidence": confidence,
            "risk_level": risk_level,
            "prob_ckd": round(proba[1] * 100, 1),
            "prob_notckd": round(proba[0] * 100, 1),
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({
            "error": f"Prediction failed: {str(e)}"
        }), 500


@app.route("/results", methods=["GET"])
def results():
    """
    Return model performance metrics for all trained models.

    Response includes accuracy, precision, recall, F1-score, AUC-ROC,
    cross-validation accuracy, and confusion matrix for each model.
    """
    if not RESULTS_SUMMARY:
        return jsonify({
            "error": "Results not available. Please run: python ckd_pipeline.py"
        }), 503

    return jsonify(RESULTS_SUMMARY)


@app.route("/feature_info", methods=["GET"])
def feature_info():
    """
    Return feature metadata for dynamic form building.

    Includes:
    - Feature names (ordered list)
    - Human-readable labels
    - Categorical feature names
    - Valid options for each categorical feature
    """
    return jsonify({
        "features": FEATURE_NAMES,
        "labels": FEATURE_LABELS,
        "categorical": CATEGORICAL_COLS,
        "categorical_options": CATEGORICAL_OPTIONS,
    })


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "model_loaded": MODEL_LOADED,
        "models_available": len(RESULTS_SUMMARY) if RESULTS_SUMMARY else 0
    })


# ============================================================================
# START SERVER
# ============================================================================
if __name__ == "__main__":
    print()
    print("="*80)
    print("   CKD PREDICTION SYSTEM - FLASK API SERVER")
    print("="*80)
    print("   Web Interface  →  http://localhost:5000/")
    print("   Predict API    →  POST /predict")
    print("   Model Results  →  GET  /results")
    print("   Feature Info   →  GET  /feature_info")
    print("   Health Check   →  GET  /health")
    print("   Plots          →  GET  /static/plots/<filename>")
    print("="*80)
    print()

    if MODEL_LOADED:
        print("✓ All systems ready. Starting server...")
    else:
        print("⚠ Models not loaded. Run 'python ckd_pipeline.py' first.")
        print("  Server will start but predictions will fail.")

    print()
    app.run(debug=True, host="0.0.0.0", port=5000)
