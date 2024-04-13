import streamlit as st
from utils import *
from constants import *


assignment = st.selectbox(label = "Choose Assignment: ", options = get_assignments_to_evaluate(username, ta)[0])

col1, col2, col3 = st.columns(3)
with col2:
    run_plag_check = st.button("Run Plagiarism Check")
    if (run_plag_check):
        plag_list = plag_checker(get_assignments_to_evaluate(username, ta)[1])
st.markdown("***")
student = st.selectbox(label = "Choose Student: ", options = ["Student 1", "Student 2"])

col1, col2, col3 = st.columns(3)
with col2:
    eval_assigment = st.button("Auto Evaluate") 

#modifieable text areas with values by evaulation

##Remarks visible
##submitted file visible
##return button
