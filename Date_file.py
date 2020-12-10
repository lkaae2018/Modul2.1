#Kan benyttes i forbindelse med lyskryds, køre over for rødt!!!!!
import calendar
import datetime
from picamera import PiCamera

camera=PiCamera()

d = datetime.today()

date = calender.month_name(d.month) + "_" + str(d.day) + "_" + str(d.year) + "_" + str(d.hour) + "_" + str(d.minute) + "_" + str(d.second)

camera.capture("/home/pi/" + date + ".jpg")
