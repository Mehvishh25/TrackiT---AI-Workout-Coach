import cv2
import mediapipe as mp
import time
import math

class poseDectector():
    def __init__(self,mode=False,model_complexity=1,upBody=False,smooth=True,detectionCon=0.5,trackCon=0.5):
        self.mode=mode
        self.model_complexity=model_complexity
        self.upBody=upBody
        self.smooth=smooth
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpDraw=mp.solutions.drawing_utils
        self.mpPose=mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.model_complexity, self.upBody, self.smooth, self.detectionCon, self.trackCon)


    def findPose(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(imgRGB)
        #print(results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)

        return img

    def getPositions(self,img,draw=True):
        self.lmList=[]
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=img.shape
                #print(id,lm)
                cx,cy= int(lm.x*w),int(lm.y*h)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,0), cv2.FILLED)
        return self.lmList
    
    def findAngle(self,img,p1,p2,p3,draw=True):

        x1,y1=self.lmList[p1][1:]
        x2,y2=self.lmList[p2][1:]
        x3,y3=self.lmList[p3][1:]

        angle=math.degrees(math.atan2(y3-y2,x3-x2)-math.atan2(y1-y2,x1-x2))
        if angle<0:
            angle+=360

        if draw:
            cv2.line(img, (x1,y1),(x2,y2), (255,255,255), 3)
            cv2.line(img, (x3,y3),(x2,y2), (255,255,255), 3)
            cv2.circle(img, (x1,y1), 10, (255,0,0), cv2.FILLED)
            cv2.circle(img, (x1,y1), 15, (255,0,255), 2)
            cv2.circle(img, (x2,y2), 10, (255,0,0), cv2.FILLED)
            cv2.circle(img, (x2,y2), 15, (255,0,255), 2)
            cv2.circle(img, (x3,y3), 10, (255,0,0), cv2.FILLED)
            cv2.circle(img, (x3,y3), 15, (255,0,255), 2)
            cv2.putText(img, str(int(angle)), (x2-50,y2+50), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)


        return angle

def main():
    cap=cv2.VideoCapture(0)
    cap.set(3,1280)
    cap.set(4,720)
    ptime=0
    detector=poseDectector()
    while True:
        success,img=cap.read()
        img=detector.findPose(img)
        lmList=detector.getPositions(img)
        if len(lmList)!=0:
            print(lmList)
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime

        cv2.putText(img, str(int(fps)), (40,60), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0), 3 )
        cv2.imshow("image",img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__=='__main__':
    main()