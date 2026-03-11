import streamlit as st 

st.title("Course Management App")
st.header("Assignment Management")
st.subheader("Dashboard")

next_assignment_id_number = 3 

#creates a space/row
st.divider() 
st.markdown("")

#load data
assignments = [
    {
        "id":"HW1",
        "title":"Intro to Database",
        "description": "basics of database deisgn",
        "prints" : 100,
        "type" : "homework" 
},
{
    "id": "HW2",
    "title":"Normalization",
    "description":"normalizing",
    "points":100 ,
    "type":"homework"
}
]

#input
#st.markdown("# ADD NEW ASSIGNMENT")
st.markdown("## ADD NEW ASSIGNMENT")
#st.markdown("### ADD NEW ASSIGNMENT")

title = st.text_input("Title: ")
description = st.text_area("Description", placeholder="normalization is covered here",
                           help="Here you are entering assignment details")
points = st.number_input("Points")

#assignment_type = st.text_input("Choose assignment type")
assignment_type = st.radio("Type" , ["Homework", "Lab"], horizontal=True)
st.caption("Homework type") 
assignment_type2 = st.selectbox("Type" , ["Select and option","Homework", "Lab"] )

if assignment_type2 == "other":
    assignment_type2 = st.text_input("Type", placeholder ="Enter the assignment type")

due_date = st.date_input("Due Date")
btn_save= st.button("Save",width="stretch")

import time
import json
from pathlib import Path

json_path = Path("assignments.json")

if btn_save:
    if not title:
        st.warning("Working on it for now")
    else:
        with st.spinner("assignment is being recorded..."):
            time.sleep(5)
            new_assignment_id = "HW" + str(new_assignment_id)
            next_assignment_id_number += 1

            assignments.append(
                {
                    "id" : new_assignment_id,
                    "title" : title,
                    "description" : description,
                    "points" : points, 
                    "type" : assignment_type
                }
            )

            #record into json file
            with json_path.open("w",encoding="utf-8") as f:
                json.dump(assignments, f)


            st.success("New assignment is recorded")
            st.info("this is a new assignment")
            st.dataframe(assignments)