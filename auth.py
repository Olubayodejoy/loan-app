# auth.py
import streamlit as st

def login():
    st.sidebar.title("🔐 Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        if username == "admin" and password == "novatrust123":
            st.session_state['logged_in'] = True
            st.experimental_rerun()
        else:
            st.sidebar.error("Invalid credentials")

def logout():
    st.sidebar.button("Logout", on_click=lambda: st.session_state.clear())
