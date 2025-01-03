import streamlit as st
from streamlit_option_menu import option_menu
import Home, About, account, Dashboard, Chatbot, CommunitySupport, Blogs, Virtual_Meetings
import Push_Ups, Reps, Forward_Lunges, Reverse_Lunges, Full_Plank, Elbow_Plank

st.set_page_config(
    page_title="TrackiT - Fitness Revolution",
    layout="wide",
)

logo_icon = 'static/images/track3.jpg'
st.sidebar.image(logo_icon, width=180)

st.sidebar.markdown(
    """
    <style>
        .trackit-text {
            font-size: 45px;
            font-weight: bold;
            font-family: sans-serif;
            background: linear-gradient(to right, #9C27B0, rgb(64, 231, 253));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: relative;
            z-index:-10;
            top:-20px;
        }
    </style>
    <div class="trackit-text">TrackiT</div>
    """,
    unsafe_allow_html=True
)

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_apps(self, title, func, require_login=False, require_premium=False):
        self.apps.append({
            "title": title,
            "function": func,
            "require_login": require_login,
            "require_premium": require_premium
        })

    def run(self):
        with st.sidebar:
            main_menu = option_menu(
                menu_title="Features", 
                options=["Home", "About", "Account", "Dashboard", "Chatbot", "Community Support", "Blogs", "Virtual Meetings", "Exercises"],
                icons=["house", "info", "key", "list-task", "robot", "person", "pencil", "camera", "zap"],
                menu_icon="star", 
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#ebe8e8"},
                    "icon": {"color": "black", "font-size": "16px"},
                    "nav-link": {"color": "black", "font-size": "16px"},
                    "nav-link:hover": {"background-color": "gray"},
                    "nav-link-selected": {"background-color": "skyblue"},
                }
            )

        if main_menu == "Exercises":
            exercise_option = st.selectbox("Select an Exercise", ["Push-Up", "Forward Lunges", "Reverse Lunges", "Full Plank", "Elbow Plank","Reps"])
            
            if not st.session_state.get("logged_in", False):
                st.error("You must be logged in to access these exercises.")
                return
            
            if st.session_state.get("access_level") != "premium":
                st.error("Only Premium users can access these exercises. Please upgrade your subscription.")
                return
            
            if exercise_option == "Push-Up":
                Push_Ups.app()
            elif exercise_option == "Forward Lunges":
                Forward_Lunges.app()
            elif exercise_option == "Reverse Lunges":
                Reverse_Lunges.app()
            elif exercise_option == "Full Plank":
                Full_Plank.app()
            elif exercise_option == "Elbow Plank":
                Elbow_Plank.app()
            elif exercise_option == "Reps":
                Reps.app()

        else:
            for app in self.apps:
                if main_menu == app["title"]:
                    if app["require_login"] and not st.session_state.get("logged_in", False):
                        st.error("You must be logged in to access this page.")
                        return
                    
                    if app["require_premium"] and st.session_state.get("access_level") != "premium":
                        st.error("This feature is only available for Premium users. Please upgrade your subscription.")
                        return
                    
                    app["function"]()

multiapp = MultiApp()
multiapp.add_apps("Home", Home.run)
multiapp.add_apps("About", About.run)
multiapp.add_apps("Account", account.run)
multiapp.add_apps("Dashboard", Dashboard.app, require_login=True, require_premium=True)
multiapp.add_apps("Chatbot", Chatbot.app, require_login=True, require_premium=True)
multiapp.add_apps("Community Support", CommunitySupport.app, require_login=True)
multiapp.add_apps("Blogs", Blogs.app, require_login=True)
multiapp.add_apps("Virtual Meetings", Virtual_Meetings.app, require_login=True, require_premium=True)

multiapp.run()