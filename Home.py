import streamlit as st
if "screen_width" not in st.session_state:
    st.session_state["screen_width"] = 768  

def free_access():
    st.markdown("### Free Access Features")
    st.markdown(
        """
        <ul>
            <li>Community Support</li>
            <li>Access to Blogs</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )
def premium_access():
    st.markdown("### Premium Access Features")
    st.markdown(
        """
        <ul>
            <li>AI-Driven Workouts</li>
            <li>Real-Time Posture Monitoring</li>
            <li>Progress Tracking</li>
            <li>Engaging Community</li>
        </ul>
        """,
        unsafe_allow_html=True,
    )
def run():
    st.markdown(
        "<h1 style='font-size:60px;background: linear-gradient(to right, #09ebd0, #49075e);-webkit-background-clip: text;-webkit-text-fill-color: transparent;'>Welcome to TrackiT</h1>",
        unsafe_allow_html=True,
    )
    st.markdown("<h3>Your AI Workout Coach</h3>", unsafe_allow_html=True)
    st.image("static/images/bgAi.webp", use_container_width=True)

    st.markdown(
        """
        <p style="font-size: 17px;">
            At TrackiT, we’re revolutionizing the fitness experience by combining cutting-edge AI and personalized guidance, allowing you to work out smarter and more effectively.
        </p>
        <h2 style="font-size: 30px; color: #0c9c95;">Features of TrackiT:</h2>
        <ul style="font-size: 18px;">
            <li><b>AI-Driven Workouts</b></li>
            <li><b>Real-Time Posture Monitoring</b></li>
            <li><b>Progress Tracking</b></li>
            <li><b>Engaging Community</b></li>
        </ul>
        <div style='background: linear-gradient(to right,#05bff2, #b405ff);padding-bottom:2px;border-radius:10px;margin-top:20px'>
        <h2 style="font-size: 30px; color: white;text-align:center">Join the Fitness Revolution with TrackiT!</h2>
        <p style="font-size: 20px;text-align:center; color:white">
            Step into a smarter way to train. Whether you’re looking to lose weight, build muscle, or increase endurance, TrackiT has you covered. Let’s unlock your potential together!
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style='margin-top:50px;background: linear-gradient(to right, #9c27b0, #ff4081);padding:1px;border-radius:10px;margin-bottom:20px'>
            <h3 style='color:#3b1757;text-align:center;'>Free Access</h3>
            <p style="font-size: 16px;text-align:center;color:white">Get access to community support, blogs, and essential pages like Home, About, and Account.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Access Free Features"):
            st.session_state["access_level"] = "free"

    with col2:
        st.markdown(
            """
            <div style='background:linear-gradient(to right, #00bfae, #f3d200);padding:1px;margin-top:50px;border-radius:10px;margin-bottom:20px'>
            <h3 style='color: #004d40;text-align:center;'>Premium Access</h3>
            <p style="font-size: 16px;text-align:center;color:white">Unlock all features, including AI-driven workouts, real-time monitoring, and advanced tracking.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Access Premium Features"):
            st.session_state["access_level"] = "premium"

    if "access_level" in st.session_state:
        if st.session_state["access_level"] == "free":
            free_access()
        elif st.session_state["access_level"] == "premium":
            premium_access()
    st.markdown("""<hr style="border: 1px solid #fff; margin-top:100px ;">""",unsafe_allow_html=True)
    def render_footer():
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

        with col1:
            st.markdown(
                """
                <div >
                    <h3>TrackiT</h3>
                    <p>Your AI Gym Trainer</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col2:
            st.markdown(
                """
                <div>
                    <h3 style='margin-left:15px'>Services</h3>
                    <ul style="list-style-type: none">
                        <li>Chatbot </li>
                        <li>Dashboard</li>
                        <li>Virtual Meetings</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col3:
            st.markdown(
                """
                <div>
                    <h3>Company</h3>
                    <ul style="list-style-type: none; padding: 0;">
                        <li>Home</li>
                        <li>About Us</li>
                        <li>Privacy Policy</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col4:
            st.markdown(
                """
                <div>
                    <h3>Contact</h3>
                    <ul style="list-style-type: none; padding: 0;">
                        <li>Gmail</li>
                        <li>LinkedIn</li>
                        <li>Facebook</li>
                        <li>Instagram</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True,
            )

    render_footer()
    st.markdown("""<hr style="border: 1px solid #ddd;">""",unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center;  color: #555; font-size: 15px;">
            &copy; 2025 TrackiT. All rights reserved.
        </div>
        """,
        unsafe_allow_html=True,
    )
if __name__ == "_main_":
    if "access_level" not in st.session_state:
        st.session_state["access_level"] = None
    run()