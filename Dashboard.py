import streamlit as st
from datetime import datetime
import plotly.express as px
import pandas as pd

def app():
    # Dashboard Title
    st.markdown("""
        <div>
            <h1 style='background: linear-gradient(to right, #09ebd0, #49075e); -webkit-background-clip: text; -webkit-text-fill-color: transparent'>Dashboard</h1>
        </div>
    """, unsafe_allow_html=True)

    # Two columns for inputs
    col1, col2 = st.columns(2,gap='large')
    
    # Select Time Frame
    with col1:
        time_frame = st.selectbox("Time Frame", ["Daily", "Weekly", "Monthly"])

    # Chart Type (Static Text)
    with col2:
        st.write("Chart Type: Bar")
    
    # Date Input Based on Time Frame
    st.markdown("---")  # Horizontal line for separation
    
    if time_frame == "Daily":
        date = st.date_input("Select Date:", datetime.now())
        st.subheader("📊 Daily Analysis")
        st.write(f"Analysis for: **{date.strftime('%B %d, %Y')}**")
        st.write("""
            - **Number of Reps:** 10
            - **Number of Push-Ups:** 20
            - **Number of Forward Lunges:** 15
            - **Number of Reverse Lunges:** 15
            - **Number of Full Plank:** 2
            - **Number of Elbow Plank:** 3
        """)
        # Sample Data
        data = {
            'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
            'Values': [10, 20, 15, 15, 2, 3]
        }

        # Create Bar Chart using Plotly
        fig = px.bar(data, x='Categories', y='Values', title="Daily Analysis", color_discrete_sequence=["green"])

        # Display in Streamlit
        st.plotly_chart(fig)

    elif time_frame == "Weekly":
        start_date = st.date_input("Select Start Date:", datetime.now())
        end_date = st.date_input("Select End Date:", datetime.now())
        st.subheader("📅 Weekly Analysis")
        st.write(f"Analysis from **{start_date.strftime('%B %d, %Y')}** to **{end_date.strftime('%B %d, %Y')}**")
        st.write("""
            - **Number of Reps:** 75
            - **Number of Push-Ups:** 150
            - **Number of Forward Lunges:** 90
            - **Number of Reverse Lunges:** 85
            - **Number of Full Plank:** 10
            - **Number of Elbow Plank:** 15
        """)
        # Bar Chart for Weekly Analysis
        weekly_data = {
            "Monday": [10, 20, 15, 15, 2, 3],
            "Tuesday": [12, 25, 18, 15, 3, 4],
            "Wednesday": [15, 30, 20, 18, 4, 5],
            "Thursday": [10, 22, 16, 14, 2, 3],
            "Friday": [13, 27, 17, 15, 3, 4],
            "Saturday": [14, 28, 19, 17, 4, 5],
            "Sunday": [16, 32, 20, 18, 4, 5],
        }
        weekly_df = pd.DataFrame(weekly_data, index=['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'])
        st.bar_chart(weekly_df)
        col3,col4=st.columns(2)
        col5,col6=st.columns(2)
        col7,col8,col9=st.columns(3)

        with col3:
            data = {
            'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
            'Values': [10, 20, 15, 15, 2, 3]
            }

            # Create Bar Chart using Plotly
            fig = px.bar(data, x='Categories', y='Values',title="Monday", color_discrete_sequence=["red"])

            # Display in Streamlit
            st.plotly_chart(fig)

        with col4:
            data = {
            'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
            'Values': [12, 25, 18, 15, 3, 4]
            }

            # Create Bar Chart using Plotly
            fig = px.bar(data, x='Categories', y='Values',title="Tuesday", color_discrete_sequence=["yellow"])

            # Display in Streamlit
            st.plotly_chart(fig)

        with col5:
            data = {
            'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
            'Values': [15, 30, 20, 18, 4, 5]
            }

            # Create Bar Chart using Plotly
            fig = px.bar(data, x='Categories', y='Values', title="Wednesday", color_discrete_sequence=["purple"])

            # Display in Streamlit
            st.plotly_chart(fig)

        with col6:
            data = {
            'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'], 
            'Values': [10, 22, 16, 14, 2, 3]
            }
            fig = px.bar(data, x='Categories', y='Values', title="Thursday", color_discrete_sequence=["green"])
            st.plotly_chart(fig)

        with col7:
            data = {
            'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
            'Values': [13, 27, 17, 15, 3, 4]
            }
            fig = px.bar(data, x='Categories', y='Values', title="Friday", color_discrete_sequence=["blue"])
            st.plotly_chart(fig)

        with col8:
            data = {
            'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
            'Values': [14, 28, 19, 17, 4, 5]
            }
            fig = px.bar(data, x='Categories', y='Values', title="Saturday", color_discrete_sequence=["pink"])
            st.plotly_chart(fig)

        with col9:
            data = {
            'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
            'Values': [16, 32, 20, 18, 4, 5]
            }
            fig = px.bar(data, x='Categories', y='Values', title="Sunday", color_discrete_sequence=["orange"])
            st.plotly_chart(fig)

    elif time_frame == "Monthly":
        st.selectbox("Select Month", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
        st.subheader("📆 Monthly Analysis")
        st.write("""
            - **Number of Reps:** 290
            - **Number of Push-Ups:** 500
            - **Number of Forward Lunges:** 350
            - **Number of Reverse Lunges:** 340
            - **Number of Full Plank:** 45
            - **Number of Elbow Plank:** 50
        """)
        monthly_data = {
        'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Reps': [290, 310, 320, 290, 330, 350, 340, 330, 360, 350, 370, 380],
        'Push-Ups': [500, 550, 570, 480, 510, 530, 550, 560, 590, 600, 610, 630],
        'Forward Lunges': [350, 370, 360, 340, 355, 380, 375, 380, 390, 400, 410, 420],
        'Reverse Lunges': [340, 360, 350, 330, 345, 360, 370, 380, 390, 400, 410, 420],
        'Full Plank': [45, 50, 52, 45, 48, 50, 53, 55, 60, 62, 65, 68],
        'Elbow Plank': [50, 55, 60, 52, 56, 58, 60, 62, 64, 66, 68, 70]
        }

        monthly_df = pd.DataFrame(monthly_data)

        # To visualize as a bar chart
        fig = px.bar(monthly_df, x='Month', y=['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges', 'Full Plank', 'Elbow Plank'],
                    title="Monthly Exercise Data", labels={"value": "Count", "variable": "Exercise Type"})
        st.plotly_chart(fig)

        col10,col11=st.columns(2)
        col12,col13=st.columns(2)
        col14,col15=st.columns(2)
        col16,col17=st.columns(2)
        col18,col19=st.columns(2)
        col20,col21=st.columns(2)

        with col10:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [290, 500, 350, 340, 45, 50]
            }
            fig = px.bar(data, x='Categories', y='Values', title="January", color_discrete_sequence=["purple"])
            st.plotly_chart(fig)

        with col11:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [310, 550, 370, 360, 50, 55]
            }
            fig = px.bar(data, x='Categories', y='Values', title="February", color_discrete_sequence=["yellow"])
            st.plotly_chart(fig)

        with col12:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [320, 570, 360, 350, 52, 60]
            }
            fig = px.bar(data, x='Categories', y='Values', title="March", color_discrete_sequence=["blue"])
            st.plotly_chart(fig)

        with col13:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [290, 480, 340, 330, 45, 52]
            }
            fig = px.bar(data, x='Categories', y='Values', title="April", color_discrete_sequence=["green"])
            st.plotly_chart(fig)

        with col14:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [330, 510, 355, 345, 48, 56]
            }
            fig = px.bar(data, x='Categories', y='Values', title="May", color_discrete_sequence=["pink"])
            st.plotly_chart(fig)

        with col15:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [350, 530, 380, 360, 50, 58]
            }
            fig = px.bar(data, x='Categories', y='Values', title="June", color_discrete_sequence=["red"])
            st.plotly_chart(fig)

        with col16:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [340, 550, 375, 370, 53, 60]
            }
            fig = px.bar(data, x='Categories', y='Values', title="July", color_discrete_sequence=["orange"])
            st.plotly_chart(fig)

        with col17:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [330, 560, 380, 380, 55, 62]
            }
            fig = px.bar(data, x='Categories', y='Values', title="August", color_discrete_sequence=["blue"])
            st.plotly_chart(fig)

        with col18:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [360, 590, 390, 390, 60, 64]
            }
            fig = px.bar(data, x='Categories', y='Values', title="September", color_discrete_sequence=["green"])
            st.plotly_chart(fig)

        with col19:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [350, 600, 400, 400, 62, 66]
            }
            fig = px.bar(data, x='Categories', y='Values', title="October", color_discrete_sequence=["yellow"])
            st.plotly_chart(fig)

        with col20:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [370, 610, 410, 410, 65, 68]
            }
            fig = px.bar(data, x='Categories', y='Values', title="November", color_discrete_sequence=["red"])
            st.plotly_chart(fig)

        with col21:
            data = {
                'Categories': ['Reps', 'Push-Ups', 'Forward Lunges', 'Reverse Lunges','Full Plank','Elbow Plank'],
                'Values': [380, 630, 420, 420, 68, 70]
            }
            fig = px.bar(data, x='Categories', y='Values', title="December", color_discrete_sequence=["orange"])
            st.plotly_chart(fig)        

if __name__ == "__main__":
    app()
