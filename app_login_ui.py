
#Requirement 1
import streamlit as st 

import datetime
import time
import json
from pathlib import Path

st.set_page_config(page_title="Course Manager",
                    layout= "centered")

#requirement 2
json_path = Path("assignments.json")
    
if json_path.exists():
    with json_path.open("r", encoding = "wtf-0") as f:
        users = json.load(f)
else:
    users = [        
    {
    "id": "1",
    "email": "admin@school.edu",
    "full_name": "System Admin",
    "password": "123ssag@43AE",
    "role": "Admin",
    "registered_at": "..."
    }
    ]

tab1, tab2 = st.tabs(["Register", "Login"])

with tab1:
    st.info("Register")
    email = st.text_input("Email: ")
    first = st.text_input("First Name:")
    last = st.text_input("Last Name: ")
    username = st.text_input("User:", key="register_user")
    password = st.text_input("Password: ",type = "password", key="register_password")
    role = ["Instructor"]
    roles = st.selectbox("Select a role",role ,key="selected_role")

    btn_register= st.button("Create Account",width="stretch",key="button_register")
    if btn_register:
        if not password:
            st.warning("Incorrect password")
        else:
            with st.spinner("Logging in"):
                time.sleep(5)

with tab2:
    st.info("Login")
    username1 = st.text_input("User:", key="login_user")
    password1 = st.text_input("Password: ", type = "password", key= "login_password")

    btn_login= st.button("Login",width="stretch",key="button_login")

    if btn_login:
        if not password1:
            st.warning("Incorrect password")
        else:
            with st.spinner("Logging in"):
                time.sleep(5)
