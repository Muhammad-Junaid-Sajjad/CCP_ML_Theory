Biomedical Signal Processing and Control 87 (2024) 105368 

Contents lists available at ScienceDirect  

Biomedical Signal Processing and Control  

journal homepage: www.elsevier.com/locate/bspc  

Machine learning models for chronic kidney disease diagnosis  and prediction  

Md. Mustafizur Rahman a,b,\*, Md. Al-Amin a, Jahangir Hossain b  a *Department of Electrical and Electronic Engineering, Jashore University of Science and Technology, Jashore 7408, Bangladesh* b *School of Electrical and Data Engineering, University of Technology Sydney, 15 Broadway, Sydney, NSW 2007, Australia*  

ARTICLE INFO  

*Keywords:*    
Chronic kidney disease  Ensemble machine learning  Borderline-SMOTE    
MICE    
Prediction  

**1\. Introduction**    
ABSTRACT  

*Background and objective:* Chronic kidney disease is a severe health problem that affects people all over the world,  particularly in South Asia. Therefore, proper diagnosis and treatment are required as early as possible. The main  goal of this study is to detect the presence or absence of CKD in the human body utilizing a variety of features  grasped from a few medical tests.  

*Methods:* This paper has focused on eight ensemble learning methods for diagnosing CKD on the UCI machine  learning datasets. The datasets have been fixed by imputing the missing values using the MICE imputation  method and handling the imbalance properties using the borderline SVMSMOTE method to improve the per formance of classifiers. Moreover, recursive feature elimination and the boruta method have been used to find  the most significant features and reduce the compilation time, while the hyperparameter tuning technique was  used to raise the performance of classifiers and get optimal solutions.    
*Results:* Taking the most significant feature into consideration, RFE outperformed boruta and selected only 50%  of the total features. Moreover, various performance matrices are used to find the best competent classifiers for  detecting CKD. LightGBM outperformed state-of-the-art and other ensemble methods with the lowest compila tion time and highest accuracy. Based on experimental findings, the proposed method achieved the highest  average of 99.75% accuracy, 99.40% precision, 99.41% recall, 99.61% F-measure and 99.57% AUC-ROC.  Moreover, our proposed method rises the average detection rate by 5.64%, 1%, 2.04%, 8.63%,1.99%, 2.84%,    
2.42% and 4.76%, respectively, in comparison with different approaches performing on the same dataset.  *Conclusion:* Experiments show that our suggested method can identify CKD more precisely than the most recent  methods.  

test indicates the severity of kidney disease. When the kidneys fail to    
work, extra fluid and waste stay in the body, potentially leading to    
Nowadays, chronic kidney diseases (CKD) are a leading cause of  death worldwide. CKD is a long-term disorderliness in which the kidneys  losses of its function gradually, and sometimes it can lead to kidney  failure \[1\]. Although significant improvements have been achieved in  the treatment of CKD, it is too costly, and its prevalence is steadily  increasing, which affect the expected life of human. Usually, many  people cannot identify CKD in the early stage because it does not show  any symptoms in the early stage \[2\]. Therefore, detection of CKD is  possible only in the advanced stage of disease when some symptoms  occur. However, it can quickly identify if someone has CKD through  blood and urine test. The levels of creatinine in the blood and protein in  the urine are determined in these two tests. The result of blood and urine    
various health issues such as heart disease and stroke. Furthermore,  various illnesses like high blood pressure, diabetes, cholesterol, and  glomerulonephritis can raise the menace of CKD \[3\]. Therefore, the  disclosure of CKD in the primary stage can assist provide advanced  treatment and preventive actions to reduce the need for dialysis or  kidney transplantation. Although chronic kidney disease (CKD) cannot  always be prevented, doctors can take the necessary steps to lower our  risks of developing it. Fig. 1 represents the factors that increase the risk  of CKD. Artificial Intelligence systems such as machine learning and  deep learning can detect and diagnose CKD in the early state \[4\].  

The primary purpose of this research is to determine whether or not a  person has CKD using various features obtained from some clinical tests.  

\* Corresponding author: Department of Electrical and Electronic Engineering, Jashore University of Science and Technology, Jashore 7408, Bangladesh.  *E-mail addresses:* mustafizur.170710@gmail.com (Md. Mustafizur Rahman), ma.amin@just.edu.bd (Md. Al-Amin), jahangir.hossain@uts.edu.au (J. Hossain).  

https://doi.org/10.1016/j.bspc.2023.105368  

Received 4 April 2023; Received in revised form 24 June 2023; Accepted 14 August 2023   
Available online 30 August 2023   
1746-8094/© 2023 Elsevier Ltd. All rights reserved.   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

Therefore, eight ensemble learning approaches, such as random forest  (RF), voting, bagging, adaptive boosting, gradient boosting decision tree  (GBDT), xtreme gradient boosting (XGBoost), light gradient boosting  (LightGBM) and stacking are implemented on two datasets. Those  ensemble learning methods were not implemented in the previous  research papers together in the same paper to detect CKD. The perfor 

mance of the models is evaluated on the two publicly available datasets.  Some measures such as accuracy, precision, recall, F-measure, and AUC ROC are used to assess the performance of each classifier. The following  are the main contributions of this research.  

a) This paper proposed eight machine learning techniques to improve  the efficacy of the existing diagnosis system of CKD healthcare.  Moreover, we have tuned the hyperparameter of each classifier  through the process of parameter tuning to improve the  performance.  

b) This study utilized the MICE imputation method to handle the  missing values instead of the statistical technique. Moreover, the  Borderline-SMOTE technique has been used to balance the unbal anced data. In addition, recursive feature elimination (RFE) and  Boruta methods are implemented to select the relevant features.  Those methods for predicting CKD have not been thoroughly  explored before.  

c) This work performed experiments on two datasets to test and vali date the model performance.  

This paper is arranged as follows: section 2 represents the literature  survey while, section 3 explains the methods and materials. Similarly,  section 4 demonstrates the experimental setup, whereas section 5 rep resents the experimental results and discussion. Finally, section 6 rep resents the conclusion and future work.  

**2\. Literature survey**  

It is evident that a number of CKD patients are increasing, and  diagnostic costs are high compared to other diseases. Moreover, many  developing countries have a deficiency of specialized radiologists.  Therefore, computer-supported diagnostic systems are essential and  previous research has emphasized the use of machine learning (ML) and  deep learning (DL) methods to assist expert physicians in making diag 

nostic decisions in medical health sectors \[5–10\]. However, detecting  and diagnosing CKD using artificial intelligence has become an  

emerging topic in recent years. As a result, numerous research articles  have utilized the ML and DL approaches as excellent automatic methods  based on features to detect and diagnose CKD in the early stages  \[11–13\]. In the study \[14\], support vector machine (SVM), k-nearest  neighbors (KNN), decision tree (DT), and random forest (RF) were used  to build a classification model using 24 features where the data was  collected from 400 patients. Random forest showed the highest classi 

fication accuracy among four classifiers, and it was about 100%. In  addition, to choose the optimal subset of characteristics, the recursive  feature elimination technique was used. Gabriel R *et al.* \[15\] devised an  NN-CBR twin system-based model to diagnose whether a person is at risk  of suffering CKD. In this study, it was identified that, around 7% people  in Colombia are at risk of being CKD. Moreover, SVM and RF algorithms  were applied to compare to the outcome of the NN-CBR system, and the  NN-CBR system obtained an accuracy of 95% in the test dataset. Q. Wing  *et al*. \[16\] proposed several classification algorithms to predict the CKD,  and XGBoost was the best classifier because it achieved accuracy,  sensitivity, and specificity of 100%, 100%, and 100%, respectively.  First, they selected the optimal features using two feature selection  methods: recursive feature elimination (RFE) and extra tree classifier  (ETC). Then the best subset of features was applied on the XGBoost  classifier. Moreover, the model has been tuned to select the optimal  hyperparameter to boost model performance. Grid search technique and  k-fold cross validation were adopted to observe the model performance.  

In the article \[17\], all the experiments used seven ML techniques to  classify CKD as CKD or NOT-CKD. Several evaluation measures such as  mean absolute error (MAE), root mean squared error (RMSE), relative  absolute error (RAE), root relative squared error (RRSE), recall, preci 

sion, F-measure, and accuracy were used to assess the model perfor mance. Overall, the results suggest that CHIRP effectively reduces  mistake classification rates and increases accuracy. The CHIRP achieved  an accuracy of 99.75% when MAE was 0.0025. Alasker et al. \[18\] used  different intelligent techniques like backpropagation neural network,  Naïve Bayes, decision trees, k-nearest neighbor, and one rule classifier to  diagnose kidney illness using a dataset from the UCI ML repository that  were 24 attributes and 400 people. The Naive Bayes method trumps the  other classification algorithms in accuracy and sensitivity. NB obtained  99.36% accuracy and 0.0057 error rate by combining all 24 attributes.  Seven classifier algorithms such as artificial neural network, C5.0, Chi 

square automatic interaction detector, logistic regression, linear sup port vector machine with penalty L1 & with penalty L2, and random tree  were applied to make a classification model of CKD \[19\]. The dataset  

**Fig. 1\.** Risk factors of chronic kidney disease.  

2   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

used in this paper was collected from the University of California.  Moreover, the synthetic minority over-sampling (SMOTE) technique has  been employed to balance the dataset using KNN algorithms. The ex periments were performed based on the feature selection techniques.  The SMOTE technique was used for all features and selected features to  analyze model performance. They achieved an accuracy of 99.6% using  a deep neural network.  

Padmanaban and Parthiban \[20\] proposed that machine learning  classifier methods can diagnose CKD in the initial stage for diabetic  patients. They worked on 600 diabetic patients, and data were collected  from the diabetes research centre at chennai in India. The two most  widely used machine learning algorithms, namely Naïve Bayes and  Decision tree method, were applied to classify the CKD by measuring the  performance metrics. They performed all the experiments using the  Weka tool and observed that the performance of the decision tree al gorithm is better than the Naïve Bayes algorithm, with an accuracy of  91%. The study \[21\] applied DT, RF, and SVM algorithms on the MIMIC 

II database. In this dataset, the medical records were collected and  stored from those patients who were in the intensive care unit of a  medical centre in Israel between 2001 and 2012\. Finally, they concluded  that RF and DT algorithms provide a classification accuracy of 80% and  87%, respectively.  

Sujata Drall et al. \[22\] utilized Naïve Bayes and KNN to detect CKD  and NOTCKD using the UCI machine learning repository dataset with  400 instances and 25 attributes. For their research, they handled the  missing value in the dataset with the help of statistical analysis like  mean and mode. They employed the correlation and dependence strat   
egy to produce highly dependent features for CKD prediction. Finally, it  was shown that the k-nearest neighbor outperformed the Naïve Bayes  for the five features. Sometimes demographic and biochemical blood  features are more significant as compared to the urinary protein quan   
tification for the earlier prediction of CKD during follow-up. In the study  \[23\], they used five demographic and thirteen blood-derived tests from  551 patients to analyze CKD severity using nine classifications algo rithms. They evaluated the AU-ROC, recall, accuracy, log-loss, speci ficity, and precision of each model to observe the model performance.  The linear model provides the highest average AUC and precision above  0.87 and 0.8, respectively. It was also observed that ALB, Scr, TG, LDL,  and EGFR significantly impacted the classification model’s predictabil ity compared to other features. The authors of the study \[24\], focused on  the supervised machine learning model to evaluate CKD as CKD or NOT CKD. Pearson CC, gain ratio and random forest is used to evaluate the  significant features related to CKD. Moreover, data has been balanced  using SMOTE technique. The highest accuracy was obtained using the  rotation forest technique and the accuracy was 99.2%. A study \[25\] used  348 subjects (116 cases and 332 controls) to build the prediction model  of CKD. The authors calculate the risk factors using logistic regression.  Moreover, they implemented a logistic regression model and the natural  logarithm methods to establish the genetic/nongenetic risk prediction  models. the prediction model reached an AUC of 89.4% while the  sensitivity was 82.70%.  

Njoud Abdullah Almansour *et al*. \[26\] employed an artificial neural  network (ANN) and SVM to the UCI machine learning repository dataset  to diagnose CKD. The corresponding attributes’ average value was used  to substitute all missing values in the dataset in their research. More   
over, the valuable parameters of each classifier were chosen using the  parameter tuning method. It was concluded that ANN outperformed  SVM, and both had an accuracy of 99.75% and 97.75%, respectively. S.  B. Akben \[27\] build a predictive model to classify CKD by combining the  findings of urine tests, blood tests, and patient’s medical history. To  perform the experiments, they took preprocessed data and then applied  it to the classification models. The data were preprocessed by using the  K-Means clustering method. An accuracy of 97.8% was obtained using  the proposed approaches. Mohamed Elhoseny et al. \[28\] have proposed  a novel framework called D-ACO algorithm by combining the density based feature selection (DFS) and ant colony based optimization. The  

DFS was used to remove the irrelevant features, and the best subset of  features was applied to the ACO-based classifier. In addition, the per formance of the D-ACO method was evaluated based on various evalu ation metrics using the UCI machine learning repository dataset. The D ACO algorithm achieved a maximum accuracy and F-score of 95% and  96%, respectively. In the study \[29\], the EDL-CDSS method was used in  order to measure the automatic detection and classification of CKD. In  this article, various processes were involved, namely, data collection,  outlier detection, hyperparameter tuning and deep learning-based  classification. The highest average accuracy was 96.71%. In the article  \[30\], they proposed three deep-learning (OANN, OLSTM, OCNN) ap proaches to classify CKD using the UCI machine learning repository’s  chronic kidney disease dataset. The three methods obtained an accuracy  of 98.75%, 96.25% and 97% respectively. They achieved an average  accuracy of 97.33. As stated earlier, this paper used eight ensemble  learning; among them, LightGBM has not been used in the previous  studies. Moreover, the borderline-SMOTE and multiple imputation  techniques have been implemented that were also missing in most past  studies. The related works are summarized in Table 1 to represent the  performance and explore the motivation based on literature survey.  

**3\. Methods and materials**  

This article has developed an intelligent system for CKD analysis and  diagnosis. Eight algorithms are employed in this paper for the analysis of  CKD data. Accuracy, precision, recall, F-measure, and AUC-ROC metrics  were used to asses each model’s performance. Two datasets were ob   
tained from the UCI ML repository website, where one dataset was used  to train and test the algorithms, and another was used to check the  validation of the model’s outcomes. Both the complete set of features  and an optimal subset of features were used in each experiment. Two  feature selection methods, named, Boruta, and Recursive feature elim 

ination, are employed to choose the most relevant features. The steps  that are involved in this research are shown in Fig. 2. The MICE algo rithm and simple imputer are utilized to impute missing values of each  attribute in the dataset. Borderline-SMOTE technique is applied to equal  the target attributes, and finally, the processed data is used as input to  each classifier. The randomized grid search and hyperparameter tuning  technique tune the parameter of each classifier. To validate the model  performance, cross-validation techniques were applied in this paper.  

*3.1. Dataset description*  

In this paper, the analysis of CKD using eight ensemble learning  methods is performed on the publicly available CKD dataset and ob tained from the UCI machine learning repository website \[31\]. More  importantly, several researchers tested their proposed classification  model using the benchmark dataset called the UCI ML repository dataset  to predict CKD \[32–35\]. In this paper, we have named that dataset is UCI  ML Repository CKD-1. The dataset contains 400 occurrences, 250 of  which are CKD and 150 of which are NOTCKD. Twenty-five attributes  are described in this dataset. There are twenty-five attributes, eleven are  of the numeric group, and the rest of them are of the nominal group. One  attribute represents the class of CKD, i.e., CKD and NOTCKD. Table 2  depicts more information about the dataset. Each feature has some  missing values except the class attribute in the dataset, and a question  symbol indicates the missing value. Moreover, the dataset is unbalanced  because it has 62.5% of CKD class (250) and 37.5% of NOTCKD (150)  class in terms of percentage. Another dataset has been collected from  Anam medical college in Dhaka, Bangladesh, after surveying 200 pa tients along with the same number of features \[36\]. In this paper, that  dataset is defined as UCI ML Repository CKD-2.  

*3.2. Data preprocessing*  

Most of the data in the real world need to be preprocessed due to  

3   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

**Table 1**    
Summary of related works.  

Reference Dataset Features Feature selection Validation Classifier Result (%)  

\[30\] University of  California, Irvine    
Machine Learning    
Repository    
24 – – Optimized CNN (OCNN), ANN (OANN),  and LSTM (OLSTM)    
OCNN: 98.75% OANN:  96.25%    
OLSTM: 98.5%  

\[29\] University of  California, Irvine    
Machine Learning    
Repository    
24 – k-fold cross  validation    
deep belief network (DBN), kernel  extreme learning machine (KELM),  convolutional neural network with gated  recurrent unit (CNN-GRU),    
Ensemble of deep learning  based clinical decision  support systems (EDL-CDSS):  Average accuracy: 96.71%.    
\[14\] University of  California, Irvine    
Machine Learning    
Repository    
24 Recursive Feature  Elimination (RFE)    
Training: 75%  Testing and    
Validation: 25%    
Support Vector Machine, K-Nearest  Neighbors, Decision tree, and Random  Forest    
Random Forest:  Accuracy:100%  Precision: 100%  Recall: 100%    
F1-Score: 100%  

\[15\] RIPS database 15 – – Neural Network. Support Vector  Machine, Random Forest    
Neural Network:  Accuracy: 95%  Precision: 94%  Recall: 97%    
F1-Score: 95%  

\[16\] University of  California, Irvine    
Machine Learning    
Repository    
24 Recursive feature  elimination (RFE) and    
extra tree classifier    
(ETC), Univariate    
Selection (US    
K-fold cross  validation  (K \= 10\)    
K-Nearest Neighbour, Logistic    
regression, Linear Discriminant Analysis,  Classification and Regression Tree,  Support Vector Machine and XGBoost    
XGBoost:    
Accuracy: 100%  Precision: 100%  Sensitivity: 100%    
Specificity: 100%  (using RFE)  

\[17\] University of  California, Irvine    
Machine Learning    
Repository    
24 – N-fold cross  validation    
(N \= 10\)    
NBTree, J48, Support Vector Machine,  Logistic Regression, Multi-layer  Perceptron, Naïve Bayes, and Composite  Hypercube on Iterated Random  Projection (CHIRP)    
CHIRP:    
Accuracy: 99.75%  Precision: 99.80%  Recall: 99.80%  F1-Score: 99.80%  

\[18\] University of  California, Irvine    
Machine Learning    
Repository    
24 – – Neural network, Naïve Bayes, Decision  Table, Decision Trees, K-Nearest    
Neighbor, and One Rule    
Naïve Bayes:    
Accuracy: 99.36%  Sensitivity: 97.70%  Specificity: 100%  

\[19\] University of  California, Irvine    
Machine Learning    
Repository    
24 Filter method, Wrapper  method, Embedded    
method    
Training: 50%  Testing: 50%  

Artificial Neural Network, C5.0, Chi square Automatic Interaction Detector,  Logistic Regression, Linear Support  Vector Machine with penalty L1 & with    
LSVM:    
Accuracy: 98.86%  

\[20\] Chennai based  diabetes research    
Centre  

12 – 10-fold cross  validation    
penalty L2, and Random Tree  

Naïve Bayes and Decision tree Decision Tree:  Accuracy: 91.00%  

\[21\] MIMIC-II database 24 – Training: 75%    
Decision Trees, Random Forest, and    
Decision Tree:  

\[22\] University of  

24 Correlation and    
Testing: 25%    
Support Vector Machine    
Accuracy: 87.00%  

California, Irvine  Machine Learning  Repository    
dependence method    
– Naïve Bayes and K-Nearest Neighbor K-nearest Neighbor:  Accuracy: 100%  

\[23\] 551 patients with  proteinuria,    
Department of    
Nephrology, Fudan    
University    
\[26\] University of  California, Irvine    
Machine Learning    
Repository    
18 – 10-fold cross  validation (90% for    
training and 10%    
for testing)  

24 – 10-fold cross  validation (90% for    
training and 10%    
for testing)    
Logistic regression, Elastic Net, Lasso  Regression, Ridge Regression, Support  Vector Machine, Random Forest,  XGBoost, Neural Network and K-Nearest  Neighbor    
Artificial Neural Network and Support  Vector Machine    
Logistic Regression:  Accuracy: 87.30%  

Artificial Neural Network:  Accuracy: 99.75%  

\[27\] University of  California, Irvine    
Machine Learning    
Repository    
24 – – KNN, SVM, and Naïve Bayes Accuracy: 99.75%  

\[28\] University of  California, Irvine    
Machine Learning    
Repository    
24 Density based Feature  Selection (DFS)    
– Ant Colony based Optimization (ACO)  algorithm    
Accuracy: 95.00%  Sensitivity: 96.00%  Specificity: 93.33%  F-score:96.00%  

inconsistency, missing values, noisy characteristics, and outliers.  Otherwise, it is tough to enhance the quality of the machine model, and  as a result, it will give a poor result. In this section, Various processes  have been performed to clean and improve the data.    
(a) Missing value imputation  

The CKD dataset used in this paper is cleaned by filling in missing  values because it had several missing values. Several methods, including  

4   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* **Table 2**  

**Fig. 2\.** Framework of detecting chronic kidney disease.  

UCI ML Repository CKD-1 dataset description with the number of missing values for each attribute.  

**Numerical Attribute**  

S. No Attribute Description Unit of measurement No. of missing value  

1 Age Age Years 9  2 bp Blood Pressure mm/Hg 12  10 bgr blood glucose random mgs/dl 44  11 bu Blood Urea mgs/dl 19  12 sc Serum Creatinine mgs/dl 17  13 sod Sodium mEq/L 87  14 pot Potassium mEq/L 88  15 hemo Hemoglobin gms 52  16 pcv Packed Cell Volume 0,1,2 70  17 wc White Blood Cell Count cells/cumm 105    
18 rc Red Blood Cell Count millions/cmm 130  **Nominal Attribute**    
S. No Attribute Description Values and range No. of missing value  3 sg Specific Gravity 1.005,1.010,1.015,1.020,1.025 47  4 al Albumin 0,1,2,3,4,5 46  5 su Sugar 0,1,2,3,4,5 49  6 rbc Red Blood Cells Normal, Abnormal 152  7 pc Pus Cell Normal, Abnormal 65  8 pcc Pus Cell clumps Present, Not present 40  9 ba Bacteria Present, Not present 4  19 htn Hypertension Yes, No 2  20 dm Diabetes Mellitus Yes, No 2  21 cad Coronary Artery Disease Yes, No 2  22 appet Appetite Good, Poor 1  23 pe Pedal Edema Yes, No 1  24 ane Anemia Yes, No 1  25 class Class Ckd, Notckd 0  

deleting the rows or columns, statistical and ML algorithms-based  imputation methods like mean, median, mode, logistic regression,  KNN, etc., have been employed in the prior studies to deal with the  missing value in the dataset \[37–39\]. Unfortunately, most of the studies  used statistical imputation to impute the value of missing data in the  

dataset due to its simplicity. In this method, the mean, mode, and me dian are calculated for the corresponding observation of missing value  and impute that mean, mode, and median in the respective features.  However, statistical imputation algorithms may generate biased or un realistic conclusions. As a result, this method results in a loss of dataset  

5   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

variation and shows poor performance. In addition, this dataset has 24  features, and some of these are categorical. Therefore, two methods can  be used to impute the missing value for this dataset. Missing values of  categorical features like appetite, pedal edema, anemia, etc., can be  replaced by using a constant value or the statistics (mean, median, or  mode) of the columns in which the missing values are present.  

First of all, this article replaced categorical missing values with  constant values called missing because it can provide a better result than  statistical approaches like mode. Therefore, a new category has been  found for each feature in which the missing value is present. For  instance, hypertension has two categories, namely, yes or no, but when  simple imputer is used with constant, then hypertension has three cat 

egories, namely, yes, no, and missing. Multiple imputations by chain  

equation (MICE) are a sophisticated method for dealing with missing  data sets \[40\]. In this paper, we have applied the MICE algorithm to  impute the missing value of each feature except the categorical features.  The flowchart of the MICE imputation method is shown in Fig. 3. In the  MICE technique, one feature column with missing values is considered  an output, and other feature columns are designated as input. Then the  regression model is used to predict the output data, and this process is  done iteratively. In each iteration, each missing value in the dataset is  imputed using the other value in the dataset, and the iterations process  repeats until convergence is met \[41,42\].  

(b) Data Rescaling  

**Fig. 3\.** Flowchart of the MICE imputation method.  

6   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

**Fig. 4\.** Kernel distribution estimation of each feature in terms of target output.  

7   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

**Fig. 4\.** (*continued*).  

8   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

The values of the whole dataset have been rescaled because the  values of data in the dataset are stored on different scales. Similarly,  ordinal and binary encoding techniques convert categorical data into  ordinal and binary values. In addition, we standardize the dataset to  ensure that each feature has an average zero and standard deviation one.  In addition, the kernel distribution estimation (KDE) is evaluated using  each sample value of each feature for describing the probability density  function \[43\]. Like a histogram, the kernel distribution builds a function  to represent the sample data’s probability distribution. This approach  can easily explain each feature’s range of values responsible for CKD.  Although some CKD and NOTCKD samples overlap each other, it can  visualize the highest information contained in the sample. The KDE of  each feature in terms of target features is shown in Fig. 4.  

*3.3. Feature selection*  

Feature selection is the approach of removing irrelevant features to  abate the computational cost of the machine and enhance the machine  model performance \[44–46\] Therefore, feature selection is desirable for  improving the classifier’s performance and reducing the execution time  of the classifier. As a result, two feature selection techniques are used in  this article.  

(i) **Recursive feature elimination (RFE)**  

The recursive feature elimination method is used to reduce the  number of features as well as choose the optimal subset of features from  the whole dataset. In this technique, relevant features are determined  based on feature importance. Then, it chooses the best N features after  removing the least essential features. \[47\]. The steps involved in the RFE  algorithm are explained in detail below using pseudo-code.  

Pseudo-code for the recursive feature elimination (RFE) method  

**Inputs: **   
Training dataset *T* \= {*t*1*, t*2*,* ⋯⋯*.tm*} with target values *R* ∈ {1*,*⋯*j*}, where *j* is the  number of classes in the dataset    
*r* number of features *F* \= {*f*1*,f*2*,*⋯*..fr*}   
Number of iterations *k*    
Learning method logistic regression (LR)    
**Output:**    
*n* number of optimal feature subsets *F*′ \= {*f*1*,f*2*,*⋯*fn*}   
**Process:**    
1\. Fit random forest (RF) model to dataset T    
for 1: k    
Calculate rank *R* based on the value of co-efficient *C*    
Eliminate specific number of features with the smallest co-efficient  end for    
2\. Return F with n number of features (*F*′ \= *F*)  

(ii) **Boruta based on RF**  

Boruta is such type of feature selection technique that functions as a  wrapper for the random forest. More importantly, Boruta iteratively  removes the statistically less relevant features to the output variable  \[48\]. The steps involved in the Boruta algorithm are explained in detail  below using pseudo-code.  

Pseudo-code for the Boruta based on RF method  

**Inputs: **   
Training dataset *T* \= {*t*1*, t*2*,* ⋯⋯*.tn*} with target values *R* ∈ {1*,*⋯*m*}, where *m* is the  number of classes in the dataset    
*r* number of features *F* \= {*f*1*,f*2*,*⋯*..fr*}   
Number of iterations *k*    
Learning method random forest (RF)    
**Output:**    
*n* number of optimal feature subsets *F*′ \= {*f*1*,f*2*,*⋯*fn*}   
**Process:**    
1\. Create shadow features *S*′(random features and shuffle values in columns)  (*continued on next column*)  

(*continued* )  

Pseudo-code for the Boruta based on RF method  

2\. Calculate new dataset *D* by combining two features (*F and S*′)    
3\. Fit random forest (RF) model to new dataset *D*    
4\. Determine Z score of original features (*Zo*) and shadow features (*Zs*) 5\. Compute maximum Z score (*Zmax*) among shadow features    
6\. if (*Zmax \> Zo*)   
Mark feature as important feature    
else    
Mark feature as un important feature    
7\. repeat the above steps for every iteration or until desired number of features are  reached    
8\. get *n* number of features  

*3.4. Balance dataset*  

It has been observed that the number of classes, i.e., CKD or  NOTCKD, in the dataset is imbalanced. Imbalanced classifications offer  predictive modeling difficulty, resulting in models with poor predictive  performance. Two methods, namely oversampling and under-sampling  techniques, can be used to handle an imbalanced dataset. Many intel 

ligent over-sampling methods have been proposed in the past studies,  with SMOTE being one of the most popular \[49\]. However, another  oversampling technique called borderline-SMOTE performed better  than SMOTE \[50\]. Therefore, in this paper, the borderline-SMOTE  technique is used instead of SMOTE technique. Hien Nguyen et al.  \[51\] have proposed a borderline SMOTE technique in which a SVM is  used instead of KNN to make the minority class instances around the  borderline between the two classes. Borderline-SMOTE SVM study  suggests a way for dealing with them by altering the class distribution of  the data set by oversampling at the data set’s borderline between the  minority and majority classes. Since borderline cases can be mis classified, it is crucial to determine the best decision border. In addition,  SVM attempts to generate new instances toward the region of the ma 

jority class, where the density of the majority class instances is low. It  has been observed that this methodology has outperformed the SMOTE  technique.  

*3.5. Classification models*  

A classifier or classification model plays a crucial role in predicting  various diseases using the patient’s history. The classifier is first trained  from training data and then tested to classify the corresponding target  variables. In this paper, eight classification algorithms were applied to  distinguish the patient’s state of CKD as CKD or NOTCKD.  

(a) Random forest (RF)  

Random Forest creates a large number of decision trees, each of  which is trained on a random subset of the training data and a random  subset of the available features. The output of the Random Forest is then  determined by averaging the outputs of all the individual decision trees.  It is nothing but an ensemble learning technique first introduced by  Breiman \[52\]. It checks out and removes the overfitting problem by  averaging the outcomes of various decision trees.  

(b) Voting  

Majority voting is a common and widely known method of the eight  ensemble methods. In a voting system, each model in the ensemble is  trained independently on a subset of the training data or using a  different algorithm or combination of hyperparameter. The prediction is  then displayed by updating the classifier weights after taking into ac 

count the classifier’s majority of votes \[53\]. This study analyses the  majority voting ensemble using the support vector machine (SVM) and  k-nearest neighbour (KNN) categorization methods.  

9   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

(c) Bagging  

Leo Breiman introduced this approach as bagging predictors in 1994  \[54\]. Bagging, short for Bootstrap Aggregating, is a machine learning  technique for ensemble learning. In bagging, each model in the  ensemble is trained on a randomly selected subset of the training data,  with replacement. It takes advantage of bootstrap sampling to create  data subsets for training each base classifier individually. Some data  points from the initial training set may be repeated in each bootstrap  sample. The most popular class is finalized after the algorithm has been  trained on all bootstrap samples.  

(d) Adaptive boosting (AdaBoost)  

The AdaBoost algorithm, also known as adaptive boosting, is an  ensemble technique that combines several weak classifiers into one  robust classifier. This approach was proposed by Freund and Schapire, in  which decision tree stumps are employed successively as a weak algo   
rithm, and the succeeding algorithms correct the incorrectly anticipated  output produced by the preceding learners \[55\]. Each sample’s weight is  assigned throughout each phase of the training period to carry out this  process. In order to upgrade the perfection of the following learners,  AdaBoost traditionally concentrates on the misclassification error. The  records are picked to streamline the weight of training samples for the  following classifier. It chooses a learner that classes data with a small  amount of error rate throughout the training stage.  

(e) Gradient boosting decision tree (GBDT)  

This technique combines many weak learners to create strong  learners for classification and regression applications. Using an iterative  procedure, decision trees are sequentially added in this method to  reduce the errors of the earlier trees, and in order to produce a strong  learner, trees are finally combined \[56\]. This technique combines many  weak learners to create strong learners for classification and regression  applications. Using an iterative procedure, decision trees are sequen 

tially added in this method to reduce the errors of the earlier trees, and  in order to produce a strong learner, trees are finally combined. When  integrating new models, it does employ a gradient descent strategy to  reduce loss.  

(f) Extreme gradient boosting (XGBoost)  

Extreme gradient boosting (XGBoost) works on the basis of a  gradient boosting technique where the computation time is lesser than  the gradient boosting \[57\]. Moreover, XGBoost uses regularization  terms; therefore, its performance is much better than the gradient  boosting method. In addition, XGBoost has an ability to handle the  missing values automatically and carry out bigger large data than the  memory size. Besides, it can work on parallel operations using column  sub-samples techniques \[58\].  

(g) Light gradient boosting (LightGBM)  

In 2017, Ke. G et al. introduced another concept of gradient-boosting  decision tree algorithm named, LightGBM, where gradient-based one side sampling (GOSS) and exclusive feature bundling (EFB) work  together \[59\]. Gradient-based One-Side Sampling (GOSS) to perform  gradient-based subsampling of the training data, which reduces over fitting and speeds up the training process. More importantly, It uses a  leaf-wise growth strategy to build the decision trees, which reduces the  number of tree nodes and improves the efficiency of the algorithm. As a  result, LIghtGBM takes less time to execute the operation as compared to  the execution time of others ensemble methods.  

(h) Stacking  

Stacking is an ensemble strategy where classification and regression  operation performs in two stages \[60\]. In the first step, classifiers are  trained on the training data and predict output as the input of the next  classifier. In the final stage, all predicted outputs are considered as the  input of the new classifier and evaluate the final output.  

**4\. Experiment environment setup**  

In this section, the proposed models are executed in Phyton software  using Windows 10 operating system to validate. The system operates  with 8 GB ram and Intel core i3 at the clock frequency of 2.40GGHz.  Moreover, the following section has been included splitting the dataset  as training and test data, tunning each classifier’s parameters using  randomized grid search technique, and evaluating metrics to validate  the model performance.  

*4.1. Splitting the dataset*  

In each experiment, we fixed up 10% of the total data as test data and  the rest of the 90% data as training data. To train the model precisely,  the shuffle-split cross-validation method was used, and furthermore,  90% of the prior training data was divided into five sub-sections. Each  sub-section is set up in such a way that it is contained a training set of  90% and a validation set of 10%.  

*4.2. Parameter tunning*  

Setting up hyperparameters of each algorithm based on various  dataset allow us to make the algorithms efficient, adjustable and effec tive. However, tuning the hyperparameter for every model is optional at  all times. Furthermore, the performance of the majority classifier relies  on the hyperparameters, and it can provide better solutions and results  when someone chooses effective parameters for different applications.  The model with all parameters will become complex and will make al gorithms slow. As a result, to get the optimized model, searching a small  group of hyperparameters for each algorithm is important. In this paper,  important hyperparameters of each classifier have been tuned using a  randomized search cross-validation approach which is better than the  normal grid search technique \[61\]. Furthermore, the CKD prediction  was observed with the best subset of the hyperparameter for each  classifier. Table 3 provides details on each classifier’s major hyper parameters for binary classification.  

*4.3. Model evaluation metric*  

Various performance evaluation metrics can evaluate the quality of a  model’s predictions. More importantly, accuracy, precision, recall, F measure, AUC-ROC, and confusion matrix are the most used perfor mance evaluation metrics for binary classification. The evaluation  metrics as mentioned above are described below.  

(a) Confusion matrix  

A confusion matrix is a method for describing the performance of a  classification model. Each row represents an actual class of the target  variable, and each column represents a predicted class of the target  variable (see Table 4).  

(b) Accuracy  

In machine learning, accuracy is a statistic used to determine how  much of a given class is predicted correctly out of the total number of  samples and calculated by equation (i)  

*Accuracy* \= *TP* \+ *TN*   
*TP* \+ *TN* \+ *FP* \+ *FN* (1)  

10   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

**Table 3**    
Parameter setting of each classifier for binary classification using randomized  grid search technique.  

Algorithm Hyperparameter Range and Name  

**Table 4**    
Confusion matrix for binary decision values.  

**Predicted value Observation**  

**CKD NOTCKD**    
Random forest n\_estimators: number of trees 50, 60, 70, 80, 90, 100,  150,  

**Actual  Value**    
**CKD**    
**(Positive)**  

**True Positive  (TP)**    
**False Negative  (FN)**  

Total number of  actual CKDs  

max\_features: number of features for  the best split.    
200, 250, 300, 400  auto  

Actual: CKD  Model    
Actual: CKD  Model  

**bootstrap** True, False    
predicted as    
predicted as  

**min\_samples\_split**: minimum number  of samples to split an internal node.  **min\_samples\_leaf**: minimum number  of samples required to be at a leaf node  **max\_depth**: maximum depth of the  tree  

2–8  

1–5  

None  

**NOTCKD  (Negative)**    
CKD    
**False Positive  (FP)**    
Actual:    
NOTCKD    
Model    
NOTCKD    
**True Negative  (TN)**    
Actual:    
NOTCKD    
Model  

Total number of  actual NOTCKDs  

Voting base\_estimator: list of classifiers Support vector  machine and k-nearest    
neighbor    
**voting** soft    
Bagging base\_estimator: list of classifiers Decision tree    
predicted as    
CKD    
**Observation** Total number of  positive    
predictions    
predicted as  NOTCKD    
Total number of  negative    
predictions  

5, 10, 15, 20  

Adaptive    
n\_estimators: number of base  estimators    
base\_estimator: classifier Decision tree  

*Recall* \= *TP*   
boosting  

Gradient  boosting  

Extreme  gradient  boosting    
n\_estimators: maximum number of  estimators    
learning rate: how slowly or fast  classifier update its last value.  n\_estimators: number of boosting  states    
max\_depth: maximum depth of the tree  of each classifier    
**min\_samples\_leaf**: minimum number  of samples required to split an internal  node    
learning rate: how slowly or fast  classifier update its last value.  **n\_estimators**: maximum number of  estimators    
**max\_depth**: maximum depth of the  tree  

50, 60,70, 80, 100  

0.0001, 0.001, 0.01,  0.1, 1    
100–500  

2–8  

4, 8, 10, 16, 20  

0.01, 0.05, 0.1  

100–700  

2–10    
*TP* \+ *FN* (3)  

(e) F-measure  

The F-measure is calculated using the combination of precision and  recall. Mathematically, the F1 score is the weighted average of precision  and recall. The F-measure is expressed by equation (iv).  

*F* − *Measure* \= 2\* *Precision*\**Recall*   
*Precision* \+ *Recall* (4)  

(f) AUC-ROC  

The graph of True Positive Rate (TPR) vs. False Positive Rate (FPR) is    
**min\_child\_weight** 1–9  

known as the Receiver Operating Characteristic (ROC) curve (FPR). It    
**learning\_rate**: how slowly or fast    
classifier update its last value.    
LightGBM **n\_estimators**: maximum number of  estimators    
**max\_depth**: maximum depth of the    
tree    
0.05, 0.1, 0.15, 0.2,  0.25    
100–500  

2–10    
demonstrates the performance ability of a classification model. The area  under the ROC curve is known as the area under the curve (AUC). AUC ROC metric represents the ability of a classification model based on  threshold values. The higher the AUC, the better the model.  

**min\_child\_weight** 1–9 (odd value)    
**learning rate**: how slowly or fast    
classifier update its last value.    
Stacking estimators: Base estimators which will  be stacked together  

final\_estimator: A classifier which will    
be used to combine the base    
estimators.  

(c) Precision    
0.05, 0.1  

Support vector    
machine and k-nearest  neighbor    
Quadratic discriminant  analysis    
**5\. Experimental results and discussion**  

In this section, the output of each classifier has been estimated using  various assessment metrics like accuracy, precision, recall, F-measure,  and AUC-ROC. The tests were carried out utilizing Python 3.2 pro gramming language through the Jupyter Notebook. Furthermore,  another dataset has been used to validate the findings of each classifier.  In addition, this paper implemented two feature selection techniques to  select the important features related to the assessment of CKD.  

It is defined as the number of accurately predicted positive cases (TP)  to all the predicted positive cases (TP \+ FP). It can be calculated using  equation (ii).  

*Precision* \= *TP*   
*TP* \+ *FP* (2)  

(d) Recall  

It is defined as the ratio of the correctly identified positive cases (TP)  to all the actual positive cases (TP \+ FN). The following equation is used  to calculate the recall.    
*5.1. Without features selection method*  

The bar graph (Fig. 5) and Table 5 represents the experimental re sults of each classification model using all features of the given dataset.  It is clear from the graph that, in the case of five performance metrics,  voting and stacking algorithms reached a 100% score. However, bagging  and GBDT showed slightly under 6% less performance than other  methods. In the case of precision, apart from voting and stacking, the  adaptive classifier reached a high of 100%. Moreover, LightGBM, RF,  Bagging, and XGBoost classifiers performed better; their scores were  greater than approximately 96%. For example, In addition, LightGBM  scored 99% accuracy, 98.21% precision, 100% recall, 99.09% F-mea 

sure and 98.88% AUC-ROC. Similarly, another method GBDT achieved  97% accuracy, 96.42% precision, 98.81% recall, 97.29% F-measure and  

11   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

**Fig. 5\.** Comparison of performance metrics of all classifiers using UCI ML Repository CKD-1 dataset and all features.  

**Table 5**    
Performance comparison (%) of all ensemble methods using all features**.**  

Classifier Validation accuracy    
(mean ± std dev.) Accuracy Precision Recall F-measure AUC-ROC Time (sec)  

RF 99.50 \+ 1.00 98 98.18 98.18 98.18 97.97 2.411  Voting 100.00 ± 00 100 100 100 100 100 5.336  Bagging 98.50 ± 1.22 97 96.42 98.18 97.29 96.86 2.473  AdaBoost 98.50 ± 1.22 99 100 98.18 99.08 99.09 0.040  GBDT 99.00 ± 1.22 97 96.42 98.18 97.29 96.86 5.043  XGBoost 99.00 ± 1.22 99 98.21 100 99.09 98.86 0.449  LightGBM 9.50 ± 1.00 99 98.21 100 99.09 98.88 0.119  Stacking 100.00 ± 00 100 100 100 100 100 2.546  

96.86% AUC-ROC. Moreover, it is noted that LightGBM performed fast  than the other two methods, while all the methods showed the same  performance (see Fig. 5).  

*5.2. Recursive feature elimination method*  

The findings that are shown in Table 6 and Fig. 6 illustrate the per centage of performance metrics of each classifier. It also depicts the  increased rate of performance metrics due to the selection of a minimal  number of subsets of CKD features. In this experiment, of the 24 features,  the twelve most important features (sg, al, su, bgr, sc, hemo, pcv, rbcc,  rbc, htn, dm, appet) were selected for finding CKD. It is observed that RF,  voting, GBDT, XGBoost, LightGBM, and stacking achieved 100% accu racy, 100% precision, 100% recall, 100% F-measure and 100% AUC ROC with 50% fewer attributes. However, the Bagging and Ada classi fiers scored greater than 98% in all cases of performance metrics which  is 2% less compared to others classifiers. For instance, bagging scored  98% accuracy, 98% precision, 97.80% recall, 98.68% F-measure, and  98.97% AUC-ROC. Similarly, bagging obtained 100% accuracy, 97.18%  precision, 97.48% recall, 98.18% F-measure, and 97.57% AUC-ROC.  

**Table 6**    
Performance comparison (%) of all ensemble methods using REF technique.  Classifier Validation accuracy    
*5.3. Boruta based on RF method*  

In the Boruta feature selection technique, 20 attributes (age, bp, sg,  al, su, bgr, bu, sc, sod, pot, hemo, pcv, wbcc, rbcc, rbc, pc, htn, dm,  appet, pe) are considered important among 24 attributes. Therefore, if it  is compared to REF feature elimination methods, it is seen that Boruta  selected about 84% of features of all the features, which is almost 34%  more than the REF method. The bar chart (Fig. 7) and Table 7 shows the  information on the percentage of performance metrics of each classifier  using the boruta feature elimination technique. It is observed that RF,  Bagging, and LightGBM outperformed the other algorithms, and they  achieved 100% accuracy,100% precision, 100% recall, 100% F-measure  and 100% AUC-.  

ROC. However, Adaptive boosting (Ada) performed quite less than  other methods, and it scored almost less than 5% compared to other  algorithms. In addition, another method named voting scored 98.87%  accuracy, 98.07% precision, 100% recall, 99.02% F-measure and  98.68% AUC-ROC, which are slightly less than 98% on average  compared to other algorithms.  

(mean ± std dev.) Accuracy Precision Recall F-measure AUC-ROC Time (sec)  

RF 99.50 ± 1.00 100 100 100 100 100 0.609  Voting 100.00 ± 0.00 100 100 100 100 100 0.628  Bagging 99.50 ± 1.00 98 98 97.80 98.69 98.97 4.012  AdaBoost 99.00 ± 2.00 100 97.18 97.48 98.18 97.57 0.029  GBDT 98.50 ± 2.00 100 100 100 100 100 3.782  XGBoost 98.50 ± 2.00 100 100 100 100 100 0.707  LightGBM 98.50 ± 2.00 100 100 100 100 100 0.116  Stacking 100.00 ± 0.00 100 100 100 100 100 0.725  

12   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

**Fig. 6\.** Comparison of performance metrics of all classifiers using UCI ML Repository CKD-1and RFE feature selection technique.  

**Fig. 7\.** Comparison of performance metrics of all classifiers using UCI ML Repository CKD-1 and Boruta feature selection technique.  

**Table 7**    
Performance comparison (%) of all three ensemble methods using boruta technique.  

Classifier Validation accuracy    
(mean ± std dev.) Accuracy Precision Recall F-measure AUC-ROC Time (sec)  

RF 100.00 ± 0.00 100 100 100 100 100 0.463  Voting 100.00 ± 0.00 98.87 98.07 100 99.02 98.68 0.535  Bagging 100.00 ± 0.00 100 100 100 100 100 4.048  AdaBoost 98.89 ± 2.22 95.55 96 96 96 95.50 0.018  GBDT 100.00 ± 0.00 100 100 100 100 100 1.543  XGBoost 100.00 ± 0.00 98.88 98.03 100 99 98.74 0.368  LightGBM 100.00 ± 0.00 100 100 100 100 100 0.133  Stacking 100.00 ± 0.00 98.87 98.07 100 99.02 98.68 0.740  

*5.4. Validate algorithm’s performance*  

We used eight ensemble methods with optimal groups of features  using the UCI dataset. Although all the algorithms performed satisfac torily, the machine learning model’s performance depends on the  dataset. Therefore, another dataset is used to validate the model per formance. The data has been collected from Anam medical college at  Dhaka in Bangladesh after surveying 200 patients \[36\]. In this paper,  that dataset is defined as UCI ML Repository CKD-2. Same methodolo gies like imbalance data handling technique, data imputation, feature  scaling, etc., have been used to validate the machine learning model.    
Nine essential features such as sg, bgr, sc, hemo, pcv, rbcc, rbc, htn, dm  were used, and it was observed that stacking and adaptive classifiers  outperformed other algorithms with an accuracy of 100%. It is clear  from the graph all the algorithms showed satisfactory performance  while using another dataset collected from another country. Moreover,  each algorithm achieved a 100% recall score (see Fig. 8 and Table 8). It  means that both algorithms correctly predicted all the positive cases,  which is essential for health science. In addition, each algorithm showed  an average of 98.31% accuracy, 97.23% precision, 100% recall, 98.58F measure and 98.01 AUC-ROC.  

13   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* **Table 8**    
**Fig. 8\.** Comparison of performance metrics of all classifiers using UCI ML Repository CKD-2.  

Performance comparison (%) of all ensemble methods using UCI ML Repository CKD-2.  

Classifier Validation accuracy    
(mean ± std dev.) Accuracy Precision Recall F-measure AUC-ROC Time (sec)  

RF 97.14 ± 2.33 96.15 93.75 100 96.77 95.45 0.659  Voting 100.00 ± 0.00 100 100 100 100 100 0.725  Bagging 98.10 ± 2.33 98.07 96.77 100 98.36 97.72 1.962  AdaBoost 97.14 ± 2.33 100 100 100 100 100 3.170  GBDT 98.10 ± 2.33 98.07 96.77 100 98.36 97.72 0.319  XGBoost 97.14 ± 2.33 96.15 93.75 100 96.77 95.45 0.610  LightGBM 97.14 ± 2.33 98.07 96.77 100 98.36 97.72 0.050  Stacking 99.05 ± 1.90 100 100 100 100 100 0.687  

**Fig. 9\.** Computation time of each algorithm in second.  

*5.5. Computational time*  

The bar chart (see Fig. 9) compares the amount of time spent by each  algorithm while executing the performance. It is interesting to note that  adaptive boosting, GBDT, and bagging algorithms take longer than  others. The average time taken by these algorithms was 3.12 s, 2.67 s  and 2.34 s, respectively. On the contrary, XGBoost and LightGBM took  less time in comparison with all algorithms. The average execution time  of XGBoost and LightGBM were 0.53 s and 0.10 s, respectively. How 

ever, it is clear from the graph, LightGBM is faster than all other  algorithms.  

*5.6. Comparative analysis of recent works*  

Table 9 depicts the comparison of various recent works with our    
proposed method based on the average accuracy. This table shows that  each of the studies applied different classification algorithms to detect  CKD using the UCI ML repository CKD-1 dataset. In contrast, we applied  eight ensemble learning approaches, including LightGBM. Moreover,  borderline SMOTE and MICE algorithms have been employed to handle  the imbalanced data and impute the missing values. In the study, N. A.  Almansour et al. achieved an average accuracy of 98.75% using two  machine learning algorithms. They did not use any data balancing  technique. Their accuracy is less as compared to our accuracy (99.75%).  Similarly, another study achieved an average accuracy of 97.71% which  is 2.04% less than our proposed method’s accuracy. The other three  studies achieved an average accuracy of 94.12%, 91.14%, 95%, and  97.76%%, respectively, which is 5.63%, 8.61% and 4.98% smaller in  comparison with our accuracy.  

Moreover, study Alsuhibany et al. and C. Mondal et al. various used  

14   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

**Table 9**    
Comparative study with recent works.  

Author Data source Missing value  imputation    
Handling  imbalance  data  

Algorithm Validation Experimental  Environment    
Average  accuracy  (%)  

N. A.    
Almansour  *et al.* \[26\]  

B. Khan *et al*.    
UCI ML    
Repository  dataset CKD-1  

UCI ML    
Mean – SVM, ANN K-fold Cross  Validation (k    
\= 10\)    
Training set:    
90%    
Test set: 10%    
Waikato Environment  for Knowledge    
Analysis (WEKA)    
98.75  

\[17\]  

P. Chittora  *et al.*\[19\]  

S. Akter *et al.*    
Repository    
dataset CKD-1  

UCI ML    
Repository    
dataset CKD-1  The Cancer    
Imaging Archive  (TCIA)    
Mean – J48, SVM, MLP, NBT, LR, NB, CHIRP N-fold Cross  Validation (k    
\= 10\)    
Training set:    
90%    
Test set: 10%    
– SMOTE ANN, C5.0, LR, CHAID, LSVM, KNN, RT Training set:  50%    
Test set: 50%    
– 97.71  

IBM SPSS 94.12  91.57  

\[4\]    
UCI ML    
Repository  dataset CKD-1    
Multiple    
imputations  method    
– ANN, LSTM, GRU based on RNN,  Bidirectional LSTM, Bidirectional GRU,    
MLP, RNN, AdaBoost, RF    
K-fold Cross  Validation (k  \= 10\)    
Training set:  90%    
– 91.14  

M. Elhoseny  *et al.* \[28\]  

Dritsas et. Al.    
UCI ML    
Repository  dataset CKD-1  

UCI ML  

– – Ant Colony based Optimization (D-ACO)  algorithm  

– SMOTE BayesNet, NB, SVM, LR, ANN, k-NN,    
Test set: 10%  K-fold Cross  Validation (k  \= 10\)    
Training set:  90%    
Test set: 10%  

MATLAB R2014a 95.00  

\[24\]  

Alsuhibany    
Repository  dataset CKD-1  UCI ML  

J48, LMT, RF, RT, DT (RepTree), RotF,    
AdaBoostM1, SGD, Stacking, Soft Voting    
Data Mining ADASYN deep belief network (DBN), kernel    
– Waikato Environment  for Knowledge  

Analysis (WEKA)    
97.76  

et al., 2021    
Repository  dataset CKD-1  

extreme learning machine (KELM),  convolutional neural network with gated  recurrent unit (CNN-GRU)    
– Python 3.6.5 96.91  

C. Mondal et al.  \[30\]  

**Proposed**    
UCI ML    
Repository  dataset CKD-1    
Numerous  imputations  method    
– Optimized CNN  Optimized ANN    
Optimized LSTM    
Training set:  80%    
Test set: 20%    
– 97.33  

**Approach**    
UCI ML    
Repository  dataset CKD-1  UCI ML    
Repository  dataset CKD-2    
MICE    
algorithm    
Borderline  SMOTE with  SVM    
Ensemble learning method Shuffle-split  cross   
validation    
Training set:    
90%    
Test set: 10%    
Python 3.3 99.75  98.31  

deep learning algorithms with an accuracy of 96.91% and 97.33%,  which is 3.14% and 2.42% less than our result. Therefore, it is proven  that our proposed method can increase the prediction rate of CKD as    
CKD or NOT-CKD. A comparative study of the accuracy (%) of the  proposed method with other studies dealing with the same dataset has  been depicted in Fig. 10. It was observed that our proposed algorithms  

**Fig. 10\.** Comparison of accuracy (%) of the proposed method with other studies dealing with the same dataset and other methods.  

15   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

outperformed different algorithms dealing with the same dataset.  Moreover, in the same figure, it has been shown how much our proposed  method enhanced the accuracy rate compared to other existing ap proaches. In Fig. 10 the enhanced accuracy rate is marked by deep red  color.  

**6\. Conclusion and future work**  

In this paper, we effectively developed an ensemble learning-based  technique for the detection of chronic kidney disease (CKD) so that  CKD patients can take medicine and recovery treatment before going to  the final stage. Physicians may utilize this prediction method as an  effective alternative method because of its high level of accuracy. It can  be utilized by regular individuals to estimate their risk of developing  CKD using their medical report. Additionally, the shortest compilation  time for the categorization of CKD is required by this method. In this  case, two datasets were used, the first one contains 400 patients with 24  attributes, and the second one has 200 patients containing 9 attributes.  The first dataset was collected from Irvine Machine Learning Repository  (UCI ML Repository CKD-1) and used to train and test the machine  learning model. Similarly, the second dataset (UCI ML Repository CKD 2\) was used to validate the model’s performance. Eight ensemble  learning methods were used to classify CKD as CKD or NOT-CKD, where  important parameters were selected by tuning the hyperparameters to  increase the model’s performance. Among eight algorithms, LightGBM  performed faster than other methods. In addition, MICE imputation and  borderline SVMSMOTE techniques were used to handle the missing  value and imbalanced data. Furthermore, two feature selection tech niques have been applied; among these, the RFE method reduced 50% of  the total features and achieved an average of 99.75% accuracy, 99.40%  precision, 99.41% recall, 99.61% F-measure, and 99.57% AUC-ROC.  Experiments show that our proposed method can identify CKD more  precisely than the most recent methods. In future work, we intend to use  deep learning technique to identify the stage of this disease. Moreover,  our proposed method can be used to classify the patients as acute kidney  injury (AKI), CKD, and healthy. Furthermore, we will use other datasets  to check out the reliability of our suggested methods.  

**Data availability**  

Datasets are available at: http://archive.ics.uci.edu/ml and the  source code of the proposed methods are available at: https://github.  com/mustafizur88/Kidney.  

**CRediT authorship contribution statement**  

**Md. Mustafizur Rahman:** Conceptualization, Methodology, Soft ware, Writing – original draft, Data curation, Validation, Investigation,  Resources. **Md. Al-Amin:** Writing – review & editing, Visualization.  **Jahangir Hossain:** Project administration, Formal analysis, Investiga tion, Writing – review & editing.  

**Declaration of Competing Interest**  

The authors declare that they have no known competing financial  interests or personal relationships that could have appeared to influence  the work reported in this paper.  

**References**  

\[1\] R. Ruiz-Arenas, et al., A Summary of Worldwide National Activities in Chronic  Kidney Disease (CKD) Testing, EJIFCC 28 (4) (Dec. 2017\) 302\. Accessed: Jan. 13,  2022\. \[Online\]. Available: /pmc/articles/PMC5746839/.    
\[2\] A. Nishanth, T. Thiruvaran, Identifying Important Attributes for Early Detection of  Chronic Kidney Disease, IEEE Rev. Biomed. Eng. 11 (Dec. 2018\) 208–216, https://  doi.org/10.1109/RBME.2017.2787480.  

\[3\] W.M. McClellan, Epidemiology and risk factors for chronic kidney disease, Med.  Clin. North Am. 89 (3) (2005) 419–445, https://doi.org/10.1016/J.  MCNA.2004.11.006.    
\[4\] S. Akter, et al., Comprehensive Performance Assessment of Deep Learning Models  in Early Prediction and Risk Identification of Chronic Kidney Disease, IEEE Access  9 (2021) 165184–165206, https://doi.org/10.1109/ACCESS.2021.3129491.    
\[5\] A. Sharma, P.K. Mishra, Performance analysis of machine learning based optimized  feature selection approaches for breast cancer diagnosis, Int. J. Inf. Technol. 14 (4)  (Aug. 2021\) 1949–1960, https://doi.org/10.1007/S41870-021-00671-5.    
\[6\] M. Imran, U. Zaman, Imran, J. Imtiaz, M. Fayaz, J. Gwak, Comprehensive Survey of  IoT, Machine Learning, and Blockchain for Health Care Applications: A Topical  Assessment for Pandemic Preparedness, Challenges, and Solutions, Electron 10  (20) (2021) 2501, https://doi.org/10.3390/ELECTRONICS10202501.    
\[7\] P. Rani, R. Kumar, A. Jain, Multistage model for accurate prediction of missing  values using imputation methods in heart disease dataset, Lect. Notes Data Eng.  Commun. Technol. 59 (2021) 637–653, https://doi.org/10.1007/978-981-15-  9651-3\_53/COVER/.    
\[8\] A.M. Rahmani, et al., Machine Learning (ML) in Medicine: Review, Applications,  and Challenges, Math. 9 (22) (2021) 2970, https://doi.org/10.3390/  MATH9222970.    
\[9\] X. Pan, Y. Wang, K.S. Chin, Dynamic programming algorithm-based picture fuzzy  clustering approach and its application to the large-scale group decision-making  problem, Comput. Ind. Eng. 157 (Jul. 2021), 107330, https://doi.org/10.1016/J.  CIE.2021.107330.    
\[10\] I.D. Borlea, R.E. Precup, A.B. Borlea, D. Iercan, A Unified Form of Fuzzy C-Means  and K-Means algorithms and its Partitional Implementation, Knowledge-Based  Syst. 214 (Feb. 2021), 106731, https://doi.org/10.1016/J.KNOSYS.2020.106731.    
\[11\] J. Qin, L. Chen, Y. Liu, C. Liu, C. Feng, B. Chen, A machine learning methodology  for diagnosing chronic kidney disease, IEEE Access 8 (2020) 20991–21002,  https://doi.org/10.1109/ACCESS.2019.2963053.    
\[12\] V. Singh, V.K. Asari, R. Rajasekaran, A Deep Neural Network for Early Detection  and Prediction of Chronic Kidney Disease, Diagnostics 12 (1) (2022) 116, https://  doi.org/10.3390/DIAGNOSTICS12010116.    
\[13\] S.I. Ali, et al., Ensemble Feature Ranking for Cost-Based Non-Overlapping Groups:  A Case Study of Chronic Kidney Disease Diagnosis in Developing Countries, IEEE  Access 8 (2020) 215623–215648, https://doi.org/10.1109/    
ACCESS.2020.3040650.    
\[14\] E.M. Senan, et al., Diagnosis of Chronic Kidney Disease Using Effective  Classification Algorithms and Recursive Feature Elimination Techniques,  J. Healthc. Eng. 2021 (2021), https://doi.org/10.1155/2021/1004767.    
\[15\] G.R. Vasquez-Morales, S.M. Martinez-Monterrubio, P. Moreno-Ger, J.A. Recio Garcia, Explainable Prediction of Chronic Renal Disease in the Colombian  Population Using Neural Networks and Case-Based Reasoning, IEEE Access 7  (2019) 152900–152910, https://doi.org/10.1109/ACCESS.2019.2948430.    
\[16\] A. Ogunleye, Q.G. Wang, XGBoost Model for Chronic Kidney Disease Diagnosis,  IEEE/ACM Trans. Comput. Biol. Bioinforma. 17 (6) (2020) 2131–2140, https://  doi.org/10.1109/TCBB.2019.2911071.    
\[17\] B. Khan, R. Naseem, F. Muhammad, G. Abbas, S. Kim, An empirical evaluation of  machine learning techniques for chronic kidney disease prophecy, IEEE Access 8  (2020) 55012–55022, https://doi.org/10.1109/ACCESS.2020.2981689.    
\[18\] H. Alasker, S. Alharkan, W. Alharkan, A. Zaki, L. S. Riza, “Detection of kidney  disease using various intelligent classifiers,” *Proceeding \- 2017 3rd Int. Conf. Sci. Inf.  Technol. Theory Appl. IT Educ. Ind. Soc. Big Data Era, ICSITech 2017*, vol. 2018-  Janua, pp. 681–684, 2017, doi: 10.1109/ICSITech.2017.8257199.    
\[19\] P. Chittora, et al., Prediction of Chronic Kidney Disease \- A Machine Learning  Perspective, IEEE Access 9 (2021) 17312–17334, https://doi.org/10.1109/  ACCESS.2021.3053763.    
\[20\] K.R. Anantha Padmanaban, G. Parthiban, Applying machine learning techniques  for predicting the risk of chronic kidney disease, Indian J. Sci. Technol. 9 (29) (May  2016\) 1–5, https://doi.org/10.17485/ijst/2016/v9i29/93880.    
\[21\] K. L. De Almeida *et al.*, “Kidney Failure Detection Using Machine Learning  Techniques,” pp. 1–8, 2020, \[Online\]. Available: https://hal.archives-ouvertes.fr  /hal-02495264.    
\[22\] S. Drall, G. Singh Drall, S. Singh, B. B. Naib, and A. Prof, “Chronic Kidney Disease  Prediction Using Machine Learning: A New Approach,” vol. 8, no. 278, pp.  278–287\.    
\[23\] J. Xiao, et al., Comparison and development of machine learning tools in the  prediction of chronic kidney disease progression, J. Transl. Med. 17 (1) (Apr. 2019\)  1–13, https://doi.org/10.1186/S12967-019-1860-0/FIGURES/5.    
\[24\] E. Dritsas and M. Trigka, “Machine Learning Techniques for Chronic Kidney  Disease Risk Prediction,” *Big Data Cogn. Comput. 2022, Vol. 6, Page 98*, vol. 6, no. 3,  p. 98, Sep. 2022, doi: 10.3390/BDCC6030098.    
\[25\] J. Zhao, et al., An early prediction model for chronic kidney disease, Sci. Rep. 12  (1) (2022) 1–9, https://doi.org/10.1038/s41598-022-06665-y.    
\[26\] N. A. Almansour *et al.*, “Neural network and support vector machine for the  prediction of chronic kidney disease: A comparative study,” *Comput. Biol. Med.*, vol.  109, no. October 2018, pp. 101–111, 2019, doi: 10.1016/j.    
compbiomed.2019.04.017.    
\[27\] S.B. Akben, Early Stage Chronic Kidney Disease Diagnosis by Applying Data Mining  Methods to Urinalysis, Blood Analysis and Disease History, IRBM 39 (5) (Nov.  2018\) 353–358, https://doi.org/10.1016/J.IRBM.2018.09.004.    
\[28\] M. Elhoseny, K. Shankar, J. Uthayakumar, Intelligent Diagnostic Prediction and  Classification System for Chronic Kidney Disease, Sci. Rep. 9 (1) (2019) 1–14,  https://doi.org/10.1038/s41598-019-46074-2.    
\[29\] S.A. Alsuhibany, et al., Ensemble of Deep Learning Based Clinical Decision Support  System for Chronic Kidney Disease Diagnosis in Medical Internet of Things  

16   
*Biomedical Signal Processing and Control 87 (2024) 105368*   
*Md. Mustafizur Rahman et al.* 

Environment, Comput. Intell. Neurosci. 2021 (2021), https://doi.org/10.1155/  2021/4931450.    
\[30\] C. Mondol, et al., Early Prediction of Chronic Kidney Disease: A Comprehensive  Performance Analysis of Deep Learning Models, Algorithms 15 (9) (Sep. 2022\) 308,  https://doi.org/10.3390/A15090308/S1.    
\[31\] C. Dua, D. and Graff, “UCI Machine Learning Repository Irvine, CA: University of  California, School of Information and Computer Science.,” 2019, \[Online\].  Available: http://archive.ics.uci.edu/ml.    
\[32\] M. Almasoud, T.E. Ward, Detection of Chronic Kidney Disease using Machine  Learning Algorithms with Least Number of Predictors, Int. J. Adv. Comput. Sci.  Appl. 10 (8) (2019) 89–96, https://doi.org/10.14569/IJACSA.2019.0100813.    
\[33\] B. Deepika, V. R. KR, D. N. Rampure, P. P, Devan, and G. G, “Early Prediction of  Chronic Kidney Disease by using Machine Learning Techniques,” *Am. J. Comput.  Sci. Eng. Surv.*, vol. 8, no. 2, Sep. 2020, doi: 10.36648/computer-science engineering-survey.08.02.07.    
\[34\] V. Kunwar, K. Chandel, A. S. Sabitha, and A. Bansal, “Chronic Kidney Disease  analysis using data mining classification techniques,” *Proc. 2016 6th Int. Conf. \-  Cloud Syst. Big Data Eng. Conflu. 2016*, pp. 300–305, Jul. 2016, doi: 10.1109/  CONFLUENCE.2016.7508132.    
\[35\] E. Avci, S. Karakus, O. Ozmen, and D. Avci, “Performance comparison of some  classifiers on Chronic Kidney Disease data,” *6th Int. Symp. Digit. Forensic Secur.  ISDFS 2018 \- Proceeding*, vol. 2018-January, pp. 1–4, May 2018, doi: 10.1109/  ISDFS.2018.8355392.    
\[36\] M. A. Islam, S. Akter, M. S. Hossen, S. A. Keya, S. A. Tisha, and S. Hossain, “Risk  factor prediction of chronic kidney disease based on machine learning algorithms,”  *Proc. 3rd Int. Conf. Intell. Sustain. Syst. ICISS 2020*, pp. 952–957, 2020, doi:  10.1109/ICISS49785.2020.9315878.    
\[37\] T. Emmanuel, T. Maupong, D. Mpoeleng, T. Semong, B. Mphago, O. Tabona,  A survey on missing data in machine learning, vol. 8, no. 1, Springer International  Publishing, 2021.    
\[38\] S. Nijman, et al., Missing data is poorly handled and reported in prediction model  studies using machine learning: a literature review, J. Clin. Epidemiol. 142 (2022)  218–229, https://doi.org/10.1016/j.jclinepi.2021.11.023.    
\[39\] D. M. P. Murti, U. Pujianto, A. P. Wibawa, and M. I. Akbar, “K-Nearest Neighbor (K NN) based Missing Data Imputation,” *Proceeding \- 2019 5th Int. Conf. Sci. Inf.  Technol. Embrac. Ind. 4.0 Towar. Innov. Cyber Phys. Syst. ICSITech 2019*, pp. 83–88,  2019, doi: 10.1109/ICSITech46713.2019.8987530.    
\[40\] S. van Buuren, K. Groothuis-Oudshoorn, mice: Multivariate Imputation by Chained  Equations in R, J. Stat. Softw. 45 (3) (Dec. 2011\) 1–67, https://doi.org/10.18637/  JSS.V045.I03.    
\[41\] C.G. Schuetz, Using neuroimaging to predict relapse to smoking: role of possible  moderators and mediators, Int. J. Methods Psychiatr. Res. vol. 17 Suppl 1(1)  (2008) S78–S82, https://doi.org/10.1002/mpr.    
\[42\] O. Mrudula, A.M. Sowjanya, S. van Buuren, K. Groothuis-Oudshoorn, Z. Zhang,  Analysis of Missing Data Using Multivariate Imputation By Chained Equations  (Mice) in R, Available: J. Stat. Softw. 45 (3) (2016) 189–197 http://www.pubme  dcentral.nih.gov/articlerender.fcgi?artid\=4731595&tool\=pmcentrez&rendertype  \=abstract%0Ahttp://www.jstatsoft.org/v45/i03/%0Ahttp://www.data.conferen  ceworld.in/LNCT/P189-197.pdf.  

\[43\] E. Parzen, “On Estimation of a Probability Density Function and Mode,” vol. 33, no.  3, pp. 1065–1076, Sep. 1962, doi: 10.1214/AOMS/1177704472.    
\[44\] A. Z. Adamov, “Analysis of Feature Selection Techniques for Classification  Problems,” pp. 1–6, Dec. 2021, doi: 10.1109/AICT52784.2021.9620226.  \[45\] M.M. Rahman, et al., Recognition of human emotions using EEG signals: A review,  Comput. Biol. Med. 136 (Sep. 2021), 104696, https://doi.org/10.1016/J.  COMPBIOMED.2021.104696.    
\[46\] M.M. Rahman, A.K. Sarkar, M.A. Hossain, M.A. Moni, EEG-based emotion analysis  using non-linear features and ensemble learning approaches, Expert Syst. Appl. 207  (Nov. 2022), 118025, https://doi.org/10.1016/J.ESWA.2022.118025.    
\[47\] I. Guyon, J. Weston, S. Barnhill, and V. Vapnik, “Gene Selection for Cancer  Classification using Support Vector Machines,” *Mach. Learn. 2002 461*, vol. 46, no.  1, pp. 389–422, 2002, doi: 10.1023/A:1012487302797.    
\[48\] M.B. Kursa, A. Jankowski, W.R. Rudnicki, Boruta – A System for Feature Selection,  Fundam. Informaticae 101 (4) (Jan. 2010\) 271–285, https://doi.org/10.3233/FI 2010-288.    
\[49\] N.V. Chawla, K.W. Bowyer, L.O. Hall, W.P. Kegelmeyer, SMOTE: Synthetic  Minority Over-sampling Technique, J. Artif. Intell. Res. 16 (Jun. 2002\) 321–357,  https://doi.org/10.1613/JAIR.953.    
\[50\] H. Han, W.Y. Wang, B.H. Mao, Borderline-SMOTE: A New Over-Sampling Method  in Imbalanced Data Sets Learning, Lect. Notes Comput. Sci vol. 3644, no. PART I  (2005) 878–887, https://doi.org/10.1007/11538059\_91.    
\[51\] H.M. Nguyen, E.W. Cooper, K. Kamei, Borderline over-sampling for imbalanced  data classification, Int. J. Knowl. Eng. Soft Data Paradig. 3 (1) (2011) 4, https://  doi.org/10.1504/ijkesdp.2011.039875.    
\[52\] L. Breiman, “Random Forests,” *Mach. Learn. 2001 451*, vol. 45, no. 1, pp. 5–32, Oct.  2001, doi: 10.1023/A:1010933404324.    
\[53\] A. Dogan, “A Weighted Majority Voting Ensemble Approach for Classification,”  *2019 4th Int. Conf. Comput. Sci. Eng.*, pp. 1–6, doi: 10.1109/UBMK.2019.8907028.  \[54\] L. Breiman, “Bagging predictors,” *Mach. Learn. 1996 242*, vol. 24, no. 2, pp.  123–140, 1996, doi: 10.1007/BF00058655.    
\[55\] Y. Freund, R.E. Schapire, A Decision-Theoretic Generalization of On-Line Learning  and an Application to Boosting, J. Comput. Syst. Sci. 55 (1) (Aug. 1997\) 119–139,  https://doi.org/10.1006/JCSS.1997.1504.    
\[56\] J.H. Friedman, Stochastic gradient boosting, Comput. Stat. Data Anal. 38 (4) (Feb.  2002\) 367–378, https://doi.org/10.1016/S0167-9473(01)00065-2.  \[57\] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,” *Proc. ACM  SIGKDD Int. Conf. Knowl. Discov. Data Min.*, vol. 13-17-August-2016, pp. 785–794,  Aug. 2016, doi: 10.1145/2939672.2939785.    
\[58\] S. Rahman, M. Irfan, M. Raza, K. M. Ghori, S. Yaqoob, and M. Awais, “Performance  Analysis of Boosting Classifiers in Recognizing Activities of Daily Living,” *Int. J.  Environ. Res. Public Heal. 2020, Vol. 17, Page 1082*, vol. 17, no. 3, p. 1082, Feb.  2020, doi: 10.3390/IJERPH17031082.    
\[59\] G. Ke *et al.*, “LightGBM: A highly efficient gradient boosting decision tree,” *Adv.  Neural Inf. Process. Syst.*, vol. 2017-Decem, no. Nips, pp. 3147–3155, 2017\.  \[60\] D.H. Wolpert, Stacked generalization, Neural Netw. 5 (2) (Jan. 1992\) 241–259,  https://doi.org/10.1016/S0893-6080(05)80023-1.    
\[61\] J. Bergstra, Y. Bengio, “Random Search for Hyper-Parameter Optimization” 13  (2012) 281–305.  

17 