import time;

def green():
    while True:
        tid=time.time()
        if time.time()-tid>=3:
            tid=time.time()
            print ("Gul")
            return yellow()


def yellow():
    while True:
        tid=time.time()
        if time.time()-tid>=1:
            tid=time.time()
            print("Rød")
            return red()


def red():
    while True:
        tid=time.time()
        if time.time()-tid>=4:
            tid=time.time()
            print("Grøn")
            return green()



state=green
print("Grøn")# initial state
while state: state=green()  # launch state machine
print ("Done with states")
