import streamlit as st
import Full_plank_backend

def app():
    st.markdown(
        """
        <h1 style="color:#05757d;">Full Plank Tracker</h1>
        """, unsafe_allow_html=True)

    # Real-Time Reps Tracker Description
    st.markdown(
        """
        <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="font-size: 18px; color: #05757d; font-weight: bold;">Real-Time Full Plank Tracker</h3>
            <p style="font-size: 16px; color: #666;">
                Track your exercise repetitions in real time. Perform your workout in front of the webcam, and let the AI count your plank live!
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Tips for Perfect Reps with Video Link
    # Tips and Video side by side
    col1, col2 = st.columns(2)

    with col1:
        # Tips Section
        st.markdown(
            """
            <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; height: 100%;">
                <h4 style="font-size: 18px; font-weight: bold; color:#05757d;">Tips for Perfect Elbow Plank</h4>
                <ul style="font-size: 16px; color: #666;">
                    <li>Maintain a Straight Line.</li>
                    <li> Tighten your abdominal muscles and squeeze your glutes to activate your core.</li>
                    <li>Position your elbows directly under your shoulders to ensure proper alignment.</li>
                    <li>Rest Between Sets: Allow yourself enough rest between sets to recover fully, depending on your fitness level.</li>
                    <li>Breathing: Ensure you breathe steadily—inhale during the relaxation phase and exhale during the exertion phase.</li>
                </ul>
                <p style="font-size: 15px; color: #666; padding-left:20px"><i>Real-time analysis will be displayed as you exercise.</i></p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        # Video Section with same size as col1
        st.markdown(
            """
            <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; height: 100%;">
                <h4 style="font-size: 16px; font-weight: bold; color: #05757d;">Elbow Plank Tutorial</h4>
                <div style="text-align: center;">
                    <img src="https://img.youtube.com/vi/B296mZDhrP4/hqdefault.jpg" class="video-thumbnail" style="width: 100%; height: auto; border-radius: 10px; margin-bottom: 10px;" />
                    <a href="https://www.youtube.com/watch?v=B296mZDhrP4" target="_blank" class="video-title" style="font-size: 14px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; margin-top: 10px;">Reps Tutorial</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # How to Perform Reps in Front of the Camera
    st.markdown(
        """
        <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-top: 20px;">
            <h4 style="font-size: 18px; font-weight: bold; color:#05757d;">How to Perform Reps in Front of the Camera</h4>
            <ul style="font-size: 16px; color: #666;">
                <li>Face left or right to the camera, ensuring the camera can capture your movement clearly.</li>
                <li>Start the virtual coach to begin counting your reps.</li>
                <li>Perform the exercise.</li>
                <li>Maintain a neutral neck position.</li>
            </ul>
            <p style="font-size: 14px; color: #666;">You can start real-time tracking by facing the camera.</p>
        </div>
        """, unsafe_allow_html=True)

    # Select Your Exercise Type
    st.markdown(
        """
        <h4 style="font-size: 16px; font-weight: bold; color:#05757d;">Select Your Exercise</h4>
        """, unsafe_allow_html=True)

    # Dropdown for selecting exercise
    level = st.selectbox("Choose your level:", options=["Beginner", "Intermediate", "Advanced"])

    if level == "Beginner":
        target = "You should perform 2-3 sets for 10-20 seconds per set"
    elif level == "Intermediate":
        target = "You should perform 3-4 sets for 30-45 seconds per set"
    else:
        target = "You should perform 4-5 sets for 1 minute per set"

    st.markdown(f"""
        <h5 style="font-size: 18px; font-weight: bold; color: #333; margin-top: 10px;">Target for {level}:</h5>
        <p style="font-size: 16px; color: #666;">
            {target}
        </p>
        """, unsafe_allow_html=True)

    # Always display the buttons
    start_coach_button = st.button("Start Virtual Coach")
    stop_coach_button = st.button("Stop Virtual Coach")

    # Update session state based on button clicks
    if start_coach_button:
        st.session_state.start_coach = True
        Full_plank_backend.process_video(level)

    if stop_coach_button:
        st.session_state.start_coach = False
        Full_plank_backend.stop_video()

if __name__== "_main":
    app()