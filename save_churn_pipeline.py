import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,classification_report)

DATA_PATH = "CustomerChurnDataset.xlsx"
print("Loading Customer Churn Dataset...")

df = pd.read_excel(DATA_PATH)
print("Dataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nColumns in dataset:")
print(df.columns.tolist())

df = df.drop_duplicates()
print("\nShape after removing duplicates:")
print(df.shape)

target_column = "Churn"

feature_columns = ["Age","Gender","Location","Tenure","Contract_Type","Subscription_Plan","Monthly_Charges",
                   "Total_Charges","Payment_Method","Internet_Service","Login_Frequency",
                   "Support_Tickets","Complaints","Avg_Session_Duration"]

required_columns = feature_columns + [target_column]
missing_columns = [column
    for column in required_columns
    if column not in df.columns
]

if missing_columns:
    print("\n❌ ERROR: Missing columns:")
    for column in missing_columns:
        print("-", column)
    print("\nActual columns in your dataset:")
    print(df.columns.tolist())
    raise ValueError("Some required columns are missing.")

X = df[feature_columns].copy()
y = df[target_column].copy()

if y.dtype == "object":
    y = (y.astype(str).str.strip().str.lower())
    y = y.replace({
        "yes": 1,
        "no": 0,
        "true": 1,
        "false": 0,
        "churn": 1,
        "stay": 0,
        "stayed": 0,
        "left": 1
    })
y = pd.to_numeric(y,errors="coerce")

valid_rows = y.notna()
X = X.loc[valid_rows].copy()
y = y.loc[valid_rows].copy()
y = y.astype(int)

numeric_features = ["Age","Tenure","Monthly_Charges","Total_Charges","Login_Frequency",
                    "Support_Tickets","Complaints","Avg_Session_Duration"]

categorical_features = ["Gender","Location","Contract_Type","Subscription_Plan","Payment_Method","Internet_Service"]

numeric_pipeline = Pipeline(
    steps=[("imputer",SimpleImputer(strategy="median")),
        ("scaler",StandardScaler())])

categorical_pipeline = Pipeline(
    steps=[("imputer",SimpleImputer(strategy="most_frequent")),
           ("encoder",OneHotEncoder(handle_unknown="ignore",sparse_output=False))])

preprocessor = ColumnTransformer(transformers=[("numeric",numeric_pipeline,numeric_features),
        ("categorical",categorical_pipeline,categorical_features)])

model = RandomForestClassifier(n_estimators=300,class_weight="balanced",random_state=42,n_jobs=-1)

churn_pipeline = Pipeline(steps=[("preprocessor",preprocessor),
                                 ("model",model)])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=42,stratify=y)
print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))


print("\nTraining Random Forest...")
churn_pipeline.fit(X_train,y_train)
print("✅ Model training completed!")

y_pred = churn_pipeline.predict(X_test)
y_probability = churn_pipeline.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test,y_pred)
precision = precision_score(y_test,y_pred,zero_division=0)
recall = recall_score(y_test,y_pred,zero_division=0)
f1 = f1_score(y_test,y_pred,zero_division=0)
roc_auc = roc_auc_score(y_test,y_probability)
print("\n")
print("MODEL PERFORMANCE")

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
print(f"ROC-AUC   : {roc_auc:.4f}")


print("\nClassification Report:")

print(classification_report(y_test,y_pred,zero_division=0))

os.makedirs("models",exist_ok=True)

MODEL_PATH = "models/churn_pipeline.pkl"
joblib.dump(churn_pipeline,MODEL_PATH)

print("\n")
print("✅ SUCCESS")

print(f"Pipeline saved at: {MODEL_PATH}")

print("\nTesting saved pipeline...")
loaded_pipeline = joblib.load(MODEL_PATH)

sample_data = X_test.head(1)

sample_prediction = loaded_pipeline.predict(sample_data)[0]
sample_probability = loaded_pipeline.predict_proba(sample_data)[0][1]
print("Sample prediction:",sample_prediction)
print("Sample churn probability:",round(sample_probability * 100,2),"%")

print("\n")
print("🎉 churn_pipeline.pkl is ready")
