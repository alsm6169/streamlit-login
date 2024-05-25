import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    if st.session_state.get("logged_in", False):
        st.sidebar.page_link("pages/page1.py", label="Landing Page")
        st.sidebar.page_link("pages/page2.py", label="Backtesting Page")
        st.sidebar.page_link("streamlit_app.py", label="Login Page", disabled=True)


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("streamlit_app.py", label="Login Page", disabled=False)


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "logged_in" not in st.session_state or st.session_state.logged_in is None:
        unauthenticated_menu()
        return
    authenticated_menu()

def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "logged_in" not in st.session_state or st.logged_in.role is None:
        st.switch_page("streamlit_app.py")
    menu()