import datetime
from playsound import playsound
alarmHour = int(input("Enter Hour : "))
alarmMin = int(input("Enter Minutes : "))
alarmAm = input("AM or PM : ")

if alarmAm=="PM":
    alarmHour+=12

while True:
    if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.datetime.now().minute:
        print("Playing...")
        playsound("C:/Users/DELL/Desktop/Python/School Alarm System/sound.mp3")
        break