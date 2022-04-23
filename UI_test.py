# from tkinter import *

# # --- functions ---

# def create_frame(master):
#     print("create frame")

#     frame = Frame(master)

#     b = Button(frame, text='Do Something')
#     b.pack(pady=10)
#     myLabel1 = Label(frame, text="Welcome to", fg="blue", bg="#f5f5dc", font=("Arial", 25))
#     myLabel1.pack()

#     clearall = Button(frame, text='reset', command=reset_all)
#     clearall.pack(pady=10)

#     return frame

# def reset_all():
#     global frame

#     frame.destroy()
#     frame = create_frame(master)
#     #frame = create_different_frame(master)
#     frame.pack()

# # --- main ---


# master = Tk()

# frame = create_frame(master)
# frame.pack()

# mainloop()

#Import the required libraries
from tkinter import *
import csv, random

def workingOutSkeleton():
    random.seed()
    num = random.randint(1,50)
    return num
#Create an instance of tkinter frame


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

    doneButton = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    doneButton.grid(row=2, column=0)
    
def workoutFrame(root, userNum):
    #Create a frame
    frame = Frame(root)
    frame.grid(row=1, column=2)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        
        userInfoFrame(root)
    filename = "data.csv"
    def saveWorkout():
        with open(filename, 'w') as csvfile: 
        # creating a csv writer object 
            csvwriter = csv.writer(csvfile) 
        
            if userNum==1:
                user1Pushups.append(pushupsDone)
                csvwriter.writerow(user1Pushups)

            elif userNum==2:
                user2Pushups.append(pushupsDone)
                csvwriter.writerow(user2Pushups)
            elif userNum==3:
                user2Pushups.append(pushupsDone)
                csvwriter.writerow(user3Pushups)

    pushupsDone = workingOutSkeleton()

    myLabel1 = Label(frame, text="Your workout will now begin", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)
    myButton2 = Button(frame, text="Save Workout (This will end your workout session)", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=saveWorkout)
    myButton2.grid(row=1, column=0)
    myButton2 = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton2.grid(row=2, column=0)

def userInfoFrame(root, userNum):
    # TODO show workout stats on this page
    frame = Frame(root)
    frame.grid(row=1, column=2)

    currentUser = ""
    pushupsDone = 0
    if userNum==1:
        currentUser = user1
        pushupsDone = sum(user1Pushups)
    elif userNum==2:
        currentUser = user2
        pushupsDone = sum(user2Pushups)
    elif userNum==3:
        currentUser = user3
        pushupsDone = sum(user3Pushups)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        mainFrame(root)
    
    def workout():
        for widgets in frame.winfo_children():
            widgets.destroy()
        workoutFrame(root, userNum)



    myLabel1 = Label(frame, text="Welcome " + currentUser+ " you can view your workout stats or start a workout", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)
    myLabel2 = Label(frame, text= "You've done " + str(pushupsDone) + " pushups", fg="blue", bg="#f5f5dc")
    myLabel2.grid(row=1, column=0)
    myButton1 = Button(frame, text="Start workout" , padx=20, pady=15, fg="blue", bg="#f5f5dc", command=workout)
    myButton1.grid(row=2, column=0)
    myButton1 = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton1.grid(row=3, column=0)

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
        print(userNum)

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
user1Pushups = 0
user2Pushups = 0
user3Pushups = 0
users = []
with open('data.csv', 'r') as file:
    data = csv.reader(file)
    i=0
    for row in data:
        if i==0:
            users = row
        elif i==1:
            user1Pushups = [int(x) for x in row]
        elif i==2:
            user2Pushups = [int(x) for x in row]
        elif i==3:
            user3Pushups = [int(x) for x in row]
        i+=1

# print(user1Pushups, user2Pushups, user3Pushups) 

workingOut = workingOutSkeleton()
print(workingOut)

user1 = users[0]
user2 = users[1]
user3 = users[2]

root= Tk()
frame = mainFrame(root)


#Set the geometry of frame
root.geometry("600x250")

root.mainloop()