import cv2
import mediapipe as mp
import numpy as np
import time
import Pose_module as pm
import pyttsx3
import streamlit as st

class VideoProcessor:
    def __init__(self):
        self.cap = None
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.detector = pm.poseDectector()
        self.count = 0
        self.dir = 0
        self.feedback_shown_time = 0
        self.message_shown1 = False
        self.message_shown2 = False
        self.pTime = 0

    def speak_message(self, message):
        engine = pyttsx3.init()  # Initialize engine within the function
        engine.say(message)
        engine.runAndWait()
        engine.stop()  # Stop the engine after speaking

    def start_processing(self):
        self.cap = cv2.VideoCapture('videos/pushups2.mp4')
        frame_placeholder = st.empty()

        while self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break

            #frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = self.pose.process(frame_rgb)
            frame = self.detector.findPose(frame)
            lmList = self.detector.getPositions(frame, False)

            if result.pose_landmarks:
                landmarks = result.pose_landmarks.landmark
                direction = "Facing Forward"
                if len(lmList) != 0:
                    angle1 = self.detector.findAngle(frame, 11, 13, 15)
                    angle2 = self.detector.findAngle(frame, 12, 14, 16)
                    per1 = np.interp(angle1, (180, 290), (0, 100))
                    angle_range2 = (90, 170)
                    per2 = np.interp(angle2, angle_range2[::-1], (0, 100)[::-1])

                    if 95 <= per1 <= 100 and 95 <= per2 <= 100 and self.dir == 0:
                        self.count += 0.5
                        self.dir = 1

                        if angle1 < 90 and (not self.message_shown1 or time.time() - self.feedback_shown_time > 2):
                            self.speak_message('Bring your chest closer to the ground while keeping your shoulders stable.')
                            self.message_shown1 = True
                            cv2.putText(frame, 'Bring your chest closer to the ground while keeping your shoulders stable.', (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
                            self.feedback_shown_time = time.time()
                        elif angle1 > 90 and (not self.message_shown2 or time.time() - self.feedback_shown_time > 2):
                            self.speak_message('Keep your shoulders stable and avoid letting them dip too far forward.')
                            self.message_shown2 = True
                            cv2.putText(frame, 'Keep your shoulders stable and avoid letting them dip too far forward.', (10, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
                            self.feedback_shown_time = time.time()

                    if time.time() - self.feedback_shown_time > 2:
                        self.message_shown1 = False
                        self.message_shown2 = False

                    if 0 <= per1 <= 5 and 0 <= per2 <= 5 and self.dir == 1:
                        self.count += 0.5
                        self.dir = 0

                    cv2.putText(frame, f'Direction: {direction}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame, f'Count: {self.count}', (450, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

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
    process_video()
