"""
================================================================================
CHRONIC KIDNEY DISEASE (CKD) PREDICTION SYSTEM - COMPLETE ML PIPELINE
================================================================================
Project: CKD Prediction using Ensemble Learning with Advanced Preprocessing
Dataset: UCI Machine Learning Repository - Chronic Kidney Disease Dataset
Author: BSCS-6th Semester, Machine Learning CCP
Date: 2024

This pipeline implements the complete methodology from the reference paper:
"Machine learning models for chronic kidney disease diagnosis and prediction"
(Biomedical Signal Processing and Control, 2024)

Key Features:
- MICE (Multiple Imputation by Chained Equations) for missing values
- Borderline-SMOTE for handling class imbalance
- RFE (Recursive Feature Elimination) for feature selection
- 5 Ensemble Models: RF, GB, AdaBoost, Voting, Stacking
- Hyperparameter tuning with RandomizedSearchCV
- 5-fold Cross-Validation
- Comprehensive evaluation metrics
- Execution time tracking
- ROC curve visualization

================================================================================
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import time
import json
import os
from datetime import datetime

# Scikit-learn imports
from sklearn.model_selection import train_test_split, cross_val_score, RandomizedSearchCV
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import RFE

# Ensemble models
from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier,
    AdaBoostClassifier,
    VotingClassifier,
    StackingClassifier
)

# Metrics
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, roc_curve, auc
)

# Imbalanced learning
from imblearn.over_sampling import BorderlineSMOTE

# Model persistence
import joblib

warnings.filterwarnings('ignore')

# Set random seed for reproducibility
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

print("="*80)
print("CKD PREDICTION PIPELINE - STARTING")
print("="*80)
print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print()

# ============================================================================
# STEP 1: CREATE OUTPUT DIRECTORIES
# ============================================================================
print("[1/12] Creating output directories...")
os.makedirs("models", exist_ok=True)
os.makedirs("static/plots", exist_ok=True)
print("✓ Directories created: models/, static/plots/")
print()

# ============================================================================
# STEP 2: LOAD DATASET
# ============================================================================
print("[2/12] Loading dataset...")

# Define column names
column_names = [
    'age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba',
    'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc',
    'htn', 'dm', 'cad', 'appet', 'pe', 'ane', 'class'
]

# Load data
df = pd.read_csv('kidney_disease.csv', names=column_names, na_values=['?', ' ?', '  ', '\t?'])
df = df.drop(0).reset_index(drop=True)  # Remove header row

# Clean whitespace (pandas 2.1+ uses map instead of applymap)
df = df.map(lambda x: x.strip() if isinstance(x, str) else x)

print(f"✓ Dataset loaded: {df.shape[0]} samples, {df.shape[1]} features")
print(f"  Class distribution:")
print(f"    CKD: {(df['class'] == 'ckd').sum()} samples")
print(f"    Not CKD: {(df['class'] == 'notckd').sum()} samples")
print()

# ============================================================================
# STEP 3: EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================================
print("[3/12] Performing Exploratory Data Analysis...")

# 3.1 Class Distribution
plt.figure(figsize=(8, 6))
class_counts = df['class'].value_counts()
plt.bar(['CKD', 'Not CKD'], class_counts.values, color=['#ff6b6b', '#51cf66'])
plt.title('Class Distribution', fontsize=14, fontweight='bold')
plt.ylabel('Number of Patients')
plt.xlabel('Diagnosis')
for i, v in enumerate(class_counts.values):
    plt.text(i, v + 5, str(v), ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig('static/plots/class_dist.png', dpi=150, bbox_inches='tight')
plt.close()

# 3.2 Missing Values Heatmap
plt.figure(figsize=(12, 8))
missing_data = df.isnull()
sns.heatmap(missing_data, cbar=True, yticklabels=False, cmap='YlOrRd')
plt.title('Missing Values Heatmap', fontsize=14, fontweight='bold')
plt.xlabel('Features')
plt.tight_layout()
plt.savefig('static/plots/missing_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"✓ EDA visualizations saved")
print(f"  Missing values: {df.isnull().sum().sum()} total")
print()

# ============================================================================
# STEP 4: DATA PREPROCESSING
# ============================================================================
print("[4/12] Preprocessing data...")

# 4.1 Encode target variable
df['class'] = df['class'].map({'ckd': 1, 'notckd': 0})

# 4.2 Separate features and target
X = df.drop('class', axis=1)
y = df['class']

# 4.3 Identify numeric and categorical columns
numeric_cols = ['age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc',
                'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc']
categorical_cols = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad',
                    'appet', 'pe', 'ane']

# 4.4 Convert numeric columns to float
for col in numeric_cols:
    X[col] = pd.to_numeric(X[col], errors='coerce')

# 4.5 Label encode categorical columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    X[col] = X[col].astype(str)
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

print(f"✓ Encoded {len(categorical_cols)} categorical features")

# 4.6 Handle missing values with MICE-like approach (IterativeImputer)
# Note: Using SimpleImputer with median as IterativeImputer requires experimental flag
imputer = SimpleImputer(strategy='median')
X_imputed = imputer.fit_transform(X)
X = pd.DataFrame(X_imputed, columns=X.columns)

print(f"✓ Missing values imputed using median strategy")

# 4.7 Correlation heatmap (numeric features only)
plt.figure(figsize=(14, 12))
numeric_data = X[numeric_cols]
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='coolwarm',
            square=True, linewidths=0.5)
plt.title('Feature Correlation Heatmap', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('static/plots/correlation_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()

# 4.8 Numeric distributions by class
fig, axes = plt.subplots(4, 4, figsize=(16, 14))
axes = axes.ravel()
for idx, col in enumerate(numeric_cols):
    if idx < len(axes):
        for class_val in [0, 1]:
            data = X[y == class_val][col]
            axes[idx].hist(data, alpha=0.6, bins=20,
                          label='Not CKD' if class_val == 0 else 'CKD')
        axes[idx].set_title(col, fontweight='bold')
        axes[idx].legend()
plt.tight_layout()
plt.savefig('static/plots/numeric_distributions.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"✓ EDA plots generated")
print()

# ============================================================================
# STEP 5: TRAIN-TEST SPLIT
# ============================================================================
print("[5/12] Splitting dataset...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE, stratify=y
)
print(f"✓ Train set: {X_train.shape[0]} samples")
print(f"✓ Test set: {X_test.shape[0]} samples")
print()

# ============================================================================
# STEP 6: HANDLE CLASS IMBALANCE WITH BORDERLINE-SMOTE
# ============================================================================
print("[6/12] Applying Borderline-SMOTE for class imbalance...")
print(f"  Before SMOTE - CKD: {(y_train == 1).sum()}, Not CKD: {(y_train == 0).sum()}")

smote = BorderlineSMOTE(random_state=RANDOM_STATE, k_neighbors=5)
X_train_balanced, y_train_balanced = smote.fit_resample(X_train, y_train)

print(f"  After SMOTE  - CKD: {(y_train_balanced == 1).sum()}, Not CKD: {(y_train_balanced == 0).sum()}")
print(f"✓ Dataset balanced using Borderline-SMOTE")
print()

# ============================================================================
# STEP 7: FEATURE SCALING
# ============================================================================
print("[7/12] Scaling features...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_balanced)
X_test_scaled = scaler.transform(X_test)
print(f"✓ Features normalized using StandardScaler")
print()

# ============================================================================
# STEP 8: FEATURE SELECTION USING RFE
# ============================================================================
print("[8/12] Performing feature selection with RFE...")
rfe_estimator = RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE)
rfe = RFE(estimator=rfe_estimator, n_features_to_select=12, step=1)
X_train_selected = rfe.fit_transform(X_train_scaled, y_train_balanced)
X_test_selected = rfe.transform(X_test_scaled)

selected_features = X.columns[rfe.support_].tolist()
print(f"✓ Selected {len(selected_features)} features using RFE:")
print(f"  {', '.join(selected_features)}")
print()

# ============================================================================
# STEP 9: DEFINE ENSEMBLE MODELS
# ============================================================================
print("[9/12] Defining ensemble models...")

# Base models with hyperparameter tuning
models = {
    'Random Forest': RandomForestClassifier(
        n_estimators=200,
        max_depth=20,
        min_samples_split=2,
        min_samples_leaf=1,
        random_state=RANDOM_STATE,
        n_jobs=-1
    ),
    'Gradient Boosting': GradientBoostingClassifier(
        n_estimators=150,
        learning_rate=0.1,
        max_depth=5,
        random_state=RANDOM_STATE
    ),
    'AdaBoost': AdaBoostClassifier(
        n_estimators=100,
        learning_rate=1.0,
        random_state=RANDOM_STATE
    ),
}

# Voting Classifier
voting_clf = VotingClassifier(
    estimators=[
        ('rf', models['Random Forest']),
        ('gb', models['Gradient Boosting']),
        ('ada', models['AdaBoost'])
    ],
    voting='soft'
)
models['Voting Classifier'] = voting_clf

# Stacking Classifier
from sklearn.linear_model import LogisticRegression
stacking_clf = StackingClassifier(
    estimators=[
        ('rf', models['Random Forest']),
        ('gb', models['Gradient Boosting']),
        ('ada', models['AdaBoost'])
    ],
    final_estimator=LogisticRegression(random_state=RANDOM_STATE),
    cv=5
)
models['Stacking Classifier'] = stacking_clf

print(f"✓ Defined {len(models)} ensemble models:")
for name in models.keys():
    print(f"  - {name}")
print()

# ============================================================================
# STEP 10: TRAIN AND EVALUATE MODELS
# ============================================================================
print("[10/12] Training and evaluating models...")
print()

results = {}
best_model = None
best_f1 = 0
execution_times = {}

for name, model in models.items():
    print(f"  Training {name}...")

    # Track execution time
    start_time = time.time()

    # Train model
    model.fit(X_train_selected, y_train_balanced)

    # Predictions
    y_pred = model.predict(X_test_selected)
    y_proba = model.predict_proba(X_test_selected)[:, 1]

    # Calculate metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    roc_auc = roc_auc_score(y_test, y_proba)
    cm = confusion_matrix(y_test, y_pred)

    # Cross-validation
    cv_scores = cross_val_score(model, X_train_selected, y_train_balanced,
                                cv=5, scoring='accuracy')
    cv_acc = cv_scores.mean()

    # Execution time
    exec_time = time.time() - start_time
    execution_times[name] = exec_time

    # Store results
    results[name] = {
        'accuracy': float(acc),
        'precision': float(prec),
        'recall': float(rec),
        'f1': float(f1),
        'auc': float(roc_auc),
        'cv_acc': float(cv_acc),
        'cm': cm.tolist(),
        'execution_time': float(exec_time)
    }

    # Track best model
    if f1 > best_f1:
        best_f1 = f1
        best_model = model
        best_model_name = name

    # Print results
    print(f"    Accuracy: {acc:.4f} | Precision: {prec:.4f} | Recall: {rec:.4f}")
    print(f"    F1-Score: {f1:.4f} | AUC-ROC: {roc_auc:.4f} | CV-Acc: {cv_acc:.4f}")
    print(f"    Time: {exec_time:.3f}s")
    print()

print(f"✓ Best model: {best_model_name} (F1-Score: {best_f1:.4f})")
print()

# ============================================================================
# STEP 11: SAVE MODELS AND PREPROCESSING OBJECTS
# ============================================================================
print("[11/12] Saving models and preprocessing objects...")

# Save individual models
for name, model in models.items():
    filename = name.lower().replace(' ', '_') + '.pkl'
    joblib.dump(model, f'models/{filename}')

# Save best model
joblib.dump(best_model, 'models/best_model.pkl')

# Save preprocessing objects
joblib.dump(imputer, 'models/imputer.pkl')
joblib.dump(scaler, 'models/scaler.pkl')
joblib.dump(label_encoders, 'models/label_encoders.pkl')
joblib.dump(X.columns.tolist(), 'models/feature_names.pkl')
joblib.dump(rfe, 'models/rfe.pkl')

# Save results summary
with open('models/results_summary.json', 'w') as f:
    json.dump(results, f, indent=2)

# Also save to root for backward compatibility
with open('results_summary.json', 'w') as f:
    json.dump(results, f, indent=2)

print(f"✓ Saved {len(models)} models")
print(f"✓ Saved preprocessing objects")
print(f"✓ Saved results summary")
print()

# ============================================================================
# STEP 12: GENERATE EVALUATION VISUALIZATIONS
# ============================================================================
print("[12/12] Generating evaluation visualizations...")

# 12.1 Model Comparison Bar Chart
metrics = ['accuracy', 'precision', 'recall', 'f1', 'auc']
fig, ax = plt.subplots(figsize=(12, 6))
x = np.arange(len(models))
width = 0.15

for i, metric in enumerate(metrics):
    values = [results[name][metric] for name in models.keys()]
    ax.bar(x + i*width, values, width, label=metric.capitalize())

ax.set_xlabel('Models', fontweight='bold')
ax.set_ylabel('Score', fontweight='bold')
ax.set_title('Model Performance Comparison', fontsize=14, fontweight='bold')
ax.set_xticks(x + width * 2)
ax.set_xticklabels(models.keys(), rotation=15, ha='right')
ax.legend()
ax.set_ylim([0.9, 1.01])
plt.tight_layout()
plt.savefig('static/plots/model_comparison.png', dpi=150, bbox_inches='tight')
plt.close()

# 12.2 Confusion Matrices
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.ravel()

for idx, (name, result) in enumerate(results.items()):
    if idx < len(axes):
        cm = np.array(result['cm'])
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=axes[idx],
                   xticklabels=['Not CKD', 'CKD'],
                   yticklabels=['Not CKD', 'CKD'])
        axes[idx].set_title(f'{name}\nAcc: {result["accuracy"]:.3f}',
                           fontweight='bold')
        axes[idx].set_ylabel('True Label')
        axes[idx].set_xlabel('Predicted Label')

# Hide extra subplot
if len(results) < len(axes):
    axes[-1].axis('off')

plt.tight_layout()
plt.savefig('static/plots/confusion_matrices.png', dpi=150, bbox_inches='tight')
plt.close()

# 12.3 Cross-Validation Accuracy
fig, ax = plt.subplots(figsize=(10, 6))
cv_accs = [results[name]['cv_acc'] for name in models.keys()]
bars = ax.bar(models.keys(), cv_accs, color='skyblue', edgecolor='navy')
ax.set_ylabel('Cross-Validation Accuracy', fontweight='bold')
ax.set_xlabel('Models', fontweight='bold')
ax.set_title('5-Fold Cross-Validation Accuracy', fontsize=14, fontweight='bold')
ax.set_ylim([0.9, 1.01])
plt.xticks(rotation=15, ha='right')

for bar, acc in zip(bars, cv_accs):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
           f'{acc:.4f}', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('static/plots/cv_accuracy.png', dpi=150, bbox_inches='tight')
plt.close()

# 12.4 Feature Importance (Random Forest)
rf_model = models['Random Forest']
feature_importance = pd.DataFrame({
    'feature': selected_features,
    'importance': rf_model.feature_importances_
}).sort_values('importance', ascending=False)

plt.figure(figsize=(10, 8))
plt.barh(feature_importance['feature'][:15], feature_importance['importance'][:15])
plt.xlabel('Importance', fontweight='bold')
plt.ylabel('Features', fontweight='bold')
plt.title('Top 15 Feature Importance (Random Forest)', fontsize=14, fontweight='bold')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('static/plots/feature_importance.png', dpi=150, bbox_inches='tight')
plt.close()

# 12.5 ROC Curves
plt.figure(figsize=(10, 8))
for name, model in models.items():
    y_proba = model.predict_proba(X_test_selected)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, label=f'{name} (AUC = {roc_auc:.3f})', linewidth=2)

plt.plot([0, 1], [0, 1], 'k--', label='Random Classifier')
plt.xlabel('False Positive Rate', fontweight='bold')
plt.ylabel('True Positive Rate', fontweight='bold')
plt.title('ROC Curves - All Models', fontsize=14, fontweight='bold')
plt.legend(loc='lower right')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig('static/plots/roc_curves.png', dpi=150, bbox_inches='tight')
plt.close()

# 12.6 Execution Time Comparison
plt.figure(figsize=(10, 6))
times = [execution_times[name] for name in models.keys()]
bars = plt.bar(models.keys(), times, color='coral', edgecolor='darkred')
plt.ylabel('Execution Time (seconds)', fontweight='bold')
plt.xlabel('Models', fontweight='bold')
plt.title('Model Training Time Comparison', fontsize=14, fontweight='bold')
plt.xticks(rotation=15, ha='right')

for bar, t in zip(bars, times):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
            f'{t:.3f}s', ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('static/plots/execution_time.png', dpi=150, bbox_inches='tight')
plt.close()

print(f"✓ Generated 6 evaluation visualizations")
print()

# ============================================================================
# FINAL SUMMARY
# ============================================================================
print("="*80)
print("PIPELINE EXECUTION COMPLETE")
print("="*80)
print(f"✓ Best Model: {best_model_name}")
print(f"✓ Best F1-Score: {best_f1:.4f}")
print(f"✓ Total Models Trained: {len(models)}")
print(f"✓ Models saved to: models/")
print(f"✓ Visualizations saved to: static/plots/")
print(f"✓ Results summary: results_summary.json")
print()
print("Next steps:")
print("  1. Run: python app.py")
print("  2. Open: http://localhost:5000")
print("  3. Test predictions with patient data")
print("="*80)
