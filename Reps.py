import streamlit as st
import Reps_backend2

def app():
    st.markdown(
        """
        <h1 style="color:#05757d;">Reps Tracker</h1>
        """, unsafe_allow_html=True)

    # Real-Time Reps Tracker Description
    st.markdown(
        """
        <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="font-size: 18px; color: #05757d; font-weight: bold;">Real-Time Reps Tracker</h3>
            <p style="font-size: 16px; color: #666;">
                Track your exercise repetitions in real time. Perform your workout in front of the webcam, and let the AI count your reps live!
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
                <h4 style="font-size: 18px; font-weight: bold; color:#05757d;">Tips for Perfect Reps</h4>
                <ul style="font-size: 16px; color: #666;">
                    <li>Start Slow: Start with a lower number of reps and gradually increase the intensity as you build strength and endurance.</li>
                    <li>Form is Key: Focus on maintaining good form to prevent injuries and maximize effectiveness.</li>
                    <li>Rest Between Sets: Allow yourself enough rest between sets to recover fully, depending on your fitness level.</li>
                    <li>Consistency Over Intensity: Focus on consistent training and proper technique rather than going for maximum intensity too soon.</li>
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
                <h4 style="font-size: 16px; font-weight: bold; color: #05757d;">Reps Tutorial</h4>
                <div style="text-align: center;">
                    <img src="https://img.youtube.com/vi/RcC2JEWfldE/hqdefault.jpg" class="video-thumbnail" style="width: 100%; height: auto; border-radius: 10px; margin-bottom: 10px;" />
                    <a href="https://www.youtube.com/watch?v=RcC2JEWfldE" target="_blank" class="video-title" style="font-size: 14px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; margin-top: 10px;">Reps Tutorial</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # How to Perform Reps in Front of the Camera
    st.markdown(
        """
        <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-top: 20px;">
            <h4 style="font-size: 18px; font-weight: bold; color:#05757d;">How to Perform Reps in Front of the Camera</h4>
            <ul style="font-size: 16px; color: #666;">
                <li>Face forward to the camera, ensuring the camera can capture your movement clearly.</li>
                <li>Start the virtual coach to begin counting your reps.</li>
                <li>Perform the exercise, ensuring each rep is full and precise.</li>
                <li>Maintain a steady pace, but avoid rushing the reps for better form.</li>
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
        rep_target = "You should perform 10-15 reps"
    elif level == "Intermediate":
        rep_target = "You should perform 20-30 reps"
    else:
        rep_target = "You should perform 40-50 reps"

    st.markdown(f"""
        <h5 style="font-size: 18px; font-weight: bold; color: #333; margin-top: 10px;">Rep Targets for {level}:</h5>
        <p style="font-size: 16px; color: #666;">
            {rep_target}
        </p>
        """, unsafe_allow_html=True)

    # Always display the buttons
    start_coach_button = st.button("Start Virtual Coach")
    stop_coach_button = st.button("Stop Virtual Coach")

    # Update session state based on button clicks
    if start_coach_button:
        st.session_state.start_coach = True
        Reps_backend2.process_video()

    if stop_coach_button:
        st.session_state.start_coach = False
        Reps_backend2.stop_video()

if __name__== "_main":
    app()