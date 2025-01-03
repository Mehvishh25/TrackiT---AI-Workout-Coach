import streamlit as st

UserInfo = {
    "admin": "password1234",
    "Username": "Password987",
    "tt": "tt"
}

def run():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    st.title("Login")

    if st.session_state.logged_in:
        st.success("Welcome,!")
        st.write("You are logged in. Manage your account here.")
    else:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login", key="login_button"):  
            if username in UserInfo and UserInfo[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login Successful!")
                st.rerun()  
            else:
                st.error("Invalid username or password.")