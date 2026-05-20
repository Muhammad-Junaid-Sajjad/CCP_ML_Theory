**Lahore Garrison University**  
**Complex Computing Problem**  
***Department of Computer Sciences***

**Instructor’s Name: Sahar Moin**         
 **Program/Semester/: BSCS-6th                    		 Section: A,B,C**  
**Course Code: CSE6505			             Course Title: Machine Learning**  
**Time Allowed: 8 Weeks			             Max Marks: 30**

**Complex Computing Problem(Theory)**

The semester project has been designed to enable students to solve complex computing problems.  Specifically, this project focuses on addressing the following characteristics of such problems in the context of Machine Learning:

| SP-1 Depth of Knowledge required of these fields. Stats & Probability Linear Algebra Python Programming Skills Web Development |  | SP-3 Depth of Analysis required | SP-7 Interdependence |  |  |  |
| ----- | :---- | ----- | :---: | :---- | :---- | ----- |
| **CLO Mapping with GA/PLO** |  |  |  |  |  |  |
| **SR \#** | **CLO** |  |  | **PLO** | **BT Levels** |  |
| CLO 1 | **Understand** machine learning algorithms, tools, and techniques. |  |  | PLO2 | C \= 2, |  |
| CLO2 | **Apply** supervised and unsupervised learning, techniques for classification, regression. |  |  | PLO4 | C \= 3, |  |
| CLO5 | **Construct** real world machine learning solutions using supervised and unsupervised algorithms with modern machine learning tools and libraries. |  |  | PLO 5 | P-4 |  |

**CCP Statement:**

We aim to utilize machine learning techniques to solve a complex computing problem of predicting chronic kidney disease (CKD) using a healthcare dataset. The project will involve implementing **ensemble learning** algorithms such as Random Forest, Gradient Boosting, AdaBoost, and Voting Classifier to develop an accurate predictive model based on clinical patient data.

**Problem Identification:**

Chronic Kidney Disease is a major public health problem and one of the leading causes of serious health complications worldwide. Early detection of CKD is important because timely medical treatment can prevent the disease from progressing to kidney failure. However, diagnosing CKD based on clinical parameters can be challenging due to the large volume and complexity of healthcare data.

Machine learning techniques, particularly ensemble learning methods, can improve prediction performance by combining multiple models to produce more accurate and robust results. These methods help in handling complex patterns within medical datasets and reduce the risk of prediction errors.

One commonly used dataset for CKD prediction is the chronic kidney disease dataset from the UCI Machine Learning Repository, which contains multiple clinical features related to kidney health. Using this dataset, ensemble machine learning algorithms can be trained and evaluated to develop an effective system that predicts whether a patient is likely to have CKD.

**Dataset:**

CKD Prediction

[**https://archive.ics.uci.edu/ml/datasets/chronic\_kidney\_disease**](https://archive.ics.uci.edu/ml/datasets/chronic_kidney_disease)

**Deliverables:**

| Week | Deliverable | Description |
| :---- | :---- | :---- |
| Week 5 | Problem Understanding | Literature review and understanding CKD dataset and project objectives |
| Week 6 | Dataset Collection | Obtain CKD dataset and analyze dataset structure |
| Week 6 | Exploratory Data Analysis | Visualize data, identify patterns, correlations, and missing values |
| Week 7 | Data Preprocessing | Handle missing values, encode categorical features, and normalize data |
| Week 7-8 | Model Development | Implement multiple machine learning / ensemble algorithms |
| Week 9 | Model Evaluation | Compare models using accuracy, precision, recall, F1-score, and confusion matrix and cross validation |
| Week 10 | Web Interface Development | Develop a web interface to input patient data and connect with trained model |
| Week 11 | Final Integration & Report | Integrate system, finalize report, and prepare presentation |

**Marks Distribution:**

**Total Marks \= 30**

* Feature Computing: Understand the dataset using Exploratory Data Analysis (EDA). Perform preprocessing including data cleaning, handling missing values, normalization, and feature encoding to prepare the dataset for machine learning models. (**6 marks – CLO 1**)  
* Model Development: Implement ensemble machine learning algorithms such as Random Forest, Gradient Boosting, AdaBoost, and Voting/Stacking classifiers to build a predictive model for chronic kidney disease (CKD) using the dataset. (**6 marks – CLO 5**)  
* Model Evaluation: Evaluate the performance of each model using appropriate metrics including accuracy, precision, recall, F1-score, and confusion matrix to assess prediction effectiveness. 

(**6 marks – CLO 2**)

* Model Comparison: Compare the performance of at least four ensemble models to determine the most accurate and reliable algorithm for CKD prediction. (**6 marks – CLO 2**)  
* Documentation: Document the complete project pipeline including dataset description, preprocessing steps, model development, evaluation results, and system workflow, ensuring reproducibility and clarity of the machine learning solution. (**6 marks – CLO 1**)

**Overview:**

The project develops a predictive system to identify patients at risk of chronic kidney disease (CKD) using clinical data from a publicly available dataset. The data undergoes preprocessing steps such as cleaning, handling missing values, normalization, and feature encoding to prepare it for machine learning. Ensemble learning algorithms including Random Forest, Gradient Boosting, AdaBoost, and Voting classifiers are used to train models that analyze clinical features and detect patterns indicating CKD. Model performance is evaluated using accuracy, precision, recall, F1-score, and confusion matrices to identify the most reliable predictor.

The selected model is integrated into a web-based interface where users can input patient parameters such as blood pressure, hemoglobin level, and glucose level. Once submitted, the backend processes the data through the trained model and displays the prediction directly on the web interface, showing whether the patient is at risk of CKD. This end-to-end workflow—from data preprocessing and model training to real-time web-based prediction demonstrates how machine learning can enable early CKD detection, support healthcare decision-making, and provide a user-friendly system for medical professionals.

**Reference Paper:**

[**https://www.sciencedirect.com/science/article/abs/pii/S1746809423008017**](https://www.sciencedirect.com/science/article/abs/pii/S1746809423008017) 

**Rubrics:**

| Criteria | Excellent (5-6) | Good (3–4) | Needs Improvement (1–2) | Total |
| ----- | :---- | :---- | :---- | ----- |
| **Feature Computing & Preprocessing** | Thorough EDA; missing values handled; data normalized and encoded properly. | EDA done with minor gaps; some missing values or encoding issues. | Limited or incorrect EDA; missing values or encoding not handled. | **6** |
| **Model Development** | All ensemble models implemented correctly; modular and reusable code. | Models implemented with minor errors; limited modularity. | Models missing or incorrect; code not reusable. | **6** |
| **Model Evaluation** | Metrics calculated correctly; results clearly interpreted. | Metrics partially correct; limited interpretation. | Metrics missing or incorrect; no interpretation. | **6** |
| **Model Comparison** | ≥4 models compared; best model justified with insights. | Comparison done but lacks clarity or justification. | Comparison missing or inaccurate; no rationale. | **6** |
| **Documentation & Reproducibility** | Complete documentation; workflow and code fully reproducible. | Documentation mostly complete; minor reproducibility issues. | Documentation missing or unclear; workflow not reproducible. | **6** |
| **Total Maks** |  |  |  | **30** |

