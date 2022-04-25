from datetime import datetime
from datetime import timedelta
# Get current time in local timezone
current_time = datetime.now()
print('Current Time: ', current_time)
# Subtract 2 hours from datetime object containing current time
# Convert datetime object to string in specific format 
final_time = current_time - timedelta(days=5)

past_time_str = final_time.strftime('%m-%d-%Y %H:%M')
print('Past Time as string object: ', past_time_str)

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