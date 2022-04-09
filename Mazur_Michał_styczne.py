def f(x):
    return (x-2)*(x-4)*(x+3)
def fp(x):
    return (x-4)*(x+3)+(x-2)*(x+3)+(x-2)*(x-4)
#1) Metoda stycnzych Newtona
def Mazur_Michał_styczne(x,eps):
    test=1000
    while (test>eps):
        ost=x
        x=ost-f(ost)/fp(ost)
        test = abs(x-ost)
    return(x)

print(Mazur_Michał_styczne(3,0.1))