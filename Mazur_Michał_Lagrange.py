import numpy as np
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

x1=np.linspace(-1,1,11)  
y1=abs(x1)
xLag=np.linspace(-1,1,1000)
print(Mazur_Michal_Lagrange(x1,y1,xLag))
