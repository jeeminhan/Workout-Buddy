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

#Create an instance of tkinter frame



    
def workoutFrame(root):
    #Create a frame
    frame = Frame(root)
    frame.grid(row=1, column=2)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        mainFrame(root)


    myLabel1 = Label(frame, text="You are now working out", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)
    myButton1 = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton1.grid(row=1, column=0)


def createUserFrame(root, user):
    #Create a frame
    frame = Frame(root)
    frame.grid(row=1, column=2)

    def myClick():
        newUser = e.get()
        for widgets in frame.winfo_children():
            widgets.destroy()
        #return newUser
        user = newUser
        print(user)
        mainFrame()
        


    myLabel1 = Label(frame, text="Choose Username", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)
    e = Entry(frame, width=50)
    e.grid(row=1, column=0)
    myButton1 = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton1.grid(row=2, column=0)

def mainFrame(root, user1, user2, user3):
    def createUser(user):
        for widgets in frame.winfo_children():
            widgets.destroy()
        createUserFrame(root,user)
        print(user)

    def startWorkout():
        for widgets in frame.winfo_children():
            widgets.destroy()
        workoutFrame(root)

    #Create a frame
    frame = Frame(root)
    frame.grid(row=1, column=2)


    #Stuff in Frame
    myLabel1 = Label(frame, text="Welcome to", fg="blue", bg="#f5f5dc", font=("Arial", 25))
    myLabel2 = Label(frame, text="Workout Buddy!", fg="blue", bg="#f5f5dc", font=("Arial", 25))

    # TODO create a intermediate function to choose between create User and workout frame
    myButton1 = Button(frame, text=user1, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=lambda:createUser(user1))
    myButton2 = Button(frame, text=user2, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=lambda:createUser(user2))
    myButton3 = Button(frame, text=user3, padx=20, pady=15, fg="blue", bg="#f5f5dc", command=lambda:createUser(user3))

    myLabel1.grid(row=0, column=0)
    myLabel2.grid(row=0, column=1)
    myButton1.grid(row=1, column=0)
    myButton2.grid(row=1, column=1)
    myButton3.grid(row=1, column=2)

    #Button(frame, text="Clear", font=('Helvetica bold', 10), command=clear_frame).grid(row=2, column=0)

#Create a button to close the window
# frame.pack()

#--- MAIN OF PROGRAM
user1 = "Add User"
user2 = "Add User"
user3 = "Add User"

root= Tk()
frame = mainFrame(root)

#Set the geometry of frame
root.geometry("600x250")

root.mainloop()