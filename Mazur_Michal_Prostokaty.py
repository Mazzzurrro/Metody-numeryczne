import math
import random
def f(x):
    return math.sin(x)
def Mazur_Michal_prostokaty(a,b,n):
    h=(b-a)/n
    xp=a
    suma=0
    while xp<b:
        suma+=f(xp)*h
        xp+=h
    return suma
print("Metoda prostokatow:",Mazur_Michal_prostokaty(0,math.pi,10000))
