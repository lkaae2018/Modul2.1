
from random import random
from time import sleep

def state0():
    print ('\x1b[7;32;40m' + "Grøn! Kør" + '\x1b[0m')
    sleep(5.5)
    return state1

def state1():
    print ('\x1b[6;30;43m' + "Gul! stop" + '\x1b[0m')
    sleep(1.5)
    return state2

def state2():
    print ('\x1b[6;30;41m' + "Rød! stop" + '\x1b[0m')
    sleep(5.5)
    return state0


state=state0    # initial state
while state: state=state()  # launch state machine
print ("Done with states")
