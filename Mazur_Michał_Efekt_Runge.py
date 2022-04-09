import numpy as np
from scipy.interpolate import interp1d
from scipy.interpolate import pchip_interpolate
import matplotlib.pyplot as plt

######################


def Mazur_Michal_Lagrange(xw,yw,x):
        y1=0
        n=len(xw)
        for i in range(0,n):
            p=1
            for j in range(0,n):
                if i!=j:
                    p=p*((x-xw[j])/(xw[i]-xw[j]))
            y1+=p*yw[i]
        return y1
            




def Nazwisko_Imie_Efekt_Runge(k):
    error=[[0 for i in range(1000)] for j in range(k)]
    for k2 in range(0,k):
        x1=np.linspace(-1,1,2*(k2+1)+1)  
        y1=abs(x1)
        xLag=np.linspace(-1,1,1000)
        yLag=Mazur_Michal_Lagrange(x1,y1,xLag)
        error[k2]=abs(abs(xLag)-Mazur_Michal_Lagrange(x1,y1,xLag))
        plt.plot(xLag,yLag,'-',label=k2+1) 
    plt.plot(x1,y1,'-',label='x')
    plt.legend()
    plt.show()
    for k2 in range(0,k):
        plt.plot(xLag,error[k],'-',label=k2+1)  
    plt.legend()
    plt.show()


        


Nazwisko_Imie_Efekt_Runge(5)
    



    
    