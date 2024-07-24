import hmac
import streamlit as st
from passwords import *
import hashlib

def write_constants(ta):
    try:
        if st.session_state["username"]:
            #Writes constants to the file constants.py
            with open("constants.py", "w") as file:
                file.write(f"TA = {ta}\n")
                file.write(f"username = '{st.session_state.get('username', '')}'\n")
    except:
        return
    
# Write default constants
write_constants(-1)

def check_password():
    """Returns `True` if the user had a correct password."""
    
    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        hashed_password = hashlib.sha256(st.session_state["password"].encode()).hexdigest()
        if (st.session_state["username"] in usernames and passwords[st.session_state["username"]]==hashed_password
        ):
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False

if not check_password():
    st.stop()

# Main Streamlit app starts here
st.header("Authentication Successful!")

# Write constants based on authentication success


try:
    if st.session_state["username"].startswith("s"):
        write_constants(0)
    else:
        write_constants(1)
except: 
    pass