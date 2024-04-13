import streamlit as st
from utils import *
from constants import *

course = st.selectbox("Choose Course", options = get_student_courses(username, assigned))
#assignment = st.selectbox("Choose Assignment", options = get_submitted_assignments(username, course, assignments))
assignment = st.selectbox("Choose Assignment", options = ["Assignment 1","Assignment 2","Assignment 3"])
st.markdown("***")
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Marks")
    st.write("10/10")
    st.subheader("Plagiarism Status")
    st.write("Not found")
    
with col3:
    st.subheader("Comments")
    st.write("Good code")
    
st.markdown("***")



st.subheader("Request to re-evaulate")
request = st.text_area(label = "Enter further details")


col1, col2, col3 = st.columns(3)
with col2:
    submit = st.button(label = "Submit Request")    
