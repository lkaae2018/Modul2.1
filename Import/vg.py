import random

def maaling():
    print("Udføre måling!!!")
    #måle program skallige her
    global maal
    maal=random.randrange(1,50)
    return


while True:
    b=input('''Tryk på en tast for at fortage måling?
    Der må ikke være noget på vægten!!!''')
    maaling()
    nulmaal=maal
    print("Nulmåling="+str(nulmaal))
    a=input("læg emner på vægten!!")
    maaling()
    print("mål="+str(maal))
    maal=maal-nulmaal
    print("Emnet vejer:"+str(maal)+"gram")
    a=int(input('Tryk på 1 for at forsætte ellers 0 for stoppe? '))
    if a==0:
        break
