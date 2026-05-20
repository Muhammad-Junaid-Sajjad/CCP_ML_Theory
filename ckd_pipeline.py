# ===============================
# CKD PREDICTION - FIXED VERSION (REALISTIC PROBABILITIES)
# ===============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os, warnings, joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.calibration import CalibratedClassifierCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

warnings.filterwarnings("ignore")

os.makedirs("models", exist_ok=True)
os.makedirs("plots", exist_ok=True)

# ===============================
# 1. LOAD DATA
# ===============================
cols = ['age','bp','sg','al','su','rbc','pc','pcc','ba','bgr','bu','sc',
        'sod','pot','hemo','pcv','wbcc','rbcc','htn','dm','cad',
        'appet','pe','ane','class']

df = pd.read_csv("kidney_disease.csv", names=cols, na_values=["?", " "])
df = df.drop(0).reset_index(drop=True)
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

# target encoding
df['class'] = df['class'].map({'ckd':1, 'notckd':0})

# ===============================
# 2. FEATURES / TARGET
# ===============================
X = df.drop('class', axis=1)
y = df['class']

num_cols = X.select_dtypes(include=np.number).columns
cat_cols = X.select_dtypes(include='object').columns

# ===============================
# 3. PREPROCESSING PIPELINE
# ===============================
numeric_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_pipe = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocess = ColumnTransformer([
    ("num", numeric_pipe, num_cols),
    ("cat", categorical_pipe, cat_cols)
])

# ===============================
# 4. TRAIN TEST SPLIT
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ===============================
# 5. BASE MODELS
# ===============================
rf = RandomForestClassifier(n_estimators=200, random_state=42)
gb = GradientBoostingClassifier()
ada = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=2),
    n_estimators=100
)

voting = VotingClassifier(
    estimators=[("rf", rf), ("gb", gb), ("ada", ada)],
    voting="soft"
)

models = {
    "Random Forest": rf,
    "Gradient Boosting": gb,
    "AdaBoost": ada,
    "Voting": voting
}

# ===============================
# 6. TRAIN + CALIBRATION (IMPORTANT FIX)
# ===============================
results = {}
best_model = None
best_f1 = 0

for name, model in models.items():

    pipe = Pipeline([
        ("prep", preprocess),
        ("model", model)
    ])

    pipe.fit(X_train, y_train)

    # 🔥 CALIBRATION STEP (FIXES 96% FALSE CONFIDENCE ISSUE)
    calibrated = CalibratedClassifierCV(pipe, method="sigmoid", cv=3)
    calibrated.fit(X_train, y_train)

    pred = calibrated.predict(X_test)
    proba = calibrated.predict_proba(X_test)[:,1]

    acc = accuracy_score(y_test, pred)
    prec = precision_score(y_test, pred)
    rec = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)
    auc = roc_auc_score(y_test, proba)

    print("\n====================")
    print(name)
    print("====================")
    print("Accuracy:", acc)
    print("Precision:", prec)
    print("Recall:", rec)
    print("F1:", f1)
    print("AUC:", auc)

    results[name] = {
        "model": calibrated,
        "f1": f1,
        "auc": auc
    }

    joblib.dump(calibrated, f"models/{name}.pkl")

    if f1 > best_f1:
        best_f1 = f1
        best_model = calibrated

# ===============================
# 7. SAVE BEST MODEL
# ===============================
joblib.dump(best_model, "models/best_model.pkl")

print("\n✔ BEST MODEL SAVED")

# ===============================
# 8. REALISTIC PREDICTION FUNCTION (FIXED OUTPUT)
# ===============================
def predict_risk(model, sample):

    prob = model.predict_proba(sample)[0][1]

    # 🔥 FIXED THRESHOLDS (no fake always-high risk)
    if prob > 0.75:
        risk = "High"
    elif prob > 0.4:
        risk = "Medium"
    else:
        risk = "Low"

    print("\n========================")
    print("CKD RISK REPORT")
    print("========================")
    print(f"Kidney Failure Probability: {round(prob*100,2)}%")
    print(f"Healthy Probability: {round((1-prob)*100,2)}%")
    print(f"Risk Level: {risk}")

    return prob, risk


# ===============================
# 9. TEST SAMPLE (IMPORTANT)
# ===============================
sample = X_test.iloc[[0]]
predict_risk(best_model, sample)

print("\n✔ PIPELINE COMPLETE (FIXED VERSION)")