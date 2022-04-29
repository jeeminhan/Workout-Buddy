# pushUpRep = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# percentScore = [88, 77, 88, 99, 76, 55, 44, 43, 45, 66, 11, 434]
# comments = ["not bad", "pretty good", "mid", "lots to work on", "ssdfsd", "sdfsd", "sdjfskdfj", "sldfjsdfk", "ssdfs", "sd", "sdfsd", "sdf"]

# from tkinter import *

# root = Tk()
# test = Text(root, width=40, height=15)
# test.grid(padx=10, pady=10, sticky='nsew')

# test.delete(1.0,END)   # Delete text from widget if there is any
# test.insert(END,'Rep:   Score:     Comment:\n')
# for index in range(len(pushUpRep)):
#     col1 = '{:<8}'.format(pushUpRep[index])
#     col2 = '{:<13}'.format(percentScore[index])
#     col2 = '{:<13}'.format(percentScore[index])

#     col3 = '{}'.format(comments[index])
#     line = col1 + col2 + col3 + '\n'
#     test.insert(END,line)

# root.mainloop()

# listTest = [22,56,33,44,55]
# listTest.sort()
# print(listTest)
from tkinter import *
import matplotlib

def finishedWorkoutScreen(root, userNum):
    frame = Frame(root)
    frame.grid(row=0, column=0)

    def myClick():
        for widgets in frame.winfo_children():
            widgets.destroy()
        # mainFrame(root)

    pushUpRep = []
    pushUpList = []
    parameter1 = []
    parameter2 = []
    parameter3 = []
    avgScore = []

    col1Total = 0
    col2Total = 0
    col3Total = 0


    if userNum==1:
        pushUpList = user1PushupsList
    elif userNum==2:
        pushUpList = user2PushupsList
    elif userNum==3:
        pushUpList = user3PushupsList
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
    print(col1Total,col2Total,col3Total)

    col1Total = col1Total/len(pushUpRep) if col1Total else 0
    col2Total = col2Total/len(pushUpRep) if col1Total else 0
    col3Total = col3Total/len(pushUpRep) if col1Total else 0
    if (col1Total == 0 and col2Total == 0 and col3Total == 0):
        topComments = "0 Pushups Done"
    else:
        topComments = workout_bud.push_up_comments(col1Total,col2Total,col3Total) 

    print(col1Total,col2Total,col3Total)

    myLabel1 = Label(frame, text="Workout Summary", font=("Helvetica", 25, "bold italic"))
    myLabel1.grid(row=0, column=0)
    myLabel1 = Label(frame, text=topComments)
    myLabel1.grid(row=1, column=0)
    doneButton = Button(frame, text="Back", padx=20, pady=15, fg="blue", command=myClick, font=("Helvetica", 25, "bold italic"))
    doneButton.grid(row=3, column=0)


    # the figure that will contain the plot
    fig = Figure(figsize = (8, 4),
                 dpi = 100)
  
    # list of squares
    x = pushUpRep
    y = avgScore
    y.sort()
    
    # adding the subplot
    plot1 = fig.add_subplot(111)
 
    # plotting the graph
    print(x)
    print(y)
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

root= Tk()
# frame = mainFrame(root)


#Set the geometry of frame
root.geometry("800x400")

root.mainloop()

finishedWorkoutScreen()