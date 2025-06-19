# pages/2_Check_Eligibility.py
import streamlit as st
import joblib

model = joblib.load("loan_model.pkl")

st.title("Loan Eligibility Checker")

# Form for inputs
with st.form("loan_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.selectbox("Loan Term", [12, 36, 60, 120, 180, 240, 300, 360])
    credit_history = st.selectbox("Credit History", [1.0, 0.0])
    property_area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = [
        1 if gender == "Male" else 0,
        1 if married == "Yes" else 0,
        int(dependents.replace("3+", "3")),
        1 if education == "Graduate" else 0,
        1 if self_employed == "Yes" else 0,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        1 if property_area == "Urban" else (2 if property_area == "Rural" else 0)
    ]
    result = model.predict([input_data])[0]
    st.success("✅ Eligible for Loan" if result == 1 else "❌ Not Eligible")
