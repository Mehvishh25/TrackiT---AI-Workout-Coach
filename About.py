import streamlit as st
def run():
    st.markdown(
        """
        <h1 style='font-size:60px;#background: linear-gradient(to right, skyblue, purple)'><span style='background: linear-gradient(to right, #09ebd0, #49075e);-webkit-background-clip: text;-webkit-text-fill-color: transparent;'> TrackiT</span></h1>
        <h3 style='color:#0c9c95;'> Your AI-Powered Workout Partner 🏋‍♂</h3>
        """,unsafe_allow_html=True
    )
    st.image("static/images/aifitness.png", use_container_width=True)
    st.markdown("""
        <style>
            .stImage img {
                border-radius: 15px;
                width: 100%;
                max-width: 1000px;
            }
        </style>
    """, unsafe_allow_html=True)
    
    
    st.markdown("""
        <div style="padding: 20px;">
        <p style="text-align: center; font-size: 20px; margin: 0 0 20px;">
            <span style="color: #0c9c95;"><b>TrackiT</b></span> harnesses the power of advanced AI and computer vision to revolutionize your fitness journey with innovative features:
        </p>
        <div style="display: flex; flex-wrap: wrap; gap: 15px; justify-content: space-between;">
            <div style="flex: 1 1 calc(33% - 15px); background: #ffffff; border: 2px solid #0c9c95; border-radius: 10px; padding: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); min-width: 250px;">
                <strong style="color: #0c9c95; font-size:18px">Real-Time Posture Monitoring:</strong> 
                <p  style='font-size:17px'>Ensures proper form by detecting incorrect postures, offering immediate corrections, tracking movements, and counting sets for safer and more consistent workouts.</p>
            </div>
            <div style="flex: 1 1 calc(33% - 15px); background: #ffffff; border: 2px solid #0c9c95; border-radius: 10px; padding: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); min-width: 250px;">
                <strong style="color: #0c9c95;font-size:18px">Performance Analytics at a Glance:</strong> 
                <p  style='font-size:17px'>Visualize your workout progress with an intuitive dashboard that highlights trends and improvements over time.</p>
            </div>
            <div style="flex: 1 1 calc(33% - 15px); background: #ffffff; border: 2px solid #0c9c95; border-radius: 10px; padding: 15px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); min-width: 250px;">
                <strong style="color: #0c9c95;font-size:18px">Personalized Workout Guidance:</strong> 
                <p style='font-size:17px'>Receive tailored exercise recommendations based on your performance, joint angles, and progress history, ensuring routines that adapt to your needs.</p>
            </div>
        </div>
        <hr style="border: 1px solid #ddd; margin: 20px 0;">
        <p style="text-align: center; font-size: 20px;">
            Take your fitness goals to the next level with - <span style="color: #0c9c95;">TrackiT</span> – your intelligent workout coach.
        </p>
    </div>

         
        """
        ,unsafe_allow_html=True
    )