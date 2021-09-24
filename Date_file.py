#Kan benyttes i forbindelse med lyskryds, køre over for rødt!!!!!
import Gmail_file
from datetime import datetime

#from picamera import PiCamera

#camera=PiCamera()
d=datetime.today()
#d = datetime.datetime.now()

#date=calendar.month_name(d.month)
print(d)
#date = calendar.month_name(d.month)
date = str(d.year) + "_" + str(d.month)+"_"+ str(d.day) + "_" + str(d.hour) + ":" + str(d.minute) + ":" + str(d.second)

print(date)
