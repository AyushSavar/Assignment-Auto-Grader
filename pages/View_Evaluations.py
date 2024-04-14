import streamlit as st
from utils import *
from constants import *

assignment = st.selectbox("Choose Assignment", options = get_assignments_to_evaluate(username, graded))
student = st.selectbox("Choose Student", options = get_students_associated(username, assignment, graded))
file_name = st.selectbox("Choose file", options = get_uploaded_files(student, assignment))
course = get_course(username)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Marks")
    try:
        st.write(get_grade(student, course, assignment, file_name)[0])
    except:
        st.write("Not Graded Yet!")
    st.subheader("Plagiarism Status")
    try:
        st.write(get_grade(student, course, assignment, file_name)[1])
    except:
        st.write("Not Graded Yet!")
        
with col3:
    st.subheader("Comments")
    try:
        st.write(get_grade(student, course, assignment, file_name)[2])
    except:
        st.write("Not Graded Yet!")
