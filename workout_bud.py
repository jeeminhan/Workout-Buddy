import cv2
import mediapipe as mp
import math

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

#count = 0
push_up_pos = None
squat_pos = None

def push_up(imlist):
    global push_up_pos
    
    #down position of pushup
    if(imlist[12][2] >= imlist[14][2] and imlist[11][2] >= imlist[13][2]):
        push_up_pos="down"

    #up position of pushup
    if(imlist[12][2] <= imlist[14][2] and imlist[11][2] <= imlist[13][2]) and push_up_pos=="down":     
        push_up_pos = "up"
        return True

    return False

def push_ups_rating(imlist):
    global push_up_pos

    elbow_rating = 100
    center_rating = 100
    
    if push_up_pos == "down":

        #Creating the rating for how wide the elbows are
        elbow_pos = (imlist[14][1] - imlist[13][1])/(imlist[12][1]-imlist[11][1])
        if(elbow_pos > 1.62):
            elbow_rating -= (elbow_pos/1.62 - 1) * 279
        #print("Elbow: ", elbow_rating, " ", (elbow_rating/1.62 - 1) * 279)
        #print("Pos: ", elbow_pos)

        #Creating the rating for the centering of the head and equal distance between hands
        center = abs(imlist[14][1] - imlist [12][1])/abs(imlist[11][1] - imlist[13][1])
        if(center > 1.5):
            center_rating -= (center/1.5 - 1) * 150
        elif(center < 0.5):
            center_rating -= (1-center/0.5) * 150

    if elbow_rating < 0:
        elbow_rating = 0
    if center_rating < 0:
        center_rating = 0

    return elbow_rating, center_rating

def height_rater(maxes):
    height_rating = 100
    #avg = 0
    #imlist = lists[len(lists) - 1]
    #if len(maxes) > 0:
        #for x in maxes:
           # avg += x
        
        #avg /= len(maxes)

    if push_up_pos == "up":

        if(max(maxes) > maxes[len(maxes) - 1]):
            height_rating -= (1 - maxes[len(maxes) - 1]/max(maxes)) * 400
    #print("Percentage: ",maxes[len(maxes) - 1], " max: ", max(maxes))

    if height_rating < 0:
        height_rating = 0

    return height_rating

def push_up_comments(elbow_rating, center_rating, height_rating):

    comments = ""

    if(elbow_rating > 90):
        comments += "Good work with you elbows! \n"
    elif(elbow_rating > 50):
        comments += "Your elbows are too far apart \n"
    else:
        comments += "Your elbows need to point towards your feet \n"

    if(center_rating > 90):
        comments += "Good job pushing with both arms equally! \n"
    elif(center_rating > 50):
        comments += "Try to push with both hands equally \n"
    else:
        comments += "You are depending too heavily on one side, keep your back straight and shoulders locked \n"
    

    if(center_rating > 90):
        comments += "Good job, you are going all the way up!"
    elif(center_rating > 50):
        comments += "Try to reach the top of your rep for maximum gains"
    else:
        comments += "You are not going up high enough"
    

    return comments

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
    avg_rating = 0
    count = 0
    poses = ''
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    rep_rating = []
    heights = []
    maxes = []
    old_max = 0
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
                    #tracking.append(imlist)
                    if exercise_option == 1:
                        if imlist[12][2] < imlist[16][2]: 
                            height = (imlist[12][2] + imlist[12][2])/2
                            heights.append(height)
                        
                            elbow_rating, center_rating = push_ups_rating(imlist)
                        
                            
                            if push_up(imlist):
                                poses = 'Push-ups: '
                                #print("Elbow: ", elbow_rating, "Center: ", center_rating)
                                maxes.append(max(heights))
                                if count > 1:
                                    if old_max != max(heights):
                                        avg_rating -= 2*count

                                old_max = max(heights)
                                

                                height_rating = height_rater(maxes)
                                
                                count+=1
                                print(count)
                                heights = []

                                rep_rating.append([elbow_rating, center_rating, height_rating])

                                avg_rating += (elbow_rating * .25) + (center_rating * .35) + (height_rating * .4)

                                avg = (elbow_rating * .25) + (center_rating * .35) + (height_rating * .4)

                                print("Average: ", avg, " Elbow: ", elbow_rating, " Center: ", center_rating, " Height: ", height_rating)
                        
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
    
    if count >= 1:
        avg_rating = avg_rating/(count)
    
    print("Overall Average: ", avg_rating)

    return count, avg_rating, rep_rating

workout(1)