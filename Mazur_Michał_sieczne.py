def f(x):
    return (x-2)*(x-4)*(x+3)
def fp(x):
    return (x-4)*(x+3)+(x-2)*(x+3)+(x-2)*(x-4)
def Mazur_Michał_sieczne(x0,x1,eps):
    test=1000
    while (test>eps):
        x=x1-(x1-x0)/(f(x1)-f(x0))*f(x1)
        test=abs(x-x1)
        x0=x1
        x1=x      
    return(x)

print(Mazur_Michał_sieczne(1,3,0.1))