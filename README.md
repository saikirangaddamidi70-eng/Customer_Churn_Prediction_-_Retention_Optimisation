# Customer Churn Prediction & Retention Optimization System

## 📌 Project Overview

An end-to-end Data Science project that predicts customer churn, estimates churn probability, explains the reasons behind predictions, identifies high-value customers at risk, and prioritizes customers for retention.

The project goes beyond basic churn classification by combining SQL, Machine Learning, SHAP explainability, customer segmentation, Power BI, and Streamlit.

---

## 🎯 Objectives

- Predict customers likely to churn
- Calculate individual churn probability
- Identify important churn-related factors
- Identify high-value customers at risk
- Segment customers based on risk and value
- Prioritize customers for retention
- Provide business-oriented retention recommendations
- Build interactive dashboards and a prediction application

---

## 🔄 Project Workflow

Raw Customer Data
       ↓
      SQL
       ↓
Data Cleaning
       ↓
     EDA
       ↓
Feature Engineering
       ↓
Train / Test Split
       ↓
Class Imbalance Handling
       ↓
ML Model Training
       ↓
Hyperparameter Tuning
       ↓
Model Evaluation
       ↓
Churn Probability
       ↓
SHAP Explainability
       ↓
Risk Scoring
       ↓
Customer Segmentation
       ↓
Retention Prioritization
       ↓
Power BI + Streamlit

---

## 📊 Dataset

The dataset contains customer-level information such as:

- Customer ID
- Age
- Gender
- Location
- Tenure
- Contract Type
- Subscription Plan
- Monthly Charges
- Total Charges
- Payment Method
- Service Type
- Usage Frequency
- Support Tickets
- Complaints
- Average Session Duration
- Last Activity
- Churn

### Target

1 → Churned
0 → Stayed

---

## 🧹 Data Preparation

The project includes:

- Missing-value detection
- Duplicate detection
- Data-type correction
- Invalid-value investigation
- Outlier analysis
- Categorical encoding
- Feature preprocessing

---

## 🔍 Exploratory Data Analysis

Churn is analyzed across:

- Tenure
- Contract Type
- Subscription Plan
- Monthly Charges
- Payment Method
- Service Type
- Usage Frequency
- Support Tickets
- Complaints
- Customer Segments

The analysis focuses on identifying patterns associated with customer churn.

---

## ⚙️ Feature Engineering

Additional features are created to capture customer behavior and value.

Examples

Avg_Sessions_Per_Week
Days_Since_Last_Login
Usage_Trend
Tickets_Per_Month
Complaints_Per_Month
Revenue_Per_Month
Charge_To_Tenure_Ratio
Tenure_Group
High_Value_Customer
Low_Engagement

---

## 🤖 Machine Learning

The following models are considered:

- Logistic Regression
- Decision Tree
- Random Forest
- KNN
- SVM
- Gradient Boosting
- XGBoost

Class Imbalance Handling

Appropriate techniques include:

- Stratified splitting
- Class weights
- SMOTE where appropriate

---

## 🔧 Hyperparameter Tuning

The strongest models are tuned using:

- "GridSearchCV"
- "RandomizedSearchCV"

The final model is selected based on relevant business and model-performance metrics.

---

## 📈 Model Evaluation

Models are evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- PR-AUC

Additional Evaluation

- Confusion Matrix
- ROC Curve
- Precision-Recall Curve

Model Comparison

Model| Accuracy| Precision| Recall| F1| ROC-AUC| PR-AUC
Logistic Regression| —| —| —| —| —| —
Random Forest| —| —| —| —| —| —
Gradient Boosting| —| —| —| —| —| —
XGBoost| —| —| —| —| —| —

«Results will be updated after model training.»

---

## 🎯 Churn Risk Scoring

Instead of only predicting churn/not churn, the system generates a churn probability.

Example

Customer A → 87%
Customer B → 63%
Customer C → 12%

Risk Levels

Probability| Risk
0–30%| Low
31–60%| Medium
61–80%| High
81–100%| Critical

«Risk thresholds are project-specific and can be adjusted according to business requirements.»

---

## 🔎 SHAP Explainability

SHAP is used to understand why the model predicts churn.

Global Analysis

Identifies the most influential features across customers.

Individual Analysis

Explains the major factors contributing to an individual customer's prediction.

Example

Customer ID: 1234
Churn Probability: 87%

Important Factors:
- Short tenure
- Low engagement
- High monthly charges
- Multiple support tickets

---

## 👥 Customer Segmentation

Customers are segmented using churn risk + customer value.

Segment| Risk| Value| Action
Critical| High| High| Immediate retention
Priority| High| Medium| Targeted retention
Watch| Medium| High| Monitor
Stable| Low| High| Loyalty strategy
Low Priority| Low| Low| Normal service

---

## 🎯 Retention Optimization

The system prioritizes customers based on:

Churn Risk + Customer Value

Potential Business Recommendations

- Personalized offers
- Discounts
- Plan upgrades
- Customer-support intervention
- Loyalty rewards
- Engagement campaigns

«These are recommendations based on observed risk factors, not claims of causal impact.»

---

## 📊 Power BI Dashboard

The project includes four dashboard sections.

### 1. Executive Overview

- Total Customers
- Churn Rate
- High-Risk Customers
- Revenue at Risk
- Customer Segments

<img width="1397" height="782" alt="Screenshot 2026-09-18 192437" src="https://github.com/user-attachments/assets/3ab0383a-a838-44fa-8406-03595646fc03" />


### 2. Churn Analysis

- Churn by Tenure
- Churn by Contract
- Churn by Payment Method
- Churn by Service Type
- Churn by Customer Segment

### 3. Customer Risk

- Customer ID
- Churn Probability
- Risk Level
- Customer Value
- Risk Factors
- Recommended Action

### 4. Retention

- High-value/high-risk customers
- Risk distribution
- Retention priorities
- Revenue at risk

---

## 🌐 Streamlit Application

The Streamlit application allows users to enter customer information and receive:

- Churn Probability
- Risk Level
- Major Risk Factors
- Recommended Action

Example

Churn Probability: 82%
Risk Level: HIGH

Major Risk Factors:
• Short tenure
• Low engagement
• High monthly charges
• Multiple support tickets

---

## 🛠️ Technologies

Category| Technologies
Programming| Python
Data Analysis| Pandas, NumPy
Visualization| Matplotlib, Seaborn, Power BI
Database| SQL, MySQL
Machine Learning| Scikit-learn, XGBoost
Explainability| SHAP
Deployment| Streamlit
Version Control| Git, GitHub
Environment| Jupyter Notebook

---

## 📌 Key Results

This section will be updated after completing the project.

- Overall Churn Rate: "XX%"
- High-Risk Customers: "XX"
- Critical-Risk Customers: "XX"
- High-Value Customers at Risk: "XX"
- Final Model: "Model Name"
- F1-Score: "XX"
- ROC-AUC: "XX"
- PR-AUC: "XX"

---

## 🚀 Future Improvements

- Probability calibration
- Customer Lifetime Value prediction
- Survival analysis
- Uplift modeling
- A/B testing for retention strategies
- Real-time prediction
- Model monitoring
- Cloud deployment

---

# 👨‍💻 Author

## Gaddamidi Sai Kiran

B.Tech – Artificial Intelligence & Data Science

Aspiring Data Scientist


