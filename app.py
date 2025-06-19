import streamlit as st
import joblib

st.set_page_config(page_title="NovaTrust Bank", layout="wide")

# Custom Styling
st.markdown("""
    <style>
    body {
        background-color: #f4f4f4;
    }
    .bank-header {
        background-color: #0b0c10;
        padding: 2rem;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 2rem;
        color: #f1c40f;
    }
    .bank-header h1 {
        font-size: 3rem;
        margin-bottom: 0;
    }
    .bank-header p {
        color: #ccc;
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }
    .stButton > button {
        background-color: #f1c40f;
        color: black;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #d4ac0d;
        color: white;
    }
    .card {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        margin-top: 2rem;
    }
    footer {
        margin-top: 4rem;
        padding: 1rem;
        text-align: center;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
    <div class="bank-header">
        <h1>NovaTrust Bank</h1>
        <p>Smarter. Faster. Safer Banking 💳</p>
    </div>
""", unsafe_allow_html=True)

# Loan Eligibility Form
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("📋 Check Your Loan Eligibility")

    gender = st.selectbox("Gender", ["Male", "Female"])
    married = st.selectbox("Married", ["Yes", "No"])
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
    applicant_income = st.number_input("Applicant Income", 0)
    coapplicant_income = st.number_input("Coapplicant Income", 0)
    loan_amount = st.number_input("Loan Amount", 0)
    loan_term = st.number_input("Loan Term", 0)
    credit_history = st.selectbox("Credit History", ["1", "0"])
    property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

    if st.button("Check Loan Eligibility"):
        # Example encoding — update as per your real pipeline if needed
        user_data = [
            1 if gender == "Male" else 0,
            1 if married == "Yes" else 0,
            1 if education == "Graduate" else 0,
            1 if self_employed == "Yes" else 0,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            int(credit_history),
            1 if property_area == "Urban" else 0,
            1 if property_area == "Semiurban" else 0
        ]

        model = joblib.load("loan_model.pkl")
        prediction = model.predict([user_data])[0]
        result = "✅ Eligible for Loan" if prediction == 1 else "❌ Not Eligible"
        st.success(result)

    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <footer>
        &copy; 2025 NovaTrust Bank. All rights reserved.
    </footer>
""", unsafe_allow_html=True)
