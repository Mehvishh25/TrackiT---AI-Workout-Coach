import streamlit as st
import Forward_Lunges_backend

def app():
    st.markdown(
        """
        <h1 style="color:#05757d;">Forward Lunges Tracker</h1>
        """, unsafe_allow_html=True)
    st.markdown(
        """
        <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="font-size: 18px; color:#05757d; font-weight: bold;">Real-Time Forward Lunges Tracker</h3>
            <p style="font-size: 16px; color: #666;">
                Track your Forward Lunges in real time. Perform lunges in front of your webcam, and let the AI count your lunges and analyze your form live!
            </p>
        </div>
        """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        # Tips Section
        st.markdown(
            """
            <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; height: 100%;">
                <h4 style="font-size: 18px; font-weight: bold; color:#05757d;">Tips for Perfect Forward Lunges</h4>
                <ul style="font-size: 16px; color: #666;">
                   <li>Proper Step: Step forward with a long stride, ensuring that your back knee nearly touches the ground while your front knee stays over your ankle (not extending beyond your toes).</li>
                    <li>Chest Up: Keep your chest lifted and shoulders back to maintain a strong, upright posture.</li>
                    <li>Engage Your Core: Tighten your core to maintain balance and stability throughout the movement.</li>
                    <li>Push from Your Heel: Push back up through the heel of your front foot to return to the standing position.</li>
                    <li>Controlled Movement: Perform the lunge with controlled movement—don’t rush through the exercise.</li>
                </ul>
                <p style="font-size: 15px; color: #666;padding-left:20px"><i>Real-time analysis will be displayed as you exercise.</i></p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; height: 100%;">
                <h4 style="font-size: 16px; font-weight: bold; color:#05757d;">Forward Lunges Tutorial</h4>
                <div style="text-align: center;">
                    <img src="https://img.youtube.com/vi/MxfTNXSFiYI/hqdefault.jpg" class="video-thumbnail" style="width: 100%; height: auto; border-radius: 10px; margin-bottom: 10px;" />
                    <a href="https://www.youtube.com/watch?v=MxfTNXSFiYI" target="_blank" class="video-title" style="font-size: 14px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; margin-top: 10px;">Forward Lunges Tutorial</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        """
        <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-top: 20px;">
            <h4 style="font-size: 18px; font-weight: bold; color:#05757d;">How to Perform Forward Lunges in Front of the Camera</h4>
            <ul style="font-size: 16px; color: #666;">
                <li>Stand tall with your feet hip-width apart.</li>
                <li>Ensure your camera captures your full body and the lunge motion.</li>
                <li>Ensure you are facing left or right.</li>
                <li>Maintain proper form and steady movement as you step forward and lower your body into a lunge.</li>
            </ul>
            <p style="font-size: 14px; color: #666;">You can start real-time tracking by facing the camera and performing the lunge.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown(
        """
        <h4 style="font-size: 16px; font-weight: bold; color:#05757d;">Select Your Lunge Level</h4>
        """, unsafe_allow_html=True)

    level = st.selectbox("Choose your level:", options=["Beginner", "Intermediate", "Advanced"])

    if level == "Beginner":
        lunge_target = "You should perform 10-15 lunges (5-7 per leg)."
    elif level == "Intermediate":
        lunge_target = "You should perform 20-30 lunges (10-15 per leg)."
    else:
        lunge_target = "You should perform 40-50 lunges (20-25 per leg)."

    st.markdown(f"""
        <h5 style="font-size: 16px; font-weight: bold; color: #333; margin-top: 10px;">Lunge Targets by Level:</h5>
        <p style="font-size: 16px; color: #666;">
            {lunge_target}
        </p>
        """, unsafe_allow_html=True)

    # Always display the buttons
    start_coach_button = st.button("Start Virtual Coach")
    stop_coach_button = st.button("Stop Virtual Coach")

    # Update session state based on button clicks
    if start_coach_button:
        st.session_state.start_coach = True
        Forward_Lunges_backend.process_video()

    if stop_coach_button:
        st.session_state.start_coach = False
        Forward_Lunges_backend.stop_video()

if __name__== "_main":
    app()