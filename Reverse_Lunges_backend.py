import cv2
import mediapipe as mp
import time
import Pose_module as pm
import pyttsx3
import numpy as np
import streamlit as st

class VideoProcessor:
    def __init__(self):
        self.cap = None
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        self.detector = pm.poseDectector()
        self.count = 0
        self.dir = 0
        self.pTime = 0
        self.feedback_shown_time = 0
        self.message_shown1 = False
        self.message_shown2 = False
        self.message_shown3 = False
        self.message_shown4 = False
        self.message_shown5 = False
        self.message_shown6 = False
        self.message_shown7 = False
        self.message_shown8 = False

        # Initialize pyttsx3 for Text-to-Speech
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)

    def speak_message(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

    def start_processing(self):
        self.cap = cv2.VideoCapture("videos/reverse_lunges_2.mp4")
        frame_placeholder = st.empty()

        while self.cap.isOpened() and st.session_state.start_coach:
            ret, frame = self.cap.read()
            if not ret:
                continue

            #frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = self.pose.process(frame_rgb)

            frame = self.detector.findPose(frame)
            lmList = self.detector.getPositions(frame, False)

            if result.pose_landmarks:
                landmarks = result.pose_landmarks.landmark

                left_shoulder = landmarks[self.mp_pose.PoseLandmark.LEFT_SHOULDER]
                right_shoulder = landmarks[self.mp_pose.PoseLandmark.RIGHT_SHOULDER]
                nose = landmarks[self.mp_pose.PoseLandmark.NOSE]

                midline_x = (left_shoulder.x + right_shoulder.x) / 2
                tolerance = 0.05

                if nose.x < midline_x - tolerance:
                    direction = "Facing Right"
                    if len(lmList) != 0:
                        angle1 = self.detector.findAngle(frame, 23, 25, 27)
                        angle2 = self.detector.findAngle(frame, 24, 26, 28)

                        angle_range1 = (70, 170)
                        reversed_range1 = angle_range1[::-1]
                        per_range1 = (0, 100)
                        per_reverse1 = per_range1[::-1]
                        per1 = np.interp(angle1, angle_range1, per_reverse1)

                        angle_range2 = (70, 170)
                        reversed_range2 = angle_range2[::-1]
                        per_range2 = (0, 100)
                        per_reverse2 = per_range2[::-1]
                        per2 = np.interp(angle2, angle_range2, per_reverse2)

                        if 95 <= per1 <= 100 and 95 <= per2 <= 100 and self.dir == 0:
                            self.count += 0.5
                            self.dir = 1

                            if angle1 > 80:
                                if not self.message_shown5 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('The front knee should bend less')
                                    self.message_shown5 = True
                                    self.feedback_shown_time = time.time()

                            if angle1 < 70:
                                if not self.message_shown6 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('The front knee should bend more')
                                    self.message_shown6 = True
                                    self.feedback_shown_time = time.time()

                            if angle1 > 80:
                                if not self.message_shown7 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('The front knee should bend less')
                                    self.message_shown7 = True
                                    self.feedback_shown_time = time.time()

                            if angle1 < 70:
                                if not self.message_shown8 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('The front knee should bend more')
                                    self.message_shown8 = True
                                    self.feedback_shown_time = time.time()

                        if 0 <= per1 <= 8 and 0 <= per2 <= 8 and self.dir == 1:
                            self.count += 0.5
                            self.dir = 0

                elif nose.x > midline_x + tolerance:
                    direction = "Facing Left"
                    if len(lmList) != 0:
                        angle1 = self.detector.findAngle(frame, 24, 26, 28)
                        angle2 = self.detector.findAngle(frame, 23, 25, 27)

                        per1 = np.interp(angle1, (190, 285), (0, 100))
                        per2 = np.interp(angle1, (190, 285), (0, 100))

                        if 95 <= per1 <= 100 and 95 <= per2 <= 100 and self.dir == 0:
                            self.count += 0.5
                            self.dir = 1

                            if angle1 > 290:
                                if not self.message_shown1 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('The front knee should bend less')
                                    self.message_shown1 = True
                                    self.feedback_shown_time = time.time()

                            if angle1 < 280:
                                if not self.message_shown2 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('The front knee should bend more')
                                    self.message_shown2 = True
                                    self.feedback_shown_time = time.time()

                            if angle1 > 290:
                                if not self.message_shown3 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('The front knee should bend less')
                                    self.message_shown3 = True
                                    self.feedback_shown_time = time.time()

                            if angle1 < 280:
                                if not self.message_shown4 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('The front knee should bend more')
                                    self.message_shown4 = True
                                    self.feedback_shown_time = time.time()

                        if 0 <= per1 <= 8 and 0 <= per2 <= 8 and self.dir == 1:
                            self.count += 0.5
                            self.dir = 0


                else:
                    midline_y = (left_shoulder.y + right_shoulder.y) / 2
                    if abs(nose.y - midline_y) < tolerance:
                        direction = "Facing Forward"
                        if not self.message_shown:
                            self.speak_message('Please put your phone in a position to face left or right')
                            self.message_shown = True
                            self.feedback_shown_time = time.time()

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

video_processor = VideoProcessor()

def process_video():
    video_processor.start_processing()

def stop_video():
    video_processor.stop_processing()

if __name__ == "__main__":
    process_video()

