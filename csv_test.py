import csv
import random
# # with open('people.csv', 'r') as file:
# #     reader = csv.reader(file)
# #     for row in reader:
# #         print(row)



# # Python program to demonstrate
# # writing to CSV
  
  
# import csv 
    
# # field names 
# # fields = ['Name', 'Branch', 'Year', 'CGPA'] 
    
# # # data rows of csv file 
# # rows = [ ['Nikhil', 'COE', '2', '9.0'], 
# #          ['Sanchit', 'COE', '2', '9.1'], 
# #          ['Aditya', 'IT', '2', '9.3'], 
# #          ['Sagar', 'SE', '1', '9.5'], 
# #          ['Prateek', 'MCE', '3', '7.8'], 
# #          ['Sahil', 'EP', '2', '9.1']] 
    
# # name of csv file 
# filename = "university_records.csv"
    
# # writing to csv file 
# with open(filename, 'w') as csvfile: 
#     # creating a csv writer object 
#     csvwriter = csv.writer(csvfile) 
    
#     csvwriter.writerow()
#     # # writing the fields 
#     # csvwriter.writerow(fields) 
        
#     # # writing the data rows 
#     # csvwriter.writerows(rows)

# filename = ""
# userNum = 1

# if userNum==1:
#     # user1PushupsList.append(pushupsDone)
#     # csvwriter.writerow(user1PushupsList)
#     filename = "CSV_Files/user1Pushups.csv"            

# elif userNum==2:
#     filename = "CSV_Files/user2Pushups.csv" 
#             # user2PushupsList.append(pushupsDone)
#             # csvwriter.writerow(user2PushupsList)
# elif userNum==3:
#     filename = "CSV_Files/user3Pushups.csv" 
#             # user2PushupsList.append(pushupsDone)
#             # csvwriter.writerow(user3PushupsList)


from datetime import datetime
from datetime import timedelta
# Get current time in local timezone
current_time = datetime.now()
print('Current Time: ', current_time)
# Subtract 2 hours from datetime object containing current time
# Convert datetime object to string in specific format 
curr_time_str = current_time.strftime('%m-%d-%Y %H:%M')
print('Current as string object: ', curr_time_str)

def saveWorkout(userNum, reps, totalScore, parameterList, timeObj=datetime.now()):
    
    
    #current_time = datetime.now()
    # Convert datetime object to string in specific format 
    curr_time_str = timeObj.strftime('%m-%d-%Y %H:%M')
    fileName = ""
    dateRepCommentList = [curr_time_str, reps, totalScore, parameterList]
    if userNum==1:
        fileName = "CSV_Files/user1Squats.csv"         
    elif userNum==2:
        fileName = "CSV_Files/user2Pushups.csv" 
    elif userNum==3:
        fileName = "CSV_Files/user3Pushups.csv" 
    with open(fileName, 'a') as csvfile: 
    # creating a csv writer object 
        csvWriter = csv.writer(csvfile) 
        csvWriter.writerow(dateRepCommentList)
        for x in parameterList:
            parameterString = ""
            for parameter in x:
                parameterString = parameterString + str(parameter) + " "
    print("workin")




def workingOutSkeleton():
    random.seed()
    randomDay = random.randint(1,1000)
    randomHour = random.randint(1,500)
    randomMin = random.randint(1,500)
    currentTime = datetime.now()
    finalTime = currentTime - timedelta(days=randomDay, hours=randomHour, minutes=randomMin)
    # finalTimeStr = finalTime.strftime('%m-%d-%Y %H:%M')
    # print(finalTimeStr)
    pushUpRep = random.randint(10,30)
    rating = random.uniform(50.1, 98.7)

    parameterList = []
    for i in range(pushUpRep):
        row = []
        for j in range(3):
            row.append(random.randint(1,100))
        parameterList.append(row)
    rating = "{rating:.2f}".format(rating=rating)
    print("workin")
    return finalTime, pushUpRep, float(rating), parameterList
#Create an instance of tkinter frame


print('jsdfsd')

finalTimeVar, repsVar, totalScoreVar, paramListVar = workingOutSkeleton()
for i in range(20):
    print("working")
    finalTimeVar, repsVar, totalScoreVar, paramListVar = workingOutSkeleton()
    saveWorkout(2, repsVar, totalScoreVar, paramListVar, finalTimeVar)

        
