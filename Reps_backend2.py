import cv2
import numpy as np
import mediapipe as mp
import time
import Pose_module as pm
import streamlit as st

class VideoProcessor:
    def __init__(self):
        self.cap = None
        self.detector = pm.poseDectector()
        self.count = 0
        self.dir = 0
        self.pTime = 0

    def start_processing(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 1280)
        self.cap.set(4, 760)
        frame_placeholder = st.empty()

        while self.cap.isOpened() and st.session_state.start_coach:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = self.detector.findPose(frame)
            lmList = self.detector.getPositions(frame, False)

            if len(lmList) != 0:
                angle = self.detector.findAngle(frame, 11, 13, 15)

                angle_range = (15, 190)
                reversed_range = angle_range[::-1]
                per_range = (0, 100)
                per_reverse = per_range[::-1]
                per = np.interp(angle, angle_range, per_reverse)

                if np.isnan(per):
                    per = 0 

                if 95 <= per <= 100 and self.dir == 0:
                    self.count += 0.5
                    self.dir = 1

                if 0 <= per <= 5 and self.dir == 1:
                    self.count += 0.5
                    self.dir = 0

                # Display completion message when count reaches 10
                if self.count >= 5.5:
                    st.success("🎉 Congratulations! You've completed today's exercise!")
                    st.balloons()
                    self.stop_processing()
                    break

                cv2.putText(frame, f'{int(per)}%', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 4)
                cv2.putText(frame, f'Total: {str(self.count)}', (40, 670), cv2.FONT_HERSHEY_PLAIN, 4, (255, 0, 0), 5)

            cTime = time.time()
            fps = 1 / (cTime - self.pTime)
            self.pTime = cTime
            cv2.putText(frame, f'FPS: {str(int(fps))}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

            frame_placeholder.image(frame, channels="BGR", use_container_width=True)

    def stop_processing(self):
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()

# Create an instance of VideoProcessor
video_processor = VideoProcessor()

def process_video():
    video_processor.start_processing()

def stop_video():
    video_processor.stop_processing()

if __name__ == "__main__":
    st.title("Personal Exercise Coach")
    
    if st.button("Start Exercise"):
        st.session_state.start_coach = True
        process_video()

    if st.button("Stop Exercise"):
        st.session_state.start_coach = False
        stop_video()
