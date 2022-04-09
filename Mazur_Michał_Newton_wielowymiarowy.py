import numpy as np
import matplotlib.pyplot as plt
import math
def f1rysunek(x):
    return 2*x**2-1
def f1(x,y):
    return y-2*x**2+1
def f2(x,y):
    return x**2+y**2-4
def f1_poy(x,y):
    return 1
def f1_pox(x,y):
    return -4*x
def f2_poy(x,y):
    return 2*y
def f2_pox(x,y):
    return 2*x
test = 1000
eps=0.01
x0=np.array([4,2])
test=1000
x=np.linspace(-3, 3, 200)
kat=np.linspace(0,2*math.pi,100)
x_1=[0 for i in range(100)]
x_2=[0 for i in range(100)]
for i in range(100):
    x_1[i]=2*math.cos(kat[i])
    x_2[i]=2*math.sin(kat[i])
plt.ylim(ymax = 5, ymin = -2)
plt.plot(x,f1rysunek(x),'-')
plt.plot(x_1,x_2,'-')
plt.plot(x0[0],x0[1],'o')
#plt.plot(2*math.sin(x_2),2*math.cos(x_2),'-')
while test>eps:
    f=np.array([f1(x0[0],x0[1]),f2(x0[0],x0[1])])
    print("f",f)
    mac = np.array([[f1_pox(x0[0],x0[1]),f1_poy(x0[0],x0[1])],[f2_pox(x0[0],x0[1]),f2_poy(x0[0],x0[1])]])
    print("mac",mac)
    macodw=np.linalg.inv(mac)
    print("macodw",macodw)
    macodwmn=np.matmul(macodw,f)
    print("macodwnmn",macodwmn)
   # x1[0]=x0[0]+macodwmn[0]
   # x1[1]=x0[1]+macodwmn[1]
    x1=np.array([x0[0]-macodwmn[0],x0[1]-macodwmn[1]])
    print("wynik1",x1)
   # print("wynik2",x0[1]+macodwmn[1])    
    test=abs(x1[1]-x0[1])
    print("test",test)
    x0=np.array([x1[0],x1[1]])
    plt.plot(x0[0],x0[1],'o')
    print(x0)
    print("")

