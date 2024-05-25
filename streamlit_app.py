import streamlit as st
import time
from navigation import menu

# streamlit run streamlit_app.py

# Initialize st.session_state.logged_in to None
if "logged_in" not in st.session_state:
    st.session_state.logged_in = None

menu() # Render the dynamic menu!


def authenticate(username, password):
    # Replace with your authentication logic
    if username == "test" and password == "test":
        return True
    else:
        return False


def show_login():
    # Login Section
    st.title("Login Page (streamlit_app.py)")
    st.write("Please log in to continue (username `test`, password `test`).")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login", type="primary")

    if login_button:
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            st.session_state.logged_in = True
            st.success("Logged in!")
            time.sleep(0.5)
            st.switch_page("pages/page1.py")
        else:
            st.session_state.logged_in = False
            st.error("Incorrect username or password")



if __name__ == "__main__":

    show_login()