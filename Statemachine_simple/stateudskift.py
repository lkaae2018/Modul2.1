from random import random
from time import sleep

def lysgreen():
    print ("Grøn:")
        # Sleep er en forsinkelse af programmet
    sleep(1.5)
    tal=random()
    if tal>.5:
        return lysyellow()
    else:
        return lysred()

def lysyellow():
    print ("Gul:")
    # Sleep er en forsinkelse af programmet
    tal=random()
    if tal>.5:
        return lysgreen()
    else:
        return lysred()

def lysred():
    print ("Rød:")
    # Sleep er en forsinkelse af programmet
    sleep(1.5)
    tal=random()
    if tal>.2:
        return lysgreen()
    else:
        return None

lys=lysgreen()    # initial state
while lys: lys=lys()  # launch state machine
print ("Done with states")
