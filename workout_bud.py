import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

#count = 0
push_up_pos = None
squat_pos = None

elbow_rating = 0
center_rating = 0
def push_up(imlist):
    global push_up_pos
    #global elbow_rating
    #global center_rating
    elbow_rating = 100
    center_rating = 100
    #measure the peak of your pushup
    peak = 0
    peak_rating = 100

    #measure the how wide the elbows sare
    elbow_pos = 0
    #elbow_rating = 100

    #measure how centered your pushup is
    center = 0
    #center_rating = 100

    #measure how straight the back is
    back = 0
    back_rating = 100

    #average of all ratings given
    avg_rating = 0

    #check for the view of the camera
    side_view = True
    #check for which side is given
    right_side = False

    #check angle of the camera
    if(imlist[14][1] < imlist[12][1] and imlist[12][1] < imlist[11][1] and imlist[11][1] < imlist[13][1]):
        #print(" not Side View")
        side_view = False
    else:
    #if side angle of the camera is given, check for right or left side
        if(imlist[12][1]>imlist[28][1]):
            #print("Right Side")
            right_side = True

    #down position of pushup
    if(imlist[12][2] >= imlist[14][2] and imlist[11][2] >= imlist[13][2]):
        push_up_pos="down"

        #creating the judging criteria when given a front view of the pushup
        if not side_view:
            #Creating the rating for the elbows
            elbow_pos = (imlist[14][1] - imlist[13][1])/(imlist[12][1]-imlist[11][1])
            if(elbow_pos > 1.62):
                #print("Point your elbows backwards")
                elbow_rating -= (elbow_rating/1.62 - 1) * 426

            #Creating the rating for the centering of the head and equal distance between hands
            center = abs(imlist[14][1] - imlist [12][1])/abs(imlist[11][1] - imlist[13][1])
            #dist = abs(center-imlist[0][1])
            if(center > 1.5):
                center_rating -= (center/1.5 - 1) * 150
                #print("Center greater: ", center_rating)

            elif(center < 0.5):
                center_rating -= (1-center/0.5) * 150
                #print("Center lesser: ", center_rating)
        
        else:
            if(right_side):
                back = imlist[12][2]-imlist[24][2]
            else:
                back = imlist[11][2]-imlist[23][2]



        #print("Elbow: ", elbow_rating, " Center: ", center_rating)
    #up position of pushup
    if(imlist[12][2] <= imlist[14][2] and imlist[11][2] <= imlist[13][2]) and push_up_pos=="down": 
        
        if side_view:
            if(right_side):
        #         height = imlist[12][1] - imlist[14][1]
                back = imlist[12][2] - imlist[24][2]
            else:
        #       height = imlist[13][1] - imlist[11][1]
        #       print("height: ", height)
                back = imlist[11][2] - imlist[23][2]
            if(back > 10):
                back_rating -= 10

            
        push_up_pos = "up"

        return True, -1, -1


    return False, elbow_rating, center_rating



def squats(imlist):
    global squat_pos

    back = 0

    center = 0
    center_rating = 100

    feet = 0
    feet_rating = 100

    knees = 0

    side_view = True
    right_view = False

    if(imlist[24][2] >= imlist[26][2] and imlist[23][2] >= imlist[25][2]):
        squat_pos ="down"

        feet = abs(imlist[31][2]-imlist[29][2])
        if(feet > 1):
            feet_rating -= 15

        center = imlist[11][1] - (imlist[29][1] - (imlist[29][1] - imlist[31][1])/2)
        print("Center: ", center)
        if(center > 1.5):
            center_rating -= 10
            
    if(imlist[24][2] <= imlist[26][2] and imlist[23][2] <= imlist[25][2]) and squat_pos=="down":
        squat_pos = "up"
        return True
    
    return False


# For webcam input:
def workout(exercise_option):
    #global 
    elbow_rating = 0
    index=0
    #global
    center_rating = 0
    shoulders = []
    avg_rating = 0
    global max_pos
    rep_rating = []
    count = 0
    poses = ''
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    i = 0
    num = 0
    temps =[]
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
                    i+=1
                    shoulders.append(imlist[12][2])
                    #print("i ", i, "lenght ", len(shoulders))
                    temps = []
                    if exercise_option == 1:
                        test, temp1, temp2 = push_up(imlist)
                        if(len(shoulders) > 10):
                            #print(len(shoulders), " i ", i)
                            #print("shoulders", shoulders[i-1])
                            min = shoulders[num-5]
                            index = 0
                            y = -1
                            for x in shoulders[num-5:num]:
                                y += 1
                                if(x < min):
                                    min = x
                                    index = y
                                temps.append([temp1, temp2])
                            # if shoulders[i-3] > shoulders[i-2] and shoulders[i-2] > shoulders[i-1] and test:
                            #     elbow_rating = temp1
                            #     center_rating = temp2
                            #     print("Elbow: ", elbow_rating, " Center: ", center_rating)
                           # y = min(temps)

                            if test:
                                if len(temps) > index:
                                    print("len ", len(temps), ", index: ", index)
                                    elbow_rating = temps[index][0]
                                    center_rating = temps[index][1]
                                    rep_rating.append([elbow_rating, center_rating, 0 ,0])
                                    avg_rating += elbow_rating + center_rating
                                    poses = 'Push-ups: '
                                    num = i
                                    count+=1
                                    print(count)

                    elif exercise_option == 2:
                        if squats(imlist):
                            poses = 'Squats: '
                            count+=1
                            print(count)

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
    cv2.destroyAllWindows()

    avg_rating = avg_rating/(count * 2)
    
    return count, avg_rating, rep_rating

workout(1)