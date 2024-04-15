import streamlit as st
from utils import *
from constants import *
from plagiarism import *

from auto_evaluate import *

assignment = st.selectbox(label = "Choose Assignment: ", options = get_assignments_to_evaluate(username, ta))

course = get_course(username)

plagiarism_tracker = {}

col1, col2, col3 = st.columns(3)
with col2:
    run_plag_check = st.button("Run Plagiarism Check")
    if (run_plag_check):
        plag_list = plag_checker_master(get_plag_list(username, assignment)[1])
    
        student_list = get_plag_list(username, assignment)[0]
        for i in range(len(plag_list)):
            st.write("File {}: ".format(i+1))    
            st.write("Plagiarism found for ", sum(plag_list[i]),"students")
            for j in range(len(student_list)):
                if (plag_list[i][j]):
                    st.write(student_list[j], end=" ")
                    if student_list[j] in plagiarism_tracker:
                        plagiarism_tracker[student_list[j]]+="Plagiarism found in file {}\n".format(i+1)
                    else:
                        plagiarism_tracker[student_list[j]]="Plagiarism found in file {}\n".format(i+1)
st.markdown("***")


student = st.selectbox(label = "Choose Student: ", options = get_students_associated(username, assignment, assignments))
file_name = st.selectbox(label = "Choose file: ", options = get_uploaded_files(student, assignment))
files_input = st.file_uploader("Input Test Cases", accept_multiple_files = True)
files_output = st.file_uploader("Output", accept_multiple_files = True)
for i in range(len(files_input)):
    files_input[i] = files_input[i].read().decode('utf-8')
for i in range(len(files_output)):
    files_output[i] = files_output[i].read().decode('utf-8')

eval_assigment = st.button("Auto Evaluate") 
if (eval_assigment):
    
    st.write(tc_checker(get_code(username, assignment, student, file_name), files_input, files_output)[0])
    late_status = get_late_status(student, course, assignment, file_name)
    if (late_status):
        st.write("Late Submission ! Deduct marks accordingly")
    col1, col2 = st.columns(2)
    with col1:
        marks = st.text_area(label = "Marks out of 100", value = tc_checker(get_code(username, assignment, student, file_name), files_input, files_output)[2])
        
        
        #print(get_late_status(username, course, assignment, file_name))
        
    with col2:
           
        if (student in plagiarism_tracker):
            plag = st.text_area(label = "Plagiarism", value = plagiarism_tracker[student])
        else:
            plag = st.text_area(label = "Plagiarism", value = "No plagiarism found")
     
    st.markdown("***")
    st.subheader("Advanced Analysis")
    col1, col2 = st.columns(2)
    feedback = tc_checker(get_code(username, assignment, student, file_name), files_input, files_output)[1]
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
        
    st.write(insert_into_graded(student, get_course(username), assignment, marks, plag, feedback, file_name))

#modifieable text areas with values by evaulation

##Remarks visible
##submitted file visible
##return button
