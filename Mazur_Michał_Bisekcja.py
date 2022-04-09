def f(x):
    return (x-2)*(x-4)*(x+3)
def fp(x):
    return (x-4)*(x+3)+(x-2)*(x+3)+(x-2)*(x-4)
def Mazur_Michał_Bisekcja(a,b):
    if f(a)*f(b)<0:
        c=(a+b)/2
        while f(c)!=0:            
            if f(a)*f(c)<0:
                b=c
            elif f(b)*f(c)<0:
                a=c
        return c
print(Bisekcja(3,5))