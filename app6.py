import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "user" not in st.session_state:
    st.session_state["user"] = None
if "role" not in st.session_state:
    st.session_state["role"] = None 
if "page" not in st.session_state:
    st.session_state["page"] = "login"

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


json_path = Path("users.json")
if json_path.exists(): 
    with open(json_path, "r") as f:
        users = json.load(f)


if st.session_state["role"] == "instructor":
    if st.session_state["page"] == "home":
        st.markdown("welcome! This is the Instructor Dashboard")
        if st.button("Go to Dashboard", key="dashboard_view_btn", type="primary", use_container_width=True):
            st.session_state["page"] = "dashboard"
            st.rerun()
        #elif st.session_state["page"] = 
                
        tab1, tab2, tab3 = st.tabs(["View Assignments", "Add New Assignment", "Update an Assignment"])

        with tab1:
            tab_option= st.radio("View/Search", ["View","search"])
            if tab_option == "View":
                st.dataframe(assignments)
            else:
                titles=[]
                for assignment in assignments:
                    titles.append(asssignment="title")

                selected_title= st.selectbox("Select a title",titles,keys="selected_title")

                selected_assignment=[]

                for assignment in assignments:
                    if assignment["title"] == selected_title:
                        selected_assignment=assignment
                        break
                
                st.divider()
                selected_assignment= st.selectbox("Select title",
                                                options=assignments,
                                                format_func=lambda x: f"{x['title']} ({x['type']})")


                if selected_assignment:
                    with st.expander("assignment details", expanded=True):
                        st.markdown(f'### Titles: {selected_assignment["title"]}')
                        st.markdown(f'description: {selected_assignment["description"]}')
                        st.markdown(f'Type: =={selected_assignment["type"]}')

        with tab2:
            st.info("coming soon")
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



            json_path = Path("assignments.json")

            if btn_save:
                if not title:
                    st.warning("Working on it for now")
                else:
                    with st.spinner("assignment is being recorded..."):
                        time.sleep(5)
                        new_assignment_id = "HW" + str(next_assignment_id_number)
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
                        st.rerun()
        with tab3: 
            st.markdown(f"### Update an Assignment")
            titles = []
            for assignment in assignments:
                titles.append(assignment["title"])

            selected_title = st.selectbox("Select a title", titles,key="selected_title_edit")

            assignment_edit=[]
            for assignment in assignments:
                if assignment["title"] == selected_title:
                    assignment_edit = assignment
                    break


            if assignment_edit: 
                edit_title = st.text_input("Title", key=f"edit_title_{assignment_edit['id']}",
                                        value=assignment_edit['title'])
                edit_description = st.text_area("Description", key="edit_description",
                                                value=assignment_edit['description'])

                type_options=["Homework","Lab"]
                selected_index = type_options.index(assignment_edit["type"])

                edit_type = st.radio("Type",("Homework","Lab"),
                                    key=f'edit_type_{assignment_edit["id"]}',
                                    index=selected_index)
                
            btn_update = st.button("Update", key="update_button",type="primary")
            if btn_update:
                with st.spinner("Updating...."):
                    time.sleep(5)
                    assignment_edit['title']=edit_title
                    assignment_edit['description']= edit_description

                    with json_path.open("W",encoding="utf-8") as f:
                        json.dump(assignments,f)

                    st.success("Updated...")
                    time.sleep(5)
                    st.rerun()


elif st.session_state["role"]=="Admin":
    st.markdown["Welcome! This is the Admin Dashboard!"]

    if st.button("Log out", type="primary", use_container_width=True):
        with st.spinner("logging out..."):
            st.session_state["logged_out"] = False
            st.session_state["user"] = False
            st.session_state["role"] = False
            st.session_state["page"] = "login"
            time.sleep(4) 
            st.rerun
else:


    st.title("Course Manager App")


    #login
    st.subheader("Log In")
    with st.container(border=True):
        email_input = st.text_input("Email", key="login_email")
        password_input = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Log In", type="secondary", use_container_width=True):
            with st.spinner("Logging in..."):
                time.sleep(2) # Fake backend delay
                
                # Find user
                found_user = None
                for user in users:
                    if user["email"].strip().lower() == email_input.strip().lower() and user["password"] == password_input:
                        found_user = user
                        break
                
                if found_user:
                    st.success(f"Welcome back, {found_user['email']}!")
                    st.session_state["logged_in"] = True
                    st.session_state["user"] = found_user
                    st.session_state["role"] = found_user["role"]
                    st.session_state["page"] = "home"

                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    # --- REGISTRATION ---
    st.subheader("New Instructor Account")
    with st.container(border=True):
        new_email = st.text_input("Email Address", key="reg_email")
        new_password = st.text_input("Password", type="password", key="reg_password")
        
        if st.button("Create Account", type="secondary", use_container_width=True):
            with st.spinner("Creating account..."):
                time.sleep(2) # Fake backend delay
                # ... (Assume validation logic here) ...
                users.append({
                    "id": str(uuid.uuid4()),
                    "email": new_email,
                    "password": new_password,
                    "role": "Instructor"
                })
                with open(json_file, "w") as f:
                    json.dump(users, f, indent=4)
                st.success("Account created!")
                st.rerun()

    st.write("---")
    st.dataframe(users)

with st.sidebar:
    st.markdown("Course Manager Sidebar")
    if st.session_state["logged_in"] == True:
        user = st.session_state["user"]
        st.markdown(f"logged User Email: {user['email']}")


json_file = Path("users.json")
if json_file.exists():
    with open(json_file, "r") as f:
        users = json.load(f)


