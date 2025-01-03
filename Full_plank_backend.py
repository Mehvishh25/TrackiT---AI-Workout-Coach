import cv2
import mediapipe as mp
import time
import Pose_module as pm
import pyttsx3
import numpy as np
import streamlit as st

class VideoProcessor:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 1)

        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()
        
        self.cap = cv2.VideoCapture(0)

        self.cap.set(3, 200)
        self.cap.set(4, 150)

        self.pTime = 0
        self.detector = pm.poseDectector()
        self.count = 0
        self.dir = 0
        self.message_shown = False
        self.message_shown1 = False
        self.message_shown2 = False
        self.message_shown3 = False
        self.message_shown4 = False
        self.message_shown5 = False
        self.message_shown6 = False
        self.message_shown7 = False
        self.message_shown8 = False
        self.message_shown9 = False
        self.message_shown10 = False
        self.message_shown11 = False
        self.message_shown12 = False
        self.message_shown13 = False
        self.message_shown14 = False
        self.message_shown15 = False
        self.feedback_shown_time = 0
        self.wait_start_time=time.time()


    def speak_message(self, message):
        self.engine.say(message)
        self.engine.runAndWait()

    def start_processing(self,level):

        self.cap = cv2.VideoCapture(0)
        frame_placeholder = st.empty()
            
        #time.sleep(30)

        while self.cap.isOpened():
            success, img = self.cap.read()
            if not success:
                break

            if time.time() - self.wait_start_time >= 30:
                direction='Facing Forward'

                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                result = self.pose.process(img_rgb)

                img = self.detector.findPose(img)
                lmList = self.detector.getPositions(img, False)

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
                            angle2 = self.detector.findAngle(img, 11, 23, 25)
                            angle3 = self.detector.findAngle(img, 23, 25, 27)
                            angle4 = self.detector.findAngle(img, 25, 27, 31)
                            angle1 = self.detector.findAngle(img, 11, 13, 15)

                            if angle1 > 185:
                                if not self.message_shown1 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Keep your elbows tucked closer to your body to maintain alignment')
                                    self.message_shown1 = True
                                    self.feedback_shown_time = time.time()

                            if angle1 < 175:
                                if not self.message_shown2 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Make your elbows outward slightly so they are directly under your')
                                    self.message_shown2 = True
                                    self.feedback_shown_time = time.time()

                            if angle2 > 195:
                                if not self.message_shown3 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Lift your hips slightly to keep your body in a straight line')
                                    self.message_shown3 = True
                                    self.feedback_shown_time = time.time()

                            if angle2 < 185:
                                if not self.message_shown4 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Lower your hips to align them with your shoulder and heels')
                                    self.message_shown4 = True
                                    self.feedback_shown_time = time.time()

                            if angle3 < 175:
                                if not self.message_shown5 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Keep your knees off the ground')
                                    self.message_shown5 = True
                                    self.feedback_shown_time = time.time()

                            if angle4 < 252:
                                if not self.message_shown6 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Keep your ankles neutral. Do not let them roll out')
                                    self.message_shown6 = True
                                    self.feedback_shown_time = time.time()

                            if 175 <= angle1 <= 185 and 180 <= angle2 <= 190 and 175 <= angle3 <= 185 and 265 <= angle4 <= 285 and dir == 0:
                                if not self.message_shown7 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Perfect')
                                    self.message_shown7 = True
                                    self.feedback_shown_time = time.time()

                            self.wait_start_time=time.time()
                            if level=='Beginner':
                                if time.time() - self.wait_start_time >= 15:
                                    if 170 <= angle1 <= 190 and 175 <= angle2 <= 195 and 180 <= angle3 <= 190 and 270 <= angle4 <= 290 and dir == 0:
                                        self.count += 1
                            elif level=='Intermediate':
                                if time.time() - self.wait_start_time >= 30:
                                    if 170 <= angle1 <= 190 and 175 <= angle2 <= 195 and 180 <= angle3 <= 190 and 270 <= angle4 <= 290 and dir == 0:
                                        self.count += 1
                            else:
                                if time.time() - self.wait_start_time >= 60:
                                    if 170 <= angle1 <= 190 and 175 <= angle2 <= 195 and 180 <= angle3 <= 190 and 270 <= angle4 <= 290 and dir == 0:
                                        self.count += 1

                    elif nose.x > midline_x + tolerance:
                        direction = "Facing Left"
                        if len(lmList) != 0:
                            angle1 = self.detector.findAngle(img, 12, 14, 16)
                            angle2 = self.detector.findAngle(img, 12, 24, 26)
                            angle3 = self.detector.findAngle(img, 24, 26, 28)
                            angle4 = self.detector.findAngle(img, 26, 28, 32)

                            if angle1 > 175:
                                if not self.message_shown8 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Make your elbows outward slightly so they are directly under your')
                                    self.message_shown8 = True
                                    self.feedback_shown_time = time.time()

                            if angle1 < 185:
                                if not self.message_shown9 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Keep your elbows tucked closer to your body to maintain alignment')
                                    self.message_shown9 = True
                                    self.feedback_shown_time = time.time()

                            if angle2 > 175:
                                if not self.message_shown10 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Lift your hips slightly to keep your body in a straight line')
                                    self.fmessage_shown10 = True
                                    self.feedback_shown_time = time.time()

                            if angle2 < 165:
                                if not self.message_shown11 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Lower your hips to align them with your shoulder and heels')
                                    self.message_shown11 = True
                                    self.feedback_shown_time = time.time()

                            if angle3 > 185:
                                if not self.message_shown12 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Keep your knees off the ground')
                                    self.message_shown = True
                                    self.feedback_shown_time = time.time()

                            if angle4 > 98:
                                if not self.message_shown13 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Keep your ankles neutral. Do not let them roll out')
                                    self.message_shown13 = True
                                    self.feedback_shown_time = time.time()

                            if 175 <= angle1 <= 185 and 165 <= angle2 <= 175 and 175 <= angle3 <= 185 and 80 <= angle4 <= 95 and dir == 0:
                                if not self.message_shown14 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Perfect')
                                    self.message_shown = True
                                    self.feedback_shown_time = time.time()

                                count += 1
                            self.wait_start_time=time.time()
                            if level=='Beginner':
                                if time.time() - self.wait_start_time >= 15:
                                    if 170 <= angle1 <= 190 and 155 <= angle2 <= 180 and 165 <= angle3 <= 190 and 80 <= angle4 <= 100 and dir == 0:
                                        self.count += 1
                            elif level=='Intermediate':
                                if time.time() - self.wait_start_time >= 30:
                                    if 170 <= angle1 <= 190 and 155 <= angle2 <= 180 and 165 <= angle3 <= 190 and 80 <= angle4 <= 100 and dir == 0:
                                        self.count += 1
                            else:
                                if time.time() - self.wait_start_time >= 60:
                                    if 170 <= angle1 <= 190 and 155 <= angle2 <= 180 and 165 <= angle3 <= 190 and 80 <= angle4 <= 100 and dir == 0:
                                        self.count += 1

                    else:
                        if not self.message_shown or (time.time() - self.feedback_shown_time > 2):
                            self.speak_message('Keep your phone in a position to face left or right')
                            self.message_shown = True
                            self.feedback_shown_time = time.time()
                    
                    self.wait_start_time=time.time()
                    if self.dir == 1:
                        if not self.message_shown15 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Wait')
                                    self.message_shown14 = True
                                    self.feedback_shown_time = time.time()
                        self.wait_start_time=time.time()
                        if level == "Beginner":
                            if not self.message_shown15 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Wait for 10 seconds')
                                    self.message_shown15 = True
                                    self.feedback_shown_time = time.time()
                            if time.time() - self.wait_start_time >= 10:
                                continue
                        elif level == "Intermediate":
                            if not self.message_shown15 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Wait for 15 seconds')
                                    self.message_shown15 = True
                                    self.feedback_shown_time = time.time()
                            if time.time() - self.wait_start_time >= 20:
                                continue  
                        else:
                            if not self.message_shown15 or (time.time() - self.feedback_shown_time > 2):
                                    self.speak_message('Wait for 20 seconds')
                                    self.message_shown14 = True
                                    self.feedback_shown_time = time.time()
                            if time.time() - self.wait_start_time >= 30:
                                continue              
                        self.dir = 0  # Reset the system for the next action
                        self.message_shown = False
                        self.message_shown1 = False
                        self.message_shown2 = False
                        self.message_shown3 = False
                        self.message_shown4 = False
                        self.message_shown5 = False
                        self.message_shown6 = False
                        self.message_shown7 = False
                        self.message_shown8 = False
                        self.message_shown9 = False
                        self.message_shown10 = False
                        self.message_shown11 = False
                        self.message_shown12 = False
                        self.message_shown13 = False
                        self.message_shown14 = False
                        self.message_shown15 = False
                        self.feedback_shown_time = 0

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = cv2.putText(img, f'Count: {self.count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            img = cv2.putText(img, f'Direction: {direction}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            img = cv2.putText(img, f'Level: {level}', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cTime = time.time()
            fps = 1 / (cTime - self.pTime) if self.pTime != 0 else 0  # Avoid division by zero
            self.pTime = cTime
            #print(f'FPS: {int(fps)}')

            frame_placeholder.image(img, channels="BGR", use_container_width=True)

    def stop_processing(self):
        if self.cap is not None:
            self.cap.release()
            cv2.destroyAllWindows()

video_processor = VideoProcessor()

def process_video(level):
    video_processor.start_processing(level)

def stop_video():
    video_processor.stop_processing()

if __name__ == "__main__":
    process_video()
