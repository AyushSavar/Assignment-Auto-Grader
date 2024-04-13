import hmac
import streamlit as st

def write_constants(ta):
    """Writes constants to the file constants.py"""
    with open("constants.py", "w") as file:
        file.write(f"ta = {ta}\n")
        file.write(f"username = '{st.session_state.get('username', '')}'\n")

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
        if st.session_state["username"] in st.secrets["passwords"] and hmac.compare_digest(
            st.session_state["password"], st.secrets.passwords[st.session_state["username"]]
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
if st.session_state["username"].startswith("s"):
    write_constants(0)
else:
    write_constants(1)
