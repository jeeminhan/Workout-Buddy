# from datetime import datetime
# from datetime import timedelta
# # Get current time in local timezone
# current_time = datetime.now()
# print('Current Time: ', current_time)
# # Subtract 2 hours from datetime object containing current time
# # Convert datetime object to string in specific format 
# final_time = current_time - timedelta(days=5)

# past_time_str = final_time.strftime('%m-%d-%Y %H:%M')
# print('Past Time as string object: ', past_time_str)

# from Tkinter import *

# root = Tk()
# frame = Frame(root)
# frame.pack()

# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )

# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)

# greenbutton = Button(frame, text="Brown", fg="brown")
# greenbutton.pack( side = LEFT )

# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )

# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)

# root.mainloop()

# Import Module
from tkinter import *
 
# Create Object
root = Tk()
 
# Add Title
root.title('On/Off Switch!')
 
# Add Geometry
root.geometry("500x300")
 
# Keep track of the button state on/off
#global is_on
is_on = True
 
# Create Label
my_label = Label(root,
    text = "The Switch Is On!",
    fg = "green",
    font = ("Helvetica", 32))
 
my_label.pack(pady = 20)
 
# Define our switch function
def switch():
    global is_on
     
    # Determine is on or off
    if is_on:
        on_button.config(image = off)
        my_label.config(text = "The Switch is Off",
                        fg = "grey")
        is_on = False
    else:
       
        on_button.config(image = on)
        my_label.config(text = "The Switch is On", fg = "green")
        is_on = True
 
# Define Our Images
on = PhotoImage(file = "on.png")
off = PhotoImage(file = "off.png")
 
# Create A Button
on_button = Button(root, image = on, bd = 0,
                   command = switch)
on_button.pack(pady = 50)
 
# Execute Tkinter
root.mainloop()