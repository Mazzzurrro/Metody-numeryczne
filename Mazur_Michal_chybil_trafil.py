import math
import random
def f(x):
    return math.sin(x)

def Mazur_Michal_chybil_trafil(a,b,n):
    pole=2*math.pi
    trafione = 0
    for i in range(n):
        x=a+(b-a)*random.random()
        y=-1+2*random.random()
        if (y>0):
            if (f(x)>=y):
                trafione+=1
        if(y<0):
            if (f(x)<=y):
                trafione-=1
    return (trafione/n)*pole
print(Mazur_Michal_chybil_trafil(0,math.pi,1000000))
