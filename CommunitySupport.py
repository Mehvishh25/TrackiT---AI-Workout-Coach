import streamlit as st
import streamlit.components.v1 as components

def app():
    
    st.markdown("""
        <style>
            * {
                box-sizing: border-box;
            }

            .feature-container {
                display: flex;
                flex-wrap: wrap;
                justify-content: space-evenly;
                gap: 20px;
            }

            .feature-box {
                border:none;
                border-radius: 10px;
                padding: 20px;
                text-align: center;
                box-shadow: 8px 8px 15px rgba(0, 0, 0, 0.2); 
                box-sizing: border-box;
                flex: 1 1 100%;  /* Default to 100% width */
            }

            @media (min-width: 1400px) {
                .feature-box {
                    flex: 1 1 23%; /* 4 boxes per row */
                }
            }

            @media (max-width: 1399px) {
                .feature-box {
                    flex: 1 1 48%; /* 2 boxes per row */
                }
            }

            @media (max-width: 480px) {
                .feature-box {
                    flex: 1 1 100%; /* 1 box per row */
                }
            }
        </style>
        <div style='background: linear-gradient(to right, #dcf9fc, #fcdcef); padding:10px; border-radius: 10px; margin-bottom: 20px;'>
            <h2 style="font-size: 30px; color:#025c75; text-align:center">Welcome to the TrackiT Community!</h2>
            <p style="font-size: 17px;color:#025c75;text-align:center; padding-left:2px;padding-right:2px">
                At TrackiT, we're not just about workouts — we're about building a supportive community where everyone can grow and achieve their goals together. Whether you're new to fitness or a seasoned athlete, the TrackiT community is here to encourage, motivate, and share knowledge to help you succeed.
            </p>
        </div>
        <h2 style="font-size: 30px; color: #0c9c95; margin-bottom:15px">Why Choose TrackiT?</h2>
        <div class="feature-container">
            <div class="feature-box">
                <h4>Real-Time Assistance</h4>
                <p>With real-time posture correction and performance tracking, you’ll never have to guess if you're doing an exercise right again.</p>
            </div>
            <div class="feature-box">
                <h4>Adaptive Plans</h4>
                <p>As you improve, TrackiT adapts your workout plans to keep challenging you and helping you reach new milestones.</p>
            </div>
            <div class="feature-box">
                <h4>Comprehensive Tools</h4>
                <p>From step-by-step instructions to expert guidance, we offer everything you need to succeed on your fitness journey.</p>
            </div>
            <div class="feature-box">
                <h4>Motivating & Interactive</h4>
                <p>Track your progress, unlock milestones, and stay motivated through gamified features and personalized reminders.</p>
            </div>
        </div>          

        <div style='background: linear-gradient(to right, #e0f7fa, #f1e4f1); padding: 30px; border-radius: 10px; margin-top: 40px;'>
            <h2 style="font-size: 30px; color: #0c9c95; text-align: center; margin-bottom: 20px;">What Our Members Say</h2>
            <div style="display: flex; flex-wrap: wrap; justify-content: space-evenly; gap: 20px;">
                <div style="flex: 1 1 calc(50% - 20px); background-color: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); text-align: center;">
                    <p style="font-size: 16px; color: #333; font-style: italic; margin-bottom: 10px;">"TrackiT has completely transformed my fitness journey!"</p>
                    <p style="font-size: 14px; color: #555;">"As a beginner, I was always unsure if I was doing exercises correctly. With TrackiT's real-time assistance, I can finally feel confident in my workouts. The personalized feedback and progress tracking have kept me motivated every day!"</p>
                    <p style="font-size: 14px; color: #0c9c95; font-weight: bold; margin-top: 10px;">— Sarah L.</p>
                </div>
                <div style="flex: 1 1 calc(50% - 20px); background-color: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); text-align: center;">
                    <p style="font-size: 16px; color: #333; font-style: italic; margin-bottom: 10px;">"A community that truly supports each other."</p>
                    <p style="font-size: 14px; color: #555;">"TrackiT is more than just an app; it's a community. The support and encouragement from other members keep me going even on tough days. Plus, the adaptive plans help me continually challenge myself. Highly recommend!"</p>
                    <p style="font-size: 14px; color: #0c9c95; font-weight: bold; margin-top: 10px;">— James M.</p>
                </div>
                <div style="flex: 1 1 calc(50% - 20px); background-color: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); text-align: center;">
                    <p style="font-size: 16px; color: #333; font-style: italic; margin-bottom: 10px;">"Customized workouts have helped me reach new milestones!"</p>
                    <p style="font-size: 14px; color: #555;">"I've tried many fitness apps, but TrackiT is the best. The adaptive workout plans are tailored to my goals and progress, ensuring I’m always improving. I’ve seen results faster than ever before!"</p>
                    <p style="font-size: 14px; color: #0c9c95; font-weight: bold; margin-top: 10px;">— Emma T.</p>
                </div>
                <div style="flex: 1 1 calc(50% - 20px); background-color: white; border-radius: 10px; padding: 20px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); text-align: center;">
                    <p style="font-size: 16px; color: #333; font-style: italic; margin-bottom: 10px;">"The gamification keeps me motivated!"</p>
                    <p style="font-size: 14px; color: #555;">"I love the interactive features of TrackiT. Unlocking milestones and earning achievements has made my fitness journey feel like a game, and I’m always excited to reach the next level. It's fun, motivating, and keeps me on track!"</p>
                    <p style="font-size: 14px; color: #0c9c95; font-weight: bold; margin-top: 10px;">— Lucas D.</p>
                </div>
            </div>
        </div>
           """,unsafe_allow_html=True)
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
            }
            .faq-section {
                max-width: 900px;
                margin:auto;
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.15);
                border: 2px solid #e0f7fa;
            }
            .faq-title {
                font-size: 26px;
                color: #025c75;
                text-align: center;
                margin-bottom: 25px;
            }
            .faq-item {
                border-bottom: 1px solid #ddd;
                padding: 15px 0;
            }
            .faq-item:last-child {
                border-bottom: none;
            }
            .faq-question {
                font-size: 18px;
                color: #333;
                font-weight: bold;
                cursor: pointer;
            }
            .faq-answer {
                font-size: 16px;
                color: #555;
                margin-top: 10px;
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="faq-section" style='margin-top:20px'>
            <h2 class="faq-title">Frequently Asked Questions</h2>
            <div class="faq-item">
                <div class="faq-question" onclick="toggleAnswer('answer1')">What is TrackiT?</div>
                <div id="answer1" class="faq-answer">TrackiT is an AI-powered gym trainer that helps you improve your workouts with real-time feedback and personalized plans.</div>
            </div>
            <div class="faq-item">
                <div class="faq-question" onclick="toggleAnswer('answer2')">How do I join TrackiT?</div>
                <div id="answer2" class="faq-answer">To join TrackiT, simply sign up on our website or download the app from your app store.</div>
            </div>
            <div class="faq-item">
                <div class="faq-question" onclick="toggleAnswer('answer3')">Is TrackiT free to use?</div>
                <div id="answer3" class="faq-answer">TrackiT offers both free and premium plans, with the premium plan offering advanced features and tailored guidance.</div>
            </div>
            <div class="faq-item">
                <div class="faq-question" onclick="toggleAnswer('answer4')">Can I reset my fitness goals?</div>
                <div id="answer4" class="faq-answer">Yes, you can reset or change your fitness goals anytime to match your progress or preferences.</div>
            </div>
            <div class="faq-item">
                <div class="faq-question" onclick="toggleAnswer('answer5')">What equipment do I need to use TrackiT?</div>
                <div id="answer5" class="faq-answer">You can use TrackiT with or without equipment. The app provides guidance for both types of workouts.</div>
            </div>
            <div class="faq-item">
                <div class="faq-question" onclick="toggleAnswer('answer6')">Does TrackiT work offline?</div>
                <div id="answer6" class="faq-answer">Some features of TrackiT work offline, but real-time feedback and updates require an internet connection.</div>
            </div>
            <div class="faq-item">
                <div class="faq-question" onclick="toggleAnswer('answer7')">How do I contact customer support?</div>
                <div id="answer7" class="faq-answer">You can contact our customer support team via the "Contact Us" page on our website or through the app.</div>
            </div>
        </div>
        <script>
            function toggleAnswer(id) {
                const answer = document.getElementById(id);
                if (answer.style.display === "none" || answer.style.display === "") {
                    answer.style.display = "block";
                } else {
                    answer.style.display = "none";
                }
            }
        </script>
    </body>
    </html>
    """

    components.html(html_code, height=900)

if __name__ == "_main_":
    app()