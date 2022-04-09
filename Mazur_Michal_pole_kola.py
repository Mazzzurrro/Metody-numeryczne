import math
import random

def Mazur_Michal_Pole_kola(r,n):
    trafione=0
    for i in range(n):
        x=r*random.random()
        y=r*random.random()
        if (x**2+y**2<=r**2):
            trafione+=1
    return 4*(trafione/n)*r*r
print(Mazur_Michal_Pole_kola(4,1000)) #wynik przyblizony
print(math.pi*16) #wynik prawidlowy
