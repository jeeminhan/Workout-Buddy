# from tkinter import *

# from tkinter import messagebox

# top = Tk()
# top.geometry("500x500")
# def helloCallBack():
#    msg = messagebox.showinfo( "Hello Python", "Hello World")

# top.Label(frm, text="Hello World!").grid(column=0, row=0)
# B = Button(top, text = "Hello", command = helloCallBack)
# B.place(x = 50,y = 50)
# top.mainloop()

# from tkinter import *
# # from tkinter import ttk
# root = Tk()

# frame = tk.Frame(root, padding=10)
# frame.grid()
# tk.Label(frame, text="Login").grid(column=0, row=0)
# # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
#size of the window
# root.geometry("400x400")

# app = Window(root)
# root.mainloop()


from tkinter import *
# from tkinter import ttk
root = Tk()

e = Entry(root, width=50)


def myClick():
    
    # myLabel = Label(root, text="Look I clicked a button!"+e.get())
    # myLabel.grid(row=3, column=2)
    pass

myLabel1 = Label(root, text="Welcome to", fg="blue", bg="#f5f5dc", font=("Arial", 25))
myLabel2 = Label(root, text="Workout Buddy!", fg="blue", bg="#f5f5dc", font=("Arial", 25))

#myLabel2 = Label(root, text="User!")
#bg does not work
myButton1 = Button(root, text="Add User", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
myButton2 = Button(root, text="Add User", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)
myButton3 = Button(root, text="Add User", padx=20, pady=15, fg="blue", bg="#f5f5dc", command=myClick)

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myButton1.grid(row=1, column=0)
myButton2.grid(row=1, column=1)
myButton3.grid(row=1, column=2)


# e.grid(row=3, column=1)
# What does this do again?
# e.get


# myLabel.pack()
root.geometry("700x700")
root.mainloop()
