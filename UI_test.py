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
        Frame1(root)


    myLabel1 = Label(frame, text="You are now working out", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)
    myButton1 = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton1.grid(row=1, column=0)

def Frame2(root):

    #Create a frame
    frame = Frame(root)
    frame.grid(row=1, column=2)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        Frame1(root)


    myLabel1 = Label(frame, text="Choose Username", fg="blue", bg="#f5f5dc")
    myLabel1.grid(row=0, column=0)
    myButton1 = Button(frame, text="Done", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
    myButton1.grid(row=1, column=0)

def Frame1(root):
    def createUser():
        for widgets in frame.winfo_children():
            widgets.destroy()
        Frame2(root)

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

    myButton1 = Button(frame, text="Add User", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=createUser)
    myButton2 = Button(frame, text="Add User", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=startWorkout)
    myButton3 = Button(frame, text="Add User", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=createUser)

    myLabel1.grid(row=0, column=0)
    myLabel2.grid(row=0, column=1)
    myButton1.grid(row=1, column=0)
    myButton2.grid(row=1, column=1)
    myButton3.grid(row=1, column=2)

    #Button(frame, text="Clear", font=('Helvetica bold', 10), command=clear_frame).grid(row=2, column=0)

#Create a button to close the window
# frame.pack()

root= Tk()

frame = Frame1(root)

#Set the geometry of frame
root.geometry("600x250")

root.mainloop()