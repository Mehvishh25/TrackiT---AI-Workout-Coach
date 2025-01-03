import streamlit as st

def app():
    st.markdown("""
        <div style=" padding: 10px; border-radius: 15px; text-align: center;">
            <h3 style="font-size: 60px; font-weight: bold; margin-bottom: 0;">
                <span style="color: #0c9c95;">Schedule Your Virtual Meeting</span>
            </h3>
            <p style="font-size: 18px; color: #555; margin-top: 5px;">
                Select a date that works for you and book a 30-minute session.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-top: 30px; text-align: center;">
            <label style="font-size: 20px; color: #0c9c95; font-weight: bold; display: block; margin-bottom: 10px;">
                Choose a date for your meeting:
            </label>
        </div>
    """, unsafe_allow_html=True)

    selected_date = st.date_input("Pick a date for your 30-minute meeting:")

    st.markdown(f"""
        <div style="background-color: #e8f5f4; padding: 15px; border-radius: 10px; text-align: center; margin-top: 20px;">
            <p style="font-size: 18px; color: #0c9c95; margin: 0;">
                You have selected:
            </p>
            <h4 style="font-size: 24px; color: #49075e; margin: 5px 0;">
                {selected_date}
            </h4>
            <p style="font-size: 16px; color: #555;">
                ⏱<em>30 min meet</em>
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-top: 40px; text-align: center; color: #777;">
            <p>Need help scheduling? Contact us at <span style="color: #0c9c95;">support@trackit.com</span></p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "_main_":
    app()