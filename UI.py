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
    myLabel = Label(root, text="Look I clicked a button!"+e.get())
    myLabel.grid(row=1, column=2)

myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="User!")
#bg does not work
myButton = Button(root, text="Enter Your Name!", padx=50, pady=50, fg="blue", bg="#f5f5dc", command=myClick)

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myButton.grid(row=2, column=0)

e.grid(row=3, column=1)
e.get


# myLabel.pack()
root.geometry("600x600")
root.mainloop()
