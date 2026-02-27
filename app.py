import streamlit as st

# Step 1: Header first
st.title("AI Course Manager")
st.header("Course Assignments Manager")
st.subheader("Course Assignments Manager")

st.divider()
#Step 2: Define assignments list (Week 2 continuity)
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
#3 Step3: Add New Assignments 
st.subheader("Add new assignment")

with st.coontainer(border=True):

    col1,col2= st.columns(2,1)

    with col1:
        with st.container(border=True):
            st.markdown("## Assignment Details")
            title = st.text_input("Assignment title", placeholder="homework1",help="enter a short name")
            description = st.text_area("Assignment description", placeholder = "ex.details.")

    with col2:
        st.markdown("**Due Date Selection**")
        due_date = st.date_input("Due Date")