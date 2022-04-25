pushUpRep = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
percentScore = [88, 77, 88, 99, 76, 55, 44, 43, 45, 66, 11, 434]
comments = ["not bad", "pretty good", "mid", "lots to work on", "ssdfsd", "sdfsd", "sdjfskdfj", "sldfjsdfk", "ssdfs", "sd", "sdfsd", "sdf"]

from tkinter import *

root = Tk()
test = Text(root, width=40, height=15)
test.grid(padx=10, pady=10, sticky='nsew')

test.delete(1.0,END)   # Delete text from widget if there is any
test.insert(END,'Rep:   Score:     Comment:\n')
for index in range(len(pushUpRep)):
    col1 = '{:<8}'.format(pushUpRep[index])
    col2 = '{:<13}'.format(percentScore[index])
    col3 = '{}'.format(comments[index])
    line = col1 + col2 + col3 + '\n'
    test.insert(END,line)

root.mainloop()
