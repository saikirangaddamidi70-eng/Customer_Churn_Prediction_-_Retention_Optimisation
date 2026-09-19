import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load(
        "models/churn_pipeline.pkl"
    )

try:
    pipeline = load_model()
except Exception as e:
    st.error("❌ Could not load churn_pipeline.pkl")
    st.info("Check that models/churn_pipeline.pkl exists.")
    st.exception(e)
    st.stop()

st.title("📊 Customer Churn Prediction & Retention Optimization System")
st.write("Enter customer information to predict churn probability and determine retention priority.")

st.header("👤 Customer Information")
col1, col2, col3 = st.columns(3)
with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=30
    )
    tenure = st.number_input(
        "Tenure (months)",
        min_value=0,
        max_value=200,
        value=12
    )
    gender = st.selectbox(
        "Gender",
        [
            "Male",
            "Female",
            "Other"
        ]
    )

with col2:
    location = st.text_input(
        "Location",
        value="Hyderabad"
    )
    contract_type = st.selectbox(
        "Contract Type",
        [
            "Month-to-Month",
            "One Year",
            "Two Year"
        ]
    )
    subscription_plan = st.selectbox(
        "Subscription Plan",
        [
            "Basic",
            "Standard",
            "Premium"
        ]
    )
with col3:
    monthly_charges = st.number_input(
        "Monthly Charges (₹)",
        min_value=0.0,
        value=799.0
    )
    total_charges = st.number_input(
        "Total Charges (₹)",
        min_value=0.0,
        value=5000.0
    )
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Credit Card",
            "Debit Card",
            "UPI",
            "Bank Transfer",
            "Cash"
        ]
    )
internet_service = st.selectbox(
    "Internet Service",
    ["DSL","Fiber","None"]
)
st.header("📱 Customer Behavior")
col1, col2, col3 = st.columns(3)

with col1:
    login_frequency = st.number_input(
        "Login Frequency",
        min_value=0.0,
        value=10.0
    )
with col2:
    support_tickets = st.number_input(
        "Support Tickets",
        min_value=0,
        value=1
    )
with col3:
    complaints = st.number_input(
        "Complaints",
        min_value=0,
        value=0
    )
avg_session_duration = st.number_input(
    "Average Session Duration (minutes)",
    min_value=0.0,
    value=30.0
)
st.divider()
predict_button = st.button(
    "🔮 Predict Churn",
    type="primary",
    use_container_width=True
)

if predict_button:
    input_data = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Location": [location],
        "Tenure": [tenure],
        "Contract_Type": [contract_type],
        "Subscription_Plan": [subscription_plan],
        "Monthly_Charges": [monthly_charges],
        "Total_Charges": [total_charges],
        "Payment_Method": [payment_method],
        "Internet_Service": [internet_service],
        "Login_Frequency": [login_frequency],
        "Support_Tickets": [support_tickets],
        "Complaints": [complaints],
        "Avg_Session_Duration": [avg_session_duration]
    })

    try:
        prediction = pipeline.predict(
            input_data
        )[0]
        probability = pipeline.predict_proba(
            input_data
        )[0][1]
        probability_percent = (
            probability * 100
        )

        if probability < 0.30:
            risk_level = "Low"
        elif probability < 0.60:
            risk_level = "Medium"
        elif probability < 0.80:
            risk_level = "High"
        else:
            risk_level = "Critical"


        if total_charges >= 10000:
            customer_value = "High"
        elif total_charges >= 5000:
            customer_value = "Medium"
        else:
            customer_value = "Low"

        if (risk_level in ["High","Critical"] and customer_value == "High"):
            retention_priority = ("🚨 Immediate Retention Priority")
        elif risk_level in ["High","Critical"]:
            retention_priority = ("⚠️ Targeted Retention")
        elif (risk_level == "Medium" and customer_value == "High"):
            retention_priority = ("👀 Monitor Closely")
        else:
            retention_priority = ("✅ Normal Customer Management")

        st.header("📊 Prediction Result")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Churn Probability",f"{probability_percent:.1f}%")
        with col2:
            st.metric("Risk Level",risk_level)

        with col3:
            st.metric("Customer Value",customer_value)

        if prediction == 1:
            st.error("⚠️ Customer is predicted to churn.")
        else:
            st.success("✅ Customer is predicted to stay.")

        st.subheader("🔎 Potential Risk Factors")
        risk_factors = []
        if tenure < 6:
            risk_factors.append("Short customer tenure")
        if monthly_charges > 800:
            risk_factors.append("High monthly charges")
        if login_frequency < 5:
            risk_factors.append("Low login frequency")
        if support_tickets >= 3:
            risk_factors.append("Multiple support tickets")
        if complaints >= 2:
            risk_factors.append("Multiple complaints")
        if avg_session_duration < 15:
            risk_factors.append("Low average session duration")
        if risk_factors:
            for factor in risk_factors:
                st.write("•",factor)
        else:
            st.write("No major predefined risk indicators detected.")


        st.subheader("🎯 Retention Priority")
        st.info(retention_priority)

        st.subheader("💡 Recommended Actions")
        recommendations = []
        if tenure < 6:
            recommendations.append("Provide early-stage onboarding and engagement support.")
        if monthly_charges > 800:
            recommendations.append("Review pricing and subscription-plan fit.")
        if login_frequency < 5:
            recommendations.append("Consider a customer engagement campaign.")
        if support_tickets >= 3:
            recommendations.append("Arrange customer-support follow-up.")
        if complaints >= 2:
            recommendations.append("Investigate unresolved complaints.")
        if avg_session_duration < 15:
            recommendations.append("Investigate low customer engagement.")
        if not recommendations:
            recommendations.append("Continue normal customer engagement and monitor future behavior.")
        for recommendation in recommendations:
            st.write("•",recommendation)

        with st.expander("🔍 View Customer Input"):
            st.dataframe(input_data,use_container_width=True)

    except Exception as e:
        st.error("❌ Prediction failed.")
        st.write("Please check that the category values and feature names match the training dataset.")
        st.exception(e)