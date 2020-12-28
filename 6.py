from math import *
def racine(x):
    if x>=0:
        a=sqrt(x)
        b=-a
        if a==0:
            return 0
        else: return a,b
    elif x<0:
        return "impossible"
    
        