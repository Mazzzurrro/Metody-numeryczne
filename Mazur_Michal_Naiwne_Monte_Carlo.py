import math
import random
def f(x):
    return math.sin(x)
def Mazur_Michal_Naiwne_Monte_Carlo(a,b,n):
    fsr=0
    for i in range(n):
        x=a+(b-a)*random.random()
        fsr+=f(x)
    fsr=fsr/n
    return (b-a)*fsr
print("Monte Carlo:",Mazur_Michal_Naiwne_Monte_Carlo(0,math.pi,10000))
