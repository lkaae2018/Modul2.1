import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.IN)

def my_callback(channel):
    if GPIO.input(25):
        print("LED er tændt!")
    else:
        print("LED slukket!")

GPIO.add_event_detect(25, GPIO.BOTH, callback=my_callback)

try:
    sleep(30)
    print("Slut!")
    
    
finally:
    GPIO.cleanup()
        
