from datetime import datetime
from datetime import timedelta
# Get current time in local timezone
current_time = datetime.now()
print('Current Time: ', current_time)
# Subtract 2 hours from datetime object containing current time
# Convert datetime object to string in specific format 
past_time_str = current_time.strftime('%m-%d-%Y %H:%M')
print('Past Time as string object: ', past_time_str)
