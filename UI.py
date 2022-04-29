#Import the required libraries
from tkinter import *
import csv, random
import time
from datetime import datetime
from datetime import timedelta
import ast
import workout_bud
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
def finishedWorkoutScreen(root, userNum, workoutType):
    frame = Frame(root)
    frame.grid(row=0, column=0)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        mainFrame(root)

    pushUpRep = []
    pushUpList = []
    parameter1 = []
    parameter2 = []
    parameter3 = []
    avgScore = []

    col1Total = 0
    col2Total = 0
    col3Total = 0

    if workoutType == 1:
        if userNum==1:
            pushUpList = user1PushupsList
        elif userNum==2:
            pushUpList = user2PushupsList
        elif userNum==3:
            pushUpList = user3PushupsList
    elif workoutType == 2:
        if userNum==1:
            pushUpList = user1SquatsList
        elif userNum==2:
            pushUpList = user2SquatsList
        elif userNum==3:
            pushUpList = user3SquatsList
    # Getting the specific row
    pushUpList = pushUpList[len(pushUpList)-1][3]
    #converting the list
    pushUpList = ast.literal_eval(pushUpList)

    for i in range(len(pushUpList)):
        pushUpRep.append(i+1)
        # if i%2:
        #     if i!=1:
        #         percentScore.append(pushUpList[i])
        # else:
        #     if i!= 0:
        #         comments.append(pushUpList[i])
        parameter1.append(pushUpList[i][0])
        parameter2.append(pushUpList[i][1])
        parameter3.append(pushUpList[i][2])
        avg = ((pushUpList[i][0]+pushUpList[i][1]+pushUpList[i][2])/3)
        avg = "{avg:.2f}".format(avg=avg)
        avgScore.append(avg)
        col1Total += pushUpList[i][0]
        col2Total += pushUpList[i][1]
        col3Total += pushUpList[i][2]

    col1Total = col1Total/len(pushUpRep) if col1Total else 0
    col2Total = col2Total/len(pushUpRep) if col1Total else 0
    col3Total = col3Total/len(pushUpRep) if col1Total else 0
    if (col1Total == 0 and col2Total == 0 and col3Total == 0):
        topComments = "0 Pushups Done"
    else:
        if workoutType == 1:
            topComments = workout_bud.push_up_comments(col1Total,col2Total,col3Total) 
        else:
            topComments = workout_bud.squat_commenter(col1Total,col2Total,col3Total) 


    myLabel1 = Label(frame, text="Workout Summary", font=("Helvetica", 25, "bold italic"))
    myLabel1.grid(row=0, column=0)
    myLabel1 = Label(frame, text=topComments)
    myLabel1.grid(row=1, column=0)
    doneButton = Button(frame, text="Back", padx=20, pady=15, fg="blue", command=myClick, font=("Helvetica", 25, "bold italic"))
    doneButton.grid(row=3, column=0)


    # the figure that will contain the plot
    fig = Figure(figsize = (8, 3),
                 dpi = 100)
  
    # list of squares
    x = pushUpRep
    y = [float(x) for x in avgScore]
    y.sort()
    
    # adding the subplot
    plot1 = fig.add_subplot(111)
 
    # plotting the graph

    plot1.scatter(x,y)
    
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = frame)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row=2, column=0)
  
    # creating the Matplotlib toolbar
    # toolbar = NavigationToolbar2Tk(canvas,frame)
    # toolbar.update()
  
    # # placing the toolbar on the Tkinter window
    # canvas.get_tk_widget().grid(row=1,column=0)


def workingOutSkeleton():
    random.seed()
    randomDay = random.randint(1,1000)
    randomHour = random.randint(1,500)
    randomMin = random.randint(1,500)
    currentTime = datetime.now()
    finalTime = currentTime - timedelta(days=randomDay, hours=randomHour, minutes=randomMin)
    # finalTimeStr = finalTime.strftime('%m-%d-%Y %H:%M')
    pushUpRep = random.randint(10,30)
    rating = random.uniform(50.1, 98.7)

    parameterList = []
    for i in range(pushUpRep):
        row = []
        for j in range(4):
            row.append(random.randint(1,100))
        parameterList.append(row)
    rating = "{rating:.2f}".format(rating=rating)
    return finalTime, pushUpRep, float(rating), parameterList


def deleteUser(root):
    #Create a frame
    frame = Frame(root)
    frame.grid(row=0, column=0)

    def myClick(userNum):
        fileName = "CSV_Files/users.csv"
        global user1
        global user2
        global user3
        if userNum == 1:
            user1 = "Add User"
            line = ["Add User", user2 , user3]
        elif userNum == 2:
            user2 = "Add User"
            line = [user1, "Add User" , user3]
        elif userNum == 3:
            user3 = "Add User"
            line = [user1, user2 , "Add User"]
        with open(fileName,'w') as csvfile: 
            csvWriter = csv.writer(csvfile) 
            csvWriter.writerow(line)

        for widgets in frame.winfo_children():
            widgets.destroy()
        mainFrame(root)
    def back():
        for widgets in frame.winfo_children():
            widgets.destroy()
        mainFrame(root)

    myLabel1 = Label(frame, text="Which user would you like to delete?", font=("Helvetica", 18, "bold italic"))
    myLabel1.grid(row=0, column=1)

    myButton1 = Button(frame, text=user1, width=8, height=2, padx=20, pady=15, fg="blue", command=lambda:myClick(1), font=("Helvetica", 25, "bold italic"))
    myButton2 = Button(frame, text=user2, width=8, height=2, padx=20, pady=15, fg="blue", command=lambda:myClick(2), font=("Helvetica", 25, "bold italic"))
    myButton3 = Button(frame, text=user3, width=8, height=2,padx=20, pady=15, fg="blue", command=lambda:myClick(3), font=("Helvetica", 25, "bold italic"))
    myButton1.grid(row=1, column=0)
    myButton2.grid(row=1, column=1)
    myButton3.grid(row=1, column=2)

    doneButton = Button(frame, text="Back", width=7, height=1, padx=20, pady=15, fg="blue", command=back, font=("Helvetica", 25, "bold italic"))
    doneButton.grid(row=2, column=1)
    
def workoutFrame(root, userNum):
    global optionWorkout
    global finalTimeVar 
    global repsVar
    global totalScoreVar 
    global paramListVar 
    optionWorkout = 0
    #Create a frame
    # buttonPress = 0
    frame = Frame(root)
    frame.grid(row=0, column=0)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        userInfoFrame(root, userNum)
    def saveWorkout(reps, totalScore, parameterList, timeObj=datetime.now()):
    
        parameterString = ""
        #current_time = datetime.now()
        # Convert datetime object to string in specific format 
        curr_time_str = timeObj.strftime('%m-%d-%Y %H:%M')
        fileName = ""
        if optionWorkout == 1:
            if userNum==1:
                fileName = "CSV_Files/user1Pushups.csv"         
            elif userNum==2:
                fileName = "CSV_Files/user2Pushups.csv" 
            elif userNum==3:
                fileName = "CSV_Files/user3Pushups.csv" 
            with open(fileName, 'a') as csvfile: 
                dateRepCommentList = [curr_time_str, reps, totalScore, parameterList]
                csvWriter = csv.writer(csvfile) 
                csvWriter.writerow(dateRepCommentList)
        elif optionWorkout == 2:
            if userNum==1:
                fileName = "CSV_Files/user1Squats.csv"         
            elif userNum==2:
                fileName = "CSV_Files/user2Squats.csv" 
            elif userNum==3:
                fileName = "CSV_Files/user3Squats.csv" 
            with open(fileName, 'a') as csvfile: 
                dateRepCommentList = [curr_time_str, reps, totalScore, parameterList]
                csvWriter = csv.writer(csvfile) 
                csvWriter.writerow(dateRepCommentList)
        for widgets in frame.winfo_children():
            widgets.destroy()
        time.sleep(1)
        finishedWorkoutScreen(root, userNum, optionWorkout)

    def dontSaveWorkout():
        for widgets in frame.winfo_children():
            widgets.destroy()
        time.sleep(0.25)
        userInfoFrame(root, userNum)

    # finalTimeVar, repsVar, totalScoreVar, paramListVar = workingOutSkeleton()

    myLabel1 = Label(frame, text="Choose Push-up or Squats", fg="blue", font=("Helvetica", 25, "bold italic"))

    # r = IntVar()
    # def radioButtonPress(value):
    #     global buttonPress
    #     if value==1:
    #         buttonPress = 1
    #         #workout_bud.workout(1)
    #         print(buttonPress)
    #     elif value==2:
    #         buttonPress = 2
    #         #workout_bud.workout(2)
    # print(buttonPress)
    # def startWorkout():
    #     print(buttonPress)
    #     if buttonPress == 1:
    #         workout_bud.workout(1)
    #     elif buttonPress ==2:
    #         workout_bud.workout(2)
    #     else:
    #         print("Please select radio button")
    
    
    def startPushups():
        global optionWorkout
        optionWorkout = 1
        global finalTimeVar, repsVar, totalScoreVar, paramListVar
        myButton1.destroy()
        myButton2.destroy()
        myButton4.destroy()
        myButton3.grid(row=3, column=0)
        myButton5.grid()
        





        # finalTimeVar, repsVar, totalScoreVar, paramListVar = workingOutSkeleton()
        repsVar, totalScoreVar, paramListVar = workout_bud.workout(1)
        #finishedWorkoutScreen(root, userNum)

    def startSquats():
        global optionWorkout
        optionWorkout = 2
        global finalTimeVar, repsVar, totalScoreVar, paramListVar
        myButton1.destroy()
        myButton2.destroy()
        myButton4.destroy()
        myButton3.grid(row=3, column=0)


        # finalTimeVar, repsVar, totalScoreVar, paramListVar = workingOutSkeleton()
        repsVar, totalScoreVar, paramListVar = workout_bud.workout(2)   

    # RB1 = Radiobutton(frame, text="Push-Ups", variable=r, value=1, command=lambda: radioButtonPress(r.get()))
    # RB1.grid(row=1, column=0)
    # RB2 = Radiobutton(frame, text="Squats", variable=r, value=2, command=lambda: radioButtonPress(r.get()))
    # RB2.grid(row=2, column=0)
    myButton1 = Button(frame, text="Start Pushups", padx=20, pady=15, fg="blue", command=startPushups, font=("Helvetica", 16, "bold italic"))
    myButton2 = Button(frame, text="Start Squats", padx=20, pady=15, fg="blue", command=startSquats, font=("Helvetica", 16, "bold italic"))
    myButton3 = Button(frame, text="Save Workout (This will end your workout session)", padx=20, pady=15, fg="blue", command=lambda:saveWorkout(repsVar, totalScoreVar, paramListVar))
    myButton4 = Button(frame, text="Done", padx=20, pady=15, fg="blue", command=myClick)
    myButton5 = Button(frame, text="Exit Without Saving", padx=20, pady=15, fg="blue", command=dontSaveWorkout)


    myLabel1.grid(row=0, column=0)
    myButton1.grid(row=1, column=0)
    myButton2.grid(row=2, column=0)
    myButton4.grid(row=3, column=0)



def showStats(root, userNum, dateRow, workoutType):
    frame = Frame(root)
    # WHAT DOES THIS DO?
    frame.grid(row=0, column=0)


    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        userInfoFrame(root, userNum)

    pushUpRep = []
    pushUpList = []
    parameter1 = []
    parameter2 = []
    parameter3 = []
    avgScore = []

    col1Total = 0
    col2Total = 0
    col3Total = 0

    if workoutType == 1:
        if userNum==1:
            pushUpList = user1PushupsList
        elif userNum==2:
            pushUpList = user2PushupsList
        elif userNum==3:
            pushUpList = user3PushupsList
    elif workoutType == 2:
        if userNum==1:
            pushUpList = user1SquatsList
        elif userNum==2:
            pushUpList = user2SquatsList
        elif userNum==3:
            pushUpList = user3SquatsList
    # Getting the specific row
    pushUpList = pushUpList[int(dateRow)][3]
    #converting the list
    pushUpList = ast.literal_eval(pushUpList)

    for i in range(len(pushUpList)):
        pushUpRep.append(i+1)
        # if i%2:
        #     if i!=1:
        #         percentScore.append(pushUpList[i])
        # else:
        #     if i!= 0:
        #         comments.append(pushUpList[i])
        parameter1.append(pushUpList[i][0])
        parameter2.append(pushUpList[i][1])
        parameter3.append(pushUpList[i][2])
        avg = ((pushUpList[i][0]+pushUpList[i][1]+pushUpList[i][2])/3)
        avg = "{avg:.2f}".format(avg=avg)
        avgScore.append(avg)
        col1Total += pushUpList[i][0]
        col2Total += pushUpList[i][1]
        col3Total += pushUpList[i][2]




        
    myButton2 = Button(frame, text="Back", padx=20, pady=15, fg="blue", command=myClick, font=("Helvetica", 25, "bold italic"))
    myButton2.grid(row=1, column=0)
    test = Text(frame, width=110, height=20)
    test.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    #ADDING A SCROLLBAR
    # myscrollbar=Scrollbar(frame, orient="vertical")
    # myscrollbar.grid(row=2, column = 0,fill="y")

    col1Total = col1Total/len(pushUpRep) if col1Total else 0
    col2Total = col2Total/len(pushUpRep) if col1Total else 0
    col3Total = col3Total/len(pushUpRep) if col1Total else 0

    test.delete(1.0,END)   # Delete text from widget if there is any
    test.insert(END,'Things to work on:\n')
    if not pushUpList:
        test.insert(END,'No pushups or squats recorded for this workout:\n')
    else:
        if workoutType == 1:
            line = workout_bud.push_up_comments(col1Total,col2Total,col3Total)
        elif workoutType == 2:
            line = workout_bud.squat_commenter(col1Total,col2Total,col3Total)
        test.insert(END,line+'\n\n')
        test.insert(END,'Rep:   Avg Score:    Elbow Rating   Center Rating    Height Rating:\n')
    for index in range(len(pushUpRep)):
        col1 = '{:<8}'.format(pushUpRep[index])
        col2 = '{:<13}'.format(avgScore[index])
        col3 = '{:<15}'.format(parameter1[index])
        col4 = '{:<17}'.format(parameter2[index])
        col5 = '{:<13}'.format(parameter3[index])
        # comments = '{:<20}'.format(workout_bud.push_up_comments(pushUpList[i][0], pushUpList[i][1], pushUpList[i][2]))
        
        line = col1 + col2 + col3 + col4 + col5 + '\n'
        test.insert(END,line)

    

def viewStatsFrame(root, userNum, workoutType):
    pushUpList = []
    options = []
    frame = Frame(root)
    frame.grid(row=0, column=0)
    # workoutType = 1

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        userInfoFrame(root, userNum)

    def show():
        optionChosenNum = options.index(clicked.get())
        # workoutInfo = pushUpList[optionChosen]


        # myLabel2 = Label(frame, text=workoutInfo, fg="blue", bg="#f5f5dc")
        # myLabel2.grid(row=3, column=0)
        for widgets in frame.winfo_children():
            widgets.destroy()
        showStats(root, userNum, optionChosenNum, workoutType)

    # r = IntVar()
    # def radioButtonPress(value):
    #     global buttonPress
    #     global options
    #     if value==1:
    #         buttonPress = 1
    #         #workout_bud.workout(1)
    #         workoutType = 1
    #         if userNum==1:
    #             pushUpList = user1PushupsList
    #         elif userNum==2:
    #             pushUpList = user2PushupsList
    #         elif userNum==3:
    #             pushUpList = user3PushupsList
    #         for row in pushUpList:
    #             options.append(row[0])
    #         print(buttonPress)
    #     elif value==2:
    #         buttonPress = 2
    #         workoutType = 2
            
    #         if userNum==1:
    #             pushUpList = user1SquatsList
    #         elif userNum==2:
    #             pushUpList = user2SquatsList
    #         elif userNum==3:
    #             pushUpList = user3SquatsList
    #         for row in pushUpList:
    #             options.append(row[0])
    #             print(buttonPress)
            #workout_bud.workout(2)

    if workoutType == 1:
        if userNum==1:
            pushUpList = user1PushupsList
        elif userNum==2:
            pushUpList = user2PushupsList
        elif userNum==3:
            pushUpList = user3PushupsList
        for row in pushUpList:
            options.append(row[0])
    elif workoutType == 2:
        if userNum==1:
            pushUpList = user1SquatsList
        elif userNum==2:
            pushUpList = user2SquatsList
        elif userNum==3:
            pushUpList = user3SquatsList
        for row in pushUpList:
            options.append(row[0])
    clicked = StringVar()

    myLabel1 = Label(frame, text="Stats Menu", fg="blue", font=("Helvetica", 25, "bold italic"))
    myLabel1.grid(row=0, column=0)

    # RB1 = Radiobutton(frame, text="Push-Ups", variable=r, value=1, command=lambda: radioButtonPress(r.get()))
    # RB1.grid(row=1, column=0)
    # RB2 = Radiobutton(frame, text="Squats", variable=r, value=2, command=lambda: radioButtonPress(r.get()))
    # RB2.grid(row=1, column=1)
    # print(options)
    options.reverse()
    drop = OptionMenu(frame, clicked, *options)
    drop.grid(row=1, column=0)


    myButton1 = Button(frame, text="Choose Date", padx=20, pady=15, fg="blue", command=show, font=("Helvetica", 25, "bold italic"))
    myButton1.grid(row=2, column=0)

    myButton2 = Button(frame, text="Back", padx=20, pady=15, fg="blue", command=myClick, font=("Helvetica", 25, "bold italic"))
    myButton2.grid(row=3, column=0)

    # myLabel2 = Label(frame, text="")
    # myLabel2.grid(row=0, column=0)
    # myLabel3 = Label(frame, text="")
    # myLabel3.grid(row=1, column=0)
    # myLabel4 = Label(frame, text="")
    # myLabel4.grid(row=2, column=0)
    # myLabel5 = Label(frame, text="")
    # myLabel5.grid(row=3, column=0)

def userInfoFrame(root, userNum):
    # TODO show workout stats on this page
    frame = Frame(root)
    frame.grid(row=0, column=0)

    currentUser = ""
    pushupsDone = 0
    workoutsCompleted = 0
    avgRating = 0

    squatsDone = 0
    workoutsCompletedSquat = 0
    avgRatingSquat = 0

    if userNum==1:
        currentUser = user1
        if user1PushupsList:
            for i in range(len(user1PushupsList)):
                pushupsDone += int(user1PushupsList[i][1])
                avgRating += float(user1PushupsList[i][2])
            avgRating = avgRating/len(user1PushupsList)
        workoutsCompleted += len(user1PushupsList)
        if user1SquatsList:
            for i in range(len(user1SquatsList)):
                squatsDone += int(user1SquatsList[i][1])
                avgRatingSquat += float(user1SquatsList[i][2])
            avgRatingSquat = avgRatingSquat/len(user1SquatsList)
        workoutsCompletedSquat += len(user1SquatsList)

        
        
    elif userNum==2:
        currentUser = user2
        if user2PushupsList:
            for i in range(len(user2PushupsList)):
                pushupsDone += int(user2PushupsList[i][1])
                avgRating += float(user2PushupsList[i][2])
            avgRating = avgRating/len(user2PushupsList)
        workoutsCompleted += len(user2PushupsList)
        if user2SquatsList:
            for i in range(len(user2SquatsList)):
                squatsDone += int(user2SquatsList[i][1])
                avgRatingSquat += float(user2SquatsList[i][2])
            avgRatingSquat = avgRatingSquat/len(user2SquatsList)
        workoutsCompletedSquat += len(user2SquatsList)

    elif userNum==3:
        currentUser = user3
        if user3PushupsList:
            for i in range(len(user3PushupsList)):
                pushupsDone += int(user3PushupsList[i][1])
                avgRating += float(user3PushupsList[i][2])
            avgRating = avgRating/len(user3PushupsList)
        workoutsCompleted += len(user3PushupsList)
        if user3SquatsList:
            for i in range(len(user3SquatsList)):
                squatsDone += int(user3SquatsList[i][1])
                avgRatingSquat += float(user3SquatsList[i][2])
            avgRatingSquat = avgRatingSquat/len(user3SquatsList)
        workoutsCompletedSquat += len(user3SquatsList)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        mainFrame(root)
    
    def workout():
        for widgets in frame.winfo_children():
            widgets.destroy()
        workoutFrame(root, userNum)
    
    def viewStats(workoutType):
        for widgets in frame.winfo_children():
            widgets.destroy()
        viewStatsFrame(root, userNum, workoutType)
    avgRating = (avgRating+avgRatingSquat)/2
    avgRating = "{avg:.2f}".format(avg=avgRating)

    myLabel1 = Label(frame, text="Welcome " + currentUser+ " you can view your workout stats or start a workout", font=("Helvetica", 12, "bold italic"), fg='blue')
    myLabel1.grid(row=0, column=1)
    myLabel2 = Label(frame, text= "You've done " + str(pushupsDone+squatsDone) + " squats and pushups total!", font=("Helvetica", 17, "bold italic"))
    myLabel2.grid(row=1, column=1)
    myLabel2 = Label(frame, text= "Your average rating is " + str(avgRating) + " for all workouts!", font=("Helvetica", 17, "bold italic"))
    myLabel2.grid(row=2, column=1)
    myLabel3 = Label(frame, text= "You've completed " + str(workoutsCompleted+workoutsCompletedSquat) + " workouts!", font=("Helvetica", 18, "bold italic"))
    myLabel3.grid(row=3, column=1)
    myButton1 = Button(frame, text="Workout", width=15, height=5, padx=20, pady=15, command=workout, font=("Helvetica", 13, "bold italic"))
    myButton1.grid(row=1, column=0)
    myButton2 = Button(frame, text="View Push-Up Stats" , width=15, height=2, padx=20, pady=5, command=lambda:viewStats(1), font=("Helvetica", 13, "bold italic"))
    myButton2.grid(row=2, column=0)
    myButton3 = Button(frame, text="View Squat Stats" , width=15, height=2, padx=20, pady=5, command=lambda:viewStats(2), font=("Helvetica", 13, "bold italic"))
    myButton3.grid(row=3, column=0)
    myButton4 = Button(frame, text="Back", width=15, height=5, padx=20, pady=15, command=myClick, font=("Helvetica", 13, "bold italic"))
    myButton4.grid(row=4, column=0)

def createUserFrame(root, userNum):
    #Create a frame
    frame = Frame(root)
    frame.grid(row=0, column=0)

    def myClick():
        newUser = e.get()

        if newUser:
            for widgets in frame.winfo_children():
                widgets.destroy()
        # if userNum == 1:
        #     user1 = "Add User"
        #     line = ["Add User", user2 , user3]
        # elif userNum == 2:
        #     user2 = "Add User"
        #     line = [user1, "Add User" , user3]
        # elif userNum == 3:
        #     user3 = "Add User"
        #     line = [user1, user2 , "Add User"]
        # print(line)
            global user1
            global user2
            global user3
            
            if userNum==1:
                line = [newUser, user2 , user3]
                user1 = newUser
            elif userNum==2:
                line = [user1, newUser , user3]
                user2 = newUser
            elif userNum==3:
                line = [user1, user2, newUser]
                user3 = newUser
            fileName = "CSV_Files/users.csv"
            with open(fileName,'w') as csvfile: 
                csvWriter = csv.writer(csvfile) 
                csvWriter.writerow(line)

            #return newUser
            # user = newUser
            mainFrame(root)
        


    myLabel1 = Label(frame, text="Choose Username", fg="blue")
    myLabel1.grid(row=0, column=0)
    e = Entry(frame, width=50)
    e.grid(row=1, column=0)
    myButton1 = Button(frame, text="Done", padx=20, pady=15, fg="blue", command=myClick)
    myButton1.grid(row=2, column=0)

def mainFrame(root):
    #Create a frame
    frame = Frame(root)
    frame.grid(row=0, column=0)
                
    def createUser(userNum):
        for widgets in frame.winfo_children():
            widgets.destroy()
        createUserFrame(root, userNum)

    def userScreen(userNum):
        for widgets in frame.winfo_children():
            widgets.destroy()
        userInfoFrame(root, userNum)

    def intermediateFunction(userNum):
        if userNum == 1:
            if user1 == "Add User":
                createUser(1)
            else:
                userScreen(1)
        elif userNum == 2:
            if user2 == "Add User":
                createUser(2)
            else:
                userScreen(2)
        elif userNum == 3:
            if user3 == "Add User":
                createUser(3)
            else:
                userScreen(3)
    def deleteUserFunc():
        for widgets in frame.winfo_children():
            widgets.destroy()
        deleteUser(root)


    #Stuff in Frame
    myLabel1 = Label(frame, text="Welcome to Workout Buddy!", font=("Helvetica", 25, "bold italic"))
    myLabel2 = Label(frame, text="", fg="blue", font=("Helvetica", 25, "bold italic"))
    myLabel3 = Label(frame, text="Choose your user", font=("Helvetica", 16, "bold italic"))
    blankLabel = Label(frame, font=("Helvetica", 25, "bold italic"))


    # TODO create a intermediate function to choose between create User and workout frame
    myButton1 = Button(frame, width=8, height=5, text=user1, padx=15, pady=15, fg="blue", command=lambda:intermediateFunction(1), font=("Helvetica", 14, "bold italic"))
    myButton2 = Button(frame, width=8, height=5, text=user2, padx=15, pady=15, fg="blue", command=lambda:intermediateFunction(2), font=("Helvetica", 14, "bold italic"))
    myButton3 = Button(frame, width=8, height=5, text=user3, padx=15, pady=15, fg="blue", command=lambda:intermediateFunction(3), font=("Helvetica", 14, "bold italic"))
    myButton4 = Button(frame, width=12, text="Edit Users", padx=20, pady=15, fg="blue", command=deleteUserFunc)


    myLabel1.grid(row=0, column=1, padx=20, pady=(50,10))
    # myLabel2.grid(row=0, column=1)
    myLabel3.grid(row=1, column=1)
    myButton1.grid(row=2, column=0)
    myButton2.grid(row=2, column=1)
    myButton3.grid(row=2, column=2)
    blankLabel.grid(row=3, column=0)
    myButton4.grid(row=3, column=1)


    #Button(frame, text="Clear", font=('Helvetica bold', 10), command=clear_frame).grid(row=2, column=0)

#Create a button to close the window
# frame.pack()

#--- MAIN OF PROGRAM
user1 = "Add User"
user2 = "Add User"
user3 = "Add User"
user1PushupsList = []
user2PushupsList = []
user3PushupsList = []
user1SquatsList = []
user2SquatsList = []
user3SquatsList = []
users = []

with open('CSV_Files/users.csv', 'r') as file:
    data = csv.reader(file)
    
    for row in data:
        users = row

with open('CSV_Files/user1Pushups.csv', 'r') as file:
    data = csv.reader(file)
    for row in data:
        user1PushupsList.append(row)
with open('CSV_Files/user2Pushups.csv', 'r') as file:
    data = csv.reader(file)
    for row in data:
        user2PushupsList.append(row)
with open('CSV_Files/user3Pushups.csv', 'r') as file:
    data = csv.reader(file)
    for row in data:
        user3PushupsList.append(row)

with open('CSV_Files/user1Squats.csv', 'r') as file:
    data = csv.reader(file)
    for row in data:
        user1SquatsList.append(row)
with open('CSV_Files/user2Squats.csv', 'r') as file:
    data = csv.reader(file)
    for row in data:
        user2SquatsList.append(row)
with open('CSV_Files/user3Squats.csv', 'r') as file:
    data = csv.reader(file)
    for row in data:
        user3SquatsList.append(row)
        

# with open('CSV_Files/user1Pushups.csv', 'r') as file:
#     data = csv.reader(file)
#     i=0
#     for row in data:
#         if i==0:
#             users = row
#         elif i==1:
#             user1PushupsList = [int(x) for x in row]
#         elif i==2:
#             user2PushupsList = [int(x) for x in row]
#         elif i==3:
#             user3PushupsList = [int(x) for x in row]
#         i+=1

# with open('CSV_Files/user1Pushups.csv', 'r') as file:
#     data = csv.reader(file)
#     i=0
#     for row in data:
#         if i==0:
#             users = row
#         elif i==1:
#             user1PushupsList = [int(x) for x in row]
#         elif i==2:
#             user2PushupsList = [int(x) for x in row]
#         elif i==3:
#             user3PushupsList = [int(x) for x in row]
#         i+=1

buttonPress = 0
# options = []

workingOut = workingOutSkeleton()
optionWorkout = 0
if users:
    user1 = users[0]
    user2 = users[1]
    user3 = users[2]

root= Tk()
frame = mainFrame(root)


#Set the geometry of frame
root.geometry("700x400")

root.mainloop()