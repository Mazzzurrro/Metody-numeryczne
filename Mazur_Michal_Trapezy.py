import math
import random
def f(x):
    return math.sin(x)
def Mazur_Michal_trapezy(a,b,n):
    h=(b-a)/n
    xp=a
    suma=0
    while xp<b:
        suma+=(f(xp)+f(xp+h))*h/2
        xp+=h
    return suma
print("Metoda trapezow:",Mazur_Michal_trapezy(0,math.pi,10000))
