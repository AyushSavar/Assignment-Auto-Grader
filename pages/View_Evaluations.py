import streamlit as st
from utils import *

assignment = st.selectbox("Choose Assignment", options = ['Assignment 1', 'Assignment 2', 'Assignment 3'])
student = st.selectbox("Choose Student", options = ['Student 1','Student 2','Student 3'])


col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Marks")
    st.write("10/10")
    st.subheader("Plagiarism Status")
    st.write("Not found")
    
with col3:
    st.subheader("Comments")
    st.write("Good code")
    

