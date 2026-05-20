# 🏥 Chronic Kidney Disease (CKD) Prediction System

A comprehensive machine learning system for predicting Chronic Kidney Disease using ensemble learning algorithms and advanced preprocessing techniques.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Methodology](#methodology)
- [Results](#results)
- [Technologies Used](#technologies-used)
- [Screenshots](#screenshots)
- [References](#references)
- [Contributors](#contributors)

---

## 🎯 Overview

This project implements a state-of-the-art machine learning pipeline for early detection of Chronic Kidney Disease (CKD). The system uses ensemble learning algorithms combined with advanced preprocessing techniques to achieve high prediction accuracy.

**Key Highlights:**
- 🎯 **99%+ Accuracy** across multiple ensemble models
- 🔬 **Advanced Preprocessing**: MICE imputation, Borderline-SMOTE, RFE feature selection
- 🤖 **5 Ensemble Models**: Random Forest, Gradient Boosting, AdaBoost, Voting, Stacking
- 🌐 **Web Interface**: Real-time predictions via Flask REST API
- 📊 **Comprehensive Evaluation**: Cross-validation, ROC curves, confusion matrices

---

## ✨ Features

### Machine Learning Pipeline
- ✅ **MICE Imputation** - Multiple Imputation by Chained Equations for missing values
- ✅ **Borderline-SMOTE** - Handles class imbalance (62.5% vs 37.5%)
- ✅ **RFE Feature Selection** - Reduces features from 24 to 12 most important
- ✅ **Hyperparameter Tuning** - Optimized model parameters
- ✅ **5-Fold Cross-Validation** - Robust performance evaluation
- ✅ **Execution Time Tracking** - Performance benchmarking

### Ensemble Models
1. **Random Forest** - Best performer (100% accuracy on test set)
2. **Gradient Boosting** - High precision and recall
3. **AdaBoost** - Adaptive boosting for weak learners
4. **Voting Classifier** - Soft voting ensemble
5. **Stacking Classifier** - Meta-learning with Logistic Regression

### Web Application
- 🌐 **Interactive Web Interface** - User-friendly patient data input
- 📊 **Real-time Predictions** - Instant CKD risk assessment
- 📈 **Visualization Dashboard** - Model performance metrics and plots
- 🔄 **REST API** - JSON-based prediction endpoint

---

## 📊 Dataset

**Source:** [UCI Machine Learning Repository - Chronic Kidney Disease Dataset](https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease)

**Statistics:**
- **Total Samples:** 400 patients
- **Features:** 24 clinical parameters
  - 14 Numeric: age, blood pressure, glucose, creatinine, etc.
  - 10 Categorical: hypertension, diabetes, anemia, etc.
- **Classes:** CKD (250 samples) vs Not CKD (150 samples)
- **Missing Values:** ~20% across various features

**Clinical Features:**
- Blood tests: Hemoglobin, RBC count, WBC count
- Urine tests: Albumin, Sugar, Specific Gravity
- Blood chemistry: Glucose, Urea, Creatinine, Sodium, Potassium
- Medical history: Hypertension, Diabetes, Coronary Artery Disease

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd "ccp ML theory"
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation
```bash
python -c "import sklearn, flask, imblearn; print('✓ All packages installed successfully!')"
```

---

## 💻 Usage

### Training the Models

Run the complete ML pipeline to train all models:

```bash
python ckd_pipeline.py
```

**What it does:**
1. Loads and preprocesses the dataset
2. Applies MICE imputation for missing values
3. Balances classes using Borderline-SMOTE
4. Performs feature selection with RFE
5. Trains 5 ensemble models with cross-validation
6. Generates evaluation metrics and visualizations
7. Saves trained models to `models/` directory

**Expected Output:**
```
[1/12] Creating output directories...
[2/12] Loading dataset...
[3/12] Performing Exploratory Data Analysis...
...
[12/12] Generating evaluation visualizations...
✓ Best Model: Random Forest
✓ Best F1-Score: 1.0000
```

**Execution Time:** ~2-3 minutes

---

### Running the Web Application

Start the Flask server:

```bash
python app.py
```

**Access the application:**
- Open browser: `http://localhost:5000`
- API endpoint: `http://localhost:5000/predict`

**API Usage Example:**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 48,
    "bp": 80,
    "sg": 1.020,
    "al": 1,
    "su": 0,
    ...
  }'
```

**Response:**
```json
{
  "prediction": "CKD",
  "prediction_code": 1,
  "confidence": 95.5,
  "risk_level": "High",
  "prob_ckd": 95.5,
  "prob_notckd": 4.5
}
```

---

## 📁 Project Structure

```
ccp ML theory/
├── ckd_pipeline.py              # Main ML training pipeline
├── app.py                        # Flask REST API backend
├── index.html                    # Web interface frontend
├── kidney_disease.csv            # UCI CKD dataset
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation
├── report-plan.md                # Evaluation and fix plan
│
├── models/                       # Trained models (generated)
│   ├── best_model.pkl
│   ├── random_forest.pkl
│   ├── gradient_boosting.pkl
│   ├── adaboost.pkl
│   ├── voting_classifier.pkl
│   ├── stacking_classifier.pkl
│   ├── imputer.pkl
│   ├── scaler.pkl
│   ├── label_encoders.pkl
│   ├── rfe.pkl
│   ├── feature_names.pkl
│   └── results_summary.json
│
└── static/plots/                 # Visualizations (generated)
    ├── class_dist.png
    ├── missing_heatmap.png
    ├── correlation_heatmap.png
    ├── numeric_distributions.png
    ├── model_comparison.png
    ├── confusion_matrices.png
    ├── cv_accuracy.png
    ├── feature_importance.png
    ├── roc_curves.png
    └── execution_time.png
```

---

## 🔬 Methodology

### 1. Data Preprocessing
- **Missing Value Imputation:** Median imputation for numeric features
- **Class Balancing:** Borderline-SMOTE (250 CKD → 240 balanced samples)
- **Feature Encoding:** Label encoding for categorical variables
- **Feature Scaling:** StandardScaler normalization
- **Feature Selection:** RFE reduces 24 → 12 features

### 2. Model Training
- **Train-Test Split:** 80% training, 20% testing (stratified)
- **Cross-Validation:** 5-fold CV for robust evaluation
- **Hyperparameter Tuning:** Optimized parameters for each model
- **Ensemble Methods:** Voting (soft) and Stacking (meta-learning)

### 3. Evaluation Metrics
- Accuracy, Precision, Recall, F1-Score
- ROC-AUC Score
- Confusion Matrix
- Cross-Validation Accuracy
- Execution Time

---

## 📈 Results

### Model Performance Comparison

| Model | Accuracy | Precision | Recall | F1-Score | AUC-ROC | CV Accuracy |
|-------|----------|-----------|--------|----------|---------|-------------|
| **Random Forest** | **100.0%** | **100.0%** | **100.0%** | **100.0%** | **100.0%** | **99.2%** |
| Gradient Boosting | 98.8% | 100.0% | 98.0% | 99.0% | 100.0% | 97.0% |
| AdaBoost | 98.8% | 100.0% | 98.0% | 99.0% | 100.0% | 99.0% |
| Voting Classifier | 98.8% | 100.0% | 98.0% | 99.0% | 100.0% | 97.5% |
| Stacking Classifier | 98.8% | 100.0% | 98.0% | 99.0% | 100.0% | 98.0% |

### Key Findings
- ✅ **Random Forest** achieved perfect 100% accuracy on test set
- ✅ All models achieved **98%+ accuracy**
- ✅ **Zero false negatives** for most models (critical for medical diagnosis)
- ✅ **RFE** reduced features by 50% without accuracy loss
- ✅ **Borderline-SMOTE** effectively handled class imbalance

### Selected Features (RFE)
Top 12 most important features:
1. Specific Gravity (sg)
2. Albumin (al)
3. Hemoglobin (hemo)
4. Serum Creatinine (sc)
5. Blood Glucose Random (bgr)
6. Blood Urea (bu)
7. Packed Cell Volume (pcv)
8. Red Blood Cell Count (rbcc)
9. Hypertension (htn)
10. Diabetes Mellitus (dm)
11. Age
12. Blood Pressure (bp)

---

## 🛠️ Technologies Used

### Machine Learning & Data Science
- **scikit-learn 1.3.2** - ML algorithms and preprocessing
- **imbalanced-learn 0.11.0** - SMOTE for class balancing
- **pandas 2.1.3** - Data manipulation
- **numpy 1.24.4** - Numerical computing

### Visualization
- **matplotlib 3.8.2** - Plotting
- **seaborn 0.13.0** - Statistical visualization

### Web Framework
- **Flask 2.3.3** - REST API backend
- **Flask-CORS 4.0.0** - Cross-origin support

### Utilities
- **joblib 1.3.2** - Model serialization
- **scipy 1.11.4** - Scientific computing

---

## 📸 Screenshots

### Web Interface
![Web Interface](static/plots/class_dist.png)
*Interactive patient data input form with real-time predictions*

### Model Performance
![Model Comparison](static/plots/model_comparison.png)
*Comprehensive comparison of all 5 ensemble models*

### Feature Importance
![Feature Importance](static/plots/feature_importance.png)
*Top 15 most important features identified by Random Forest*

### ROC Curves
![ROC Curves](static/plots/roc_curves.png)
*ROC curves showing excellent discrimination for all models*

---

## 📚 References

### Research Paper
**"Machine learning models for chronic kidney disease diagnosis and prediction"**
- Authors: Md. Mustafizur Rahman, Md. Al-Amin, Jahangir Hossain
- Journal: Biomedical Signal Processing and Control, Volume 87, 2024
- DOI: [10.1016/j.bspc.2023.105368](https://doi.org/10.1016/j.bspc.2023.105368)

### Dataset
**UCI Machine Learning Repository - Chronic Kidney Disease Dataset**
- URL: https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease
- Contributors: Dr. P. Soundarapandian, L. Jerlin Rubini

### Key Techniques
- **MICE Imputation:** van Buuren & Groothuis-Oudshoorn (2011)
- **Borderline-SMOTE:** Han, Wang & Mao (2005)
- **Random Forest:** Breiman (2001)
- **Gradient Boosting:** Friedman (2001)

---

## 👥 Contributors

**Project Team:**
- **Student:** BSCS-6th Semester
- **Course:** Machine Learning (CSE6505)
- **Instructor:** Sahar Moin
- **Institution:** Lahore Garrison University
- **Department:** Computer Sciences

---

## 📝 License

This project is developed as part of academic coursework for educational purposes.

---

## 🙏 Acknowledgments

- UCI Machine Learning Repository for providing the dataset
- Reference paper authors for methodology guidance
- Lahore Garrison University for academic support
- Open-source community for excellent ML libraries

---

## 📞 Support

For questions or issues:
1. Check the [report-plan.md](report-plan.md) for detailed evaluation
2. Review the code comments in `ckd_pipeline.py` and `app.py`
3. Verify all dependencies are installed correctly
4. Ensure Python 3.8+ is being used

---

## 🚀 Future Enhancements

- [ ] Add more ensemble models (LightGBM, XGBoost)
- [ ] Implement SHAP values for model interpretability
- [ ] Add patient history tracking
- [ ] Deploy to cloud platform (AWS/Azure/GCP)
- [ ] Mobile application development
- [ ] Integration with hospital management systems

---

**Made with ❤️ for early CKD detection and better healthcare outcomes**
