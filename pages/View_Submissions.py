import streamlit as st
from utils import *
from constants import *

course = st.selectbox("Choose Course", options = get_student_courses(username, graded))
#assignment = st.selectbox("Choose Assignment", options = get_submitted_assignments(username, course, assignments))
assignment = st.selectbox("Choose Assignment", options = get_student_assignments(username, course, graded))
file_name = st.selectbox("Choose file", options = get_uploaded_files(username, assignment))


st.markdown("***")
late_status = get_late_status(username, course, assignment, file_name)
if (late_status):
    st.write("Late Submission !")

col1, col2 = st.columns(2)

##roll num ,course, assignment, marks, plag, comm
#print(get_grade(username, course, assignment, file_name))

with col1:
    st.subheader("Marks")
    try:
        st.write(get_grade(username, course, assignment, file_name)[0])
    except:
        st.write("Not Graded Yet!")
        
with col2:
    st.subheader("Plagiarism Status")
    try:
        st.write(get_grade(username, course, assignment, file_name)[1])
    except:
        st.write("Not Graded Yet!")
    
st.subheader("Additional Remarks")
col1, col2 = st.columns(2)
try:
    feedback = (get_grade(username, course, assignment, file_name)[2])
    
    with col1:
        
        if (len(feedback)==1):
            comments = st.text_area(label = "Remarks", value = feedback[0][0])
        else:
            comments = st.text_area(label = "Comments", value = feedback[0][0])
            expressions = st.text_area(label = "Expressions", value = feedback[1][0])
            variables = st.text_area(label = "Variable Naming", value = feedback[4][0])
    with col2:
        if (len(feedback)>1):
            repetition = st.text_area(label = "Repetition", value = feedback[2][0])
            indentation = st.text_area(label = "Indentation", value = feedback[3][0])
except:
    print(1)        
    
#st.markdown("***")

#st.subheader("Request to re-evaulate")
#request = st.text_area(label = "Enter further details")


#col1, col2, col3 = st.columns(3)
#with col2:
#    submit = st.button(label = "Submit Request")    
