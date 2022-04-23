import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

#count = 0
push_up_pos = None
squat_pos = None
max_pos = 0

def push_up(imlist):
    global push_up_pos
    global max_pos
    height = 0
    height_rating = 100
    elbow_pos = 100
    elbow_rating = 0
    center = 0
    center_rating = 100
    avg_rating = 0
    side_view = False

    #check angle of the camera
    if(imlist[14][1] - imlist[13][1]) == 0 or (imlist[12][1]-imlist[11][1]) == 0:
        side_view = True

        #down position of pushup
    if(imlist[12][2] >= imlist[14][2] and imlist[11][2] >= imlist[13][2]):
        push_up_pos="down"

        #creating the judging criteria when given a front view of the pushup
        if not side_view:

            #Creating the rating for the elbows
            elbow_pos = (imlist[14][1] - imlist[13][1])/(imlist[12][1]-imlist[11][1])
            if(elbow_pos > 1.62):
                print("Point your elbows backwards")
                elbow_rating -= (elbow_rating/1.62 - 1) * 426

            #Creating the rating for the centering of the head and equal distance between hands
            center = imlist[12][1] - (imlist[12][1] -  imlist[11][1])/2
            dist = abs(center-imlist[0][1])
            if(dist > 35):
                center_rating -= (dist/35 - 1) * 78.125
                print("Make sure you push equally with both sides")

                
    ''' if(imlist[12][2] <= imlist[14][2] and imlist[11][2] <= imlist[13][2]):
        height = (imlist[16][2]-imlist[12][2]) + (imlist[15][2]-imlist[11][2])/2  ''' 

    #up position of pushup
    if(imlist[12][2] <= imlist[14][2] and imlist[11][2] <= imlist[13][2]) and push_up_pos=="down": 
        #print("height: ", height)
        #print("starting position: ", max_pos)
        #if not side_view:

        '''if(height > max_pos):
            max_pos = height
            print("Recallibrated max height of pushup")

        if(max_pos < height):
            height_rating -= height/max_pos * 100
            #print("height: ", height)
            #print("starting position: ", max_pos)
            print("Try to go all the way up at the end of your pushup!")'''

        push_up_pos = "up"
        
        return True


    return False 



def squats(imlist):
    global squat_pos
    if(imlist[24][2] <= imlist[26][2] and imlist[23][2] <= imlist[25][2]):
        squat_pos ="down"
    if(imlist[24][2] >= imlist[26][2] and imlist[23][2] >= imlist[25][2]) and squat_pos=="down":
        squat_pos = "up"
        return True
    return False


# For webcam input:
def workout():
    global max_pos
    count = 0
    #position = None
    poses = ''
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    with mp_pose.Pose(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as pose:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
                break
                #continue
        
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = pose.process(image)

            # Draw the pose annotation on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            imlist = []
            if(results.pose_landmarks):
                mp_drawing.draw_landmarks(
                    image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                for id,im in enumerate(results.pose_landmarks.landmark):
                    h,w,_=image.shape
                    X,Y=int(im.x*w),int(im.y*h)
                    imlist.append([id,X,Y])

                if len(imlist) != 0:
                    #print(imlist[15][1])
                    #print((imlist[12][1] - (imlist[12][1] -  imlist[11][1])/2) - imlist[0][1])
                    if count == 1:
                        max_pos = (imlist[16][2]-imlist[12][2]) + (imlist[15][2]-imlist[11][2])/2
                    #print("starting position: ", starting_pos)q
                    #print(imlist[16][2])
                    if push_up(imlist):
                        poses = 'Push-ups: '
                        count+=1
                        print(count)

                    '''if squats(imlist):
                        poses = 'Squats: '
                        count+=1
                        print(count)'''

            # Flip the image horizontally for a selfie-view display.
            image=cv2.flip(image,1)
            cv2.putText(image, 
                    str(poses) + str(count), 
                    (50, 50), 
                    font, 1, 
                    (0, 0, 0), 
                    2, 
                    cv2.LINE_4)

            cv2.imshow('MediaPipe Pose', image)
            
            key=cv2.waitKey(1)
            if key == ord('q'):
                break
        
    cap.release()
    return

workout()