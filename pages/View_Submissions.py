import streamlit as st
from utils import *
from constants import *

course = st.selectbox("Choose Course", options = get_student_courses(username, graded))
#assignment = st.selectbox("Choose Assignment", options = get_submitted_assignments(username, course, assignments))
assignment = st.selectbox("Choose Assignment", options = get_student_assignments(username, course, graded))
file_name = st.selectbox("Choose file", options = get_uploaded_files(username, assignment))

st.markdown("***")
col1, col2, col3 = st.columns(3)

##roll num ,course, assignment, marks, plag, comm
print(get_grade(username, course, assignment, file_name))
with col1:
    st.subheader("Marks")
    try:
        st.write(get_grade(username, course, assignment, file_name)[0])
    except:
        st.write("Not Graded Yet!")
    st.subheader("Plagiarism Status")
    try:
        st.write(get_grade(username, course, assignment, file_name)[1])
    except:
        st.write("Not Graded Yet!")
        
with col3:
    st.subheader("Comments")
    try:
        st.write(get_grade(username, course, assignment, file_name)[2])
    except:
        st.write("Not Graded Yet!")

    
#st.markdown("***")

#st.subheader("Request to re-evaulate")
#request = st.text_area(label = "Enter further details")


#col1, col2, col3 = st.columns(3)
#with col2:
#    submit = st.button(label = "Submit Request")    
