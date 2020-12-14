#Kan benyttes i forbindelse med lyskryds, køre over for rødt!!!!!
import calendar
from datetime import datetime

#from picamera import PiCamera

#camera=PiCamera()
d=datetime.today()
#d = datetime.datetime.now()

#date=calendar.month_name(d.month)
print(d)
date = calendar.month_name(d.month)
#date = calendar.month_name(d.month) + "_" + str(d.day) + "_" + str(d.year) + "_" + str(d.hour) + "_" + str(d.minute) + "_" + str(d.second)


