import time;
a=1
tid=time.time()
print ("tiden er:", tid)
print("Groen")

while a==0:
    if time.time()-tid >=3:
        a=1
        tid=time.time()
        print ("Gul")
    else:
        a=0

while a==1:
    #
   if time.time()-tid >=1:
       a=2
       tid=time.time()
       print("Raed")
   else:
        a=1

while a==2:
    #print("Rød")
    if time.time()-tid>=4:
        a=0
        tid=time.time()
        print("Groen")
    else:
        a=2

