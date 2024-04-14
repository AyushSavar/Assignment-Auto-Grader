import streamlit as st
from utils import *
from constants import *
from plagiarism import *
from auto_evaluate import *

assignment = st.selectbox(label = "Choose Assignment: ", options = get_assignments_to_evaluate(username, ta))

col1, col2, col3 = st.columns(3)
with col2:
    run_plag_check = st.button("Run Plagiarism Check")
    if (run_plag_check):
        plag_list = plag_checker_master(get_plag_list(username, assignment)[1])
    
        student_list = get_plag_list(username, assignment)[0]
        print("####")
        print(plag_list)
        print("####")
        print("@@@@")
        print(student_list)
        print("@@@@")
        
        for i in range(len(plag_list)):
            st.write("File {}: ".format(i+1))    
            st.write("Plagiarism found for ", sum(plag_list[i]),"students")
            for j in range(len(student_list)):
                if (plag_list[i][j]):
                    st.write(student_list[j], end=" ")
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
    print(get_code(username, assignment, student, file_name))
    print(files_input)
    print(files_output)
    st.write(tc_checker(get_code(username, assignment, student, file_name), files_input, files_output)[0])

    col1, col2 = st.columns(2)
    with col1:
        marks = st.text_area(label = "Marks out of 100", value = tc_checker(get_code(username, assignment, student, file_name), files_input, files_output)[2])
        plag = st.text_area(label = "Plagiarism")
    with col2:
        comments = st.text_area(label = "Remarks", value = tc_checker(get_code(username, assignment, student, file_name), files_input, files_output)[1])        
    st.write(insert_into_graded(student, get_course(username), assignment, marks, plag, comments, file_name))

#modifieable text areas with values by evaulation

##Remarks visible
##submitted file visible
##return button
