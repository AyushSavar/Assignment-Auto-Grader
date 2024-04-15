import streamlit as st
from constants import *
from utils import *
import datetime    

if (TA):
    assignment = st.text_input(label = "Enter Assignment Name")
    deadline = st.date_input(label = "Choose Deadline")
    deadline = deadline.strftime('%Y-%m-%d')

    col1, col2, col3 = st.columns(3)
    with col2:
        submit = st.button(label="Create Assignment")
        course = get_course(username)
        if (submit):
            roll_numbers = get_roll_numbers(username)
            for roll_number in roll_numbers:
                insert_into_assigned(roll_number, course, assignment, deadline)
else:
    st.subheader("You do not have authorization")
