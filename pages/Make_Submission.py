import streamlit as st
from utils import *
from constants import *
from datetime import date

course = st.selectbox("Choose Course", options = get_student_courses(username, assigned))
assignment = st.selectbox("Choose Assignment", options = get_student_assignments(username, course, assigned))
files = st.file_uploader("Upload File", accept_multiple_files = True)
comment = st.text_area(label = "Details")

col1, col2, col3 = st.columns(3)
with col2:
    submit = st.button(label = "Make Submission")
    if (submit):
        for file in files:
            st.write((add_submission(username, course, assignment, file.read(), comment, assignments, file.name,date.today())))