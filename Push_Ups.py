import streamlit as st
import Push_Ups_backend

def app():
    st.markdown(
        """
        <h1 style="color:#05757d;">Push Ups Tracker</h1>
        """, unsafe_allow_html=True)

    # Initialize session state for start_coach if it doesn't exist
    if "start_coach" not in st.session_state:
        st.session_state.start_coach = False

    # Display session state for debugging purposes
    st.write(f"Start Coach State at the beginning: {st.session_state.start_coach}")  # Debugging

    # Real-Time Push-Up Tracker Description
    st.markdown(
        """
        <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="font-size: 18px; color: #05757d; font-weight: bold;">Real-Time Push-Up Tracker</h3>
            <p style="font-size: 14px; color: #666;">
                Track Push-Ups in Real Time. Perform push-ups in front of your webcam, and let the AI track your posture, count, and form live!
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Tips for a Perfect Push-Up with Video Link
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; height: 100%;">
                <h4 style="font-size: 16px; font-weight: bold; color: #05757d;">Tips for a Perfect Push-Up</h4>
                <ul style="font-size: 14px; color: #666;">
                    <li>Keep your body straight from head to heels.</li>
                    <li>Lower yourself until your chest nearly touches the ground.</li>
                    <li>Keep your elbows at a 45-degree angle to your body.</li>
                    <li>Maintain a controlled and steady motion.</li>
                </ul>
                <p style="font-size: 14px; color: #666;">Real-time analysis will be displayed during the exercise.</p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(
            """
            <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; height: 100%;">
                <h4 style="font-size: 16px; font-weight: bold; color: #05757d;">Push-Up Tutorial</h4>
                <div style="text-align: center;">
                    <img src="https://img.youtube.com/vi/EjEiZZ4VNrE/hqdefault.jpg" class="video-thumbnail" style="width: 100%; height: auto; border-radius: 10px; margin-bottom: 10px;" />
                    <a href="https://www.youtube.com/watch?v=EjEiZZ4VNrE" target="_blank" class="video-title" style="font-size: 14px; font-weight: bold; color: #4f0f62; text-decoration: none; display: block; margin-top: 10px;">Push-Up Tutorial</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        """
        <div style="border: 2px solid #e0e0e0; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-top: 20px;">
            <h4 style="font-size: 16px; font-weight: bold; color: #05757d;">How to Perform Push-Ups in Front of the Camera</h4>
            <ul style="font-size: 14px; color: #666;">
                <li>Face forward to the camera.</li>
                <li>Align your body and ensure the camera can capture your full range of motion.</li>
                <li>Start the virtual coach to begin tracking your form and count.</li>
                <li>Make sure your posture is correct and the camera captures your push-up movement clearly.</li>
            </ul>
            <p style="font-size: 14px; color: #666;">You can start the real-time tracking by facing the camera.</p>
        </div>
        """, unsafe_allow_html=True)

    level = st.selectbox("Choose your level:", options=["Beginner", "Intermediate", "Advanced"])

    if level == "Beginner":
        push_up_count = "You should perform 5-10 push-ups."
    elif level == "Intermediate":
        push_up_count = "You should perform 15-20 push-ups."
    else:
        push_up_count = "You should perform 25-30 push-ups."

    st.markdown(f"""
        <h5 style="font-size: 14px; font-weight: bold; color: #333; margin-top: 10px;">Push-Up Counts by Level:</h5>
        <p style="font-size: 14px; color: #666;">
            {push_up_count}
        </p>
        """, unsafe_allow_html=True)

    # Always display the buttons
    start_coach_button = st.button("Start Virtual Coach")
    stop_coach_button = st.button("Stop Virtual Coach")

    # Update session state based on button clicks
    if start_coach_button:
        st.session_state.start_coach = True
        Push_Ups_backend.process_video()

    if stop_coach_button:
        st.session_state.start_coach = False
        Push_Ups_backend.stop_video()

if __name__ == "__main__":
    app()
