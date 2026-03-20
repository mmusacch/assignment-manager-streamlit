import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time


st.set_page_config("Excused Absences", layout="wide", initial_sidebar_state="expanded")

 

requests = [
    {

        "request_id" : "0111212",
        "status": "Pending",
        "course_id": "011101",
        "student_email": "jsmith@university.edu",
        "absence_date": "2026-03-25",
        "submitted_timestamp": "2026-03-19 08:30:00",
        "excuse_type": "Medical",
        "explanation": "I have a scheduled doctor's appointment that I cannot reschedule.",
        "instructor_note": ""
    }
]

json_path_requests = Path("requests.json")
if json_path_requests.exists():
    with open(json_path_requests, "r") as f:
        requests = json.load(f)

else:
    requests = []



if "page" not in st.session_state:
    st.session_state["page"] = "Dashboard"

with st.sidebar:
    if st.button("Dashboard", key="dashboard_btn", use_container_width=True):
        st.session_state["page"] = "dashboard"
        st.rerun()

    if st.button("New Request", key="request_btn", use_container_width=True):
        st.session_state["page"] = "request"
        st.rerun()


if st.session_state["page"] == "dashboard":
    st.title("Excused Absence Dashboard")

    if len(requests) > 0:
        event = st.dataframe(requests,on_select="rerun",selection_mode="single-row")
        if event.selection.rows:
            selected_index = event.selection.rows[0]
            selected_request = requests[selected_index]
            st.subheader("Selected Request")
            st.json(selected_request)
    else:
            st.warning("No requests submitted yet")


#-------
if st.session_state["page"] == "request":
    st.title("Submit Excused Absence Request")

    st.info("This page is under development")

    with st.form("request_form", clear_on_submit=True):
        student_email = st.text_input("Student Email", key="email_input")

        absence_date = st.date_input("Absence Date", key="date_input")
        date_str = absence_date.strftime("%Y-%m-%d")

        excuse_type = st.selectbox("Excuse Type", ["Medical", "University Competitions", "Other"],
                                    key="excuse_select")
        
        explanation = st.text_area("Explanation", key="explanation_input")

        instructor_note = st.text_area("Instructor Note", key="note_input")

        submit = st.form_submit_button("Submit", key="submit_btn")
        if submit:
            new_request = {
                "request_id": str(len(requests) + 1),
                "status": "Pending",
                "course_id": "011101",
                "student_email": student_email,
                "absence_date": date_str,
                "submitted_timestamp": absence_date,
                "excuse_type": excuse_type,
                "explanation": explanation,
                "instructor_note": instructor_note
            }

            requests.append(new_request)

            with open(json_path_requests, "w") as f:
                json.dump(requests, f,)

            st.success("Request submitted successfully")
            st.rerun()
