from random import *
def plus_ou_moins():
    c=0
    a=randint(1,1000)
    while c==0:
        b=int(input("Chiffre?"))
        if a>b:
            print("trop petit")
        elif a<b:
            print("trop grand")
        elif a==b:
            break
    return "Bravo c'était",a
        

