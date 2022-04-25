#Import the required libraries
from tkinter import *
import csv, random
import time
from datetime import datetime
from datetime import timedelta
import ast
import workout_bud


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
    frame.grid(row=1, column=2)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        mainFrame(root)


    myLabel1 = Label(frame, text="Which user would you like to delete?", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)

    myButton1 = Button(frame, text=user1, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton2 = Button(frame, text=user2, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton3 = Button(frame, text=user3, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton1.grid(row=1, column=0)
    myButton2.grid(row=1, column=1)
    myButton3.grid(row=1, column=2)

    doneButton = Button(frame, text="Back", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    doneButton.grid(row=2, column=0)
    
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
    frame.grid(row=1, column=2)

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
        myButton3.destroy()
        time.sleep(0.25)
        userInfoFrame(root, userNum)

    # finalTimeVar, repsVar, totalScoreVar, paramListVar = workingOutSkeleton()

    myLabel1 = Label(frame, text="Choose Push-up or Squats", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)

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
        finalTimeVar, repsVar, totalScoreVar, paramListVar = workingOutSkeleton()
        myButton1.destroy()
        myButton2.destroy()
        myButton4.destroy()



        # finalTimeVar, repsVar, totalScoreVar, paramListVar = workout_bud.workout(1)
    def startSquats():
        global optionWorkout
        optionWorkout = 2
        global finalTimeVar, repsVar, totalScoreVar, paramListVar
        finalTimeVar, repsVar, totalScoreVar, paramListVar = workingOutSkeleton()
        myButton1.destroy()
        myButton2.destroy()
        myButton4.destroy()

        # finalTimeVar, repsVar, totalScoreVar, paramListVar = workout_bud.workout(2)   

    # RB1 = Radiobutton(frame, text="Push-Ups", variable=r, value=1, command=lambda: radioButtonPress(r.get()))
    # RB1.grid(row=1, column=0)
    # RB2 = Radiobutton(frame, text="Squats", variable=r, value=2, command=lambda: radioButtonPress(r.get()))
    # RB2.grid(row=2, column=0)
    myButton1 = Button(frame, text="Start Pushups", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=startPushups)
    myButton1.grid(row=1, column=0)
    myButton2 = Button(frame, text="Start Squats", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=startSquats)
    myButton2.grid(row=1, column=1)
    myButton3 = Button(frame, text="Save Workout (This will end your workout session)", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=lambda:saveWorkout(repsVar, totalScoreVar, paramListVar))
    myButton3.grid(row=3, column=0)
    myButton4 = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton4.grid(row=4, column=0)
    
def showStats(root, userNum, dateRow):
    frame = Frame(root)
    # WHAT DOES THIS DO?
    frame.grid(row=1, column=2)

    pushUpRep = []
    pushUpList = []
    parameter1 = []
    parameter2 = []
    parameter3 = []
    parameter4 = []
    avgScore = []



    
    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        userInfoFrame(root, userNum)

    if userNum==1:
        pushUpList = user1PushupsList
    elif userNum==2:
        pushUpList = user2PushupsList
    elif userNum==3:
        pushUpList = user3PushupsList
    # Getting the specific row
    pushUpList = pushUpList[int(dateRow)][3]
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
        parameter4.append(pushUpList[i][3])
        avg = ((pushUpList[i][0]+pushUpList[i][1]+pushUpList[i][2]+pushUpList[i][3])/4)
        avg = "{avg:.2f}".format(avg=avg)
        avgScore.append(avg)


        
    myButton2 = Button(frame, text="Back", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton2.grid(row=1, column=0)
    test = Text(frame, width=60, height=15)
    test.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    #ADDING A SCROLLBAR
    # myscrollbar=Scrollbar(frame, orient="vertical")
    # myscrollbar.grid(row=2, column = 0,fill="y")

    test.delete(1.0,END)   # Delete text from widget if there is any
    test.insert(END,'Rep:   Avg Score:    P1   P2    P3    P4:\n')
    for index in range(len(pushUpRep)):
        col1 = '{:<8}'.format(pushUpRep[index])
        col2 = '{:<8}'.format(avgScore[index])
        col3 = '{:<5}'.format(parameter1[index])
        col4 = '{:<5}'.format(parameter2[index])
        col5 = '{:<5}'.format(parameter3[index])
        col6 = '{:<5}'.format(parameter4[index])
        line = col1 + col2 + col3 + col4 + col5 + col6+ '\n'
        test.insert(END,line)

    

def viewStatsFrame(root, userNum):
    pushUpList = []
    options = []
    frame = Frame(root)
    frame.grid(row=1, column=2)

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
        showStats(root, userNum, optionChosenNum)

    
    if userNum==1:
        pushUpList = user1PushupsList
    elif userNum==2:
        pushUpList = user2PushupsList
    elif userNum==3:
        pushUpList = user3PushupsList
    for row in pushUpList:
        options.append(row[0])
    clicked = StringVar()

    myLabel1 = Label(frame, text="Stats Menu", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)

    drop = OptionMenu(frame, clicked, *options)
    drop.grid(row=1, column=0)

    myButton1 = Button(frame, text="Choose Date", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=show)
    myButton1.grid(row=2, column=0)

    myButton2 = Button(frame, text="Back", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
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
    frame.grid(row=1, column=2)

    currentUser = ""
    pushupsDone = 0
    if userNum==1:
        currentUser = user1
        if user1PushupsList[0] != '':
            for i in range(len(user1PushupsList)):
                pushupsDone += int(user1PushupsList[i][1])
        
        
    elif userNum==2:
        currentUser = user2
        if user1PushupsList[0] != '':
            for i in range(len(user2PushupsList)):
                pushupsDone += int(user2PushupsList[i][1])
        
    elif userNum==3:
        currentUser = user3
        if user1PushupsList[0] != '':
            for i in range(len(user3PushupsList)):
                pushupsDone += int(user3PushupsList[i][1])
        

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        mainFrame(root)
    
    def workout():
        for widgets in frame.winfo_children():
            widgets.destroy()
        workoutFrame(root, userNum)
    
    def viewStats():
        for widgets in frame.winfo_children():
            widgets.destroy()
        viewStatsFrame(root, userNum)



    myLabel1 = Label(frame, text="Welcome " + currentUser+ " you can view your workout stats or start a workout", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)
    myLabel2 = Label(frame, text= "You've done " + str(pushupsDone) + " pushups total!", fg="blue", bg="#f5f5dc")
    myLabel2.grid(row=1, column=0)
    myButton1 = Button(frame, text="Workout" , padx=20, pady=15, fg="blue", bg="#f5f5dc", command=workout)
    myButton1.grid(row=2, column=0)
    myButton1 = Button(frame, text="View Stats" , padx=20, pady=15, fg="blue", bg="#f5f5dc", command=viewStats)
    myButton1.grid(row=3, column=0)
    myButton1 = Button(frame, text="Back", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton1.grid(row=4, column=0)

def createUserFrame(root, userNum):
    #Create a frame
    frame = Frame(root)
    frame.grid(row=1, column=2)

    def myClick():
        newUser = e.get()
        for widgets in frame.winfo_children():
            widgets.destroy()
        if userNum==1:
            global user1
            user1 = newUser
        elif userNum==2:
            global user2
            user2 = newUser
        elif userNum==3:
            global user3
            user3 = newUser

        #return newUser
        # user = newUser
        mainFrame(root)
        


    myLabel1 = Label(frame, text="Choose Username", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)
    e = Entry(frame, width=50)
    e.grid(row=1, column=0)
    myButton1 = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton1.grid(row=2, column=0)

def mainFrame(root):
    #Create a frame
    frame = Frame(root)
    frame.grid(row=1, column=2)
                
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
    myLabel1 = Label(frame, text="Welcome to", fg="blue", bg="#f5f5dc", font=("Arial", 25))
    myLabel2 = Label(frame, text="Workout Buddy!", fg="blue", bg="#f5f5dc", font=("Arial", 25))
    myLabel3 = Label(frame, text="Choose your user", font=("Arial", 10))
    blankLabel = Label(frame, font=("Arial", 10))


    # TODO create a intermediate function to choose between create User and workout frame
    myButton1 = Button(frame, text=user1, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=lambda:intermediateFunction(1))
    myButton2 = Button(frame, text=user2, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=lambda:intermediateFunction(2))
    myButton3 = Button(frame, text=user3, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=lambda:intermediateFunction(3))
    myButton4 = Button(frame, text="Edit Users", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=deleteUserFunc)


    myLabel1.grid(row=0, column=0)
    myLabel2.grid(row=0, column=1)
    myLabel3.grid(row=1, column=0)
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


workingOut = workingOutSkeleton()
optionWorkout = 0
if users:
    user1 = users[0]
    user2 = users[1]
    user3 = users[2]

root= Tk()
frame = mainFrame(root)


#Set the geometry of frame
root.geometry("800x400")

root.mainloop()