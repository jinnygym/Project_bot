import time
from datetime import datetime, timedelta
now = datetime.now()
now = str(now)
now = now[now.find(" ")+1:now.find("."):]
delta = "00:05:00"
hour = int(time[:2:]) + int(delta[:2:])
minute = int(time[3:5:]) + int(delta[3:5:])
sec = int(time[6::]) + int(delta[6::])
alarm = hour + ":" + minute + ":" + sec
# print(now)
# print(alarm)
# print(hour)
# print(minute)
# print(sec)