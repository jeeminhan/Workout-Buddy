import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def push_up(im_list):

    return


# For webcam input:
def workout():
    count = 0
    position = None
    
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
                    if(imlist[12][2] >= imlist[14][2] and imlist[11][2] >= imlist[13][2]):
                        position="down"
                    if(imlist[12][2] <= imlist[14][2] and imlist[11][2] <= imlist[13][2]) and position=="down":
                        position = "up"
                        count+=1
                        print(count)


            # Flip the image horizontally for a selfie-view display.
            image=cv2.flip(image,1)
            cv2.putText(image, 
                    'Push-ups: ' + str(count), 
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