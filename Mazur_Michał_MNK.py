import matplotlib.pyplot as plt
import numpy as np

def Mazur_Michał_mnoz_mac(A,B):
    if (len(A[0])==len(B)): #sprawdzam czy zgadzają się wymiary macierzy
        wynik=[[0]*len(B[0]) for i in range(len(A))]
        for i in range(len(A)): #po wierszach z A
            for j in range(len(B[0])):  #po kolumnach z B
                for k in range(len(B)): #lub range(len(A[0]))            
                        wynik[i][j]+=A[i][k]*B[k][j]               
        return wynik
    


def Mazur_Michał_gauss_pivot(A,b):
    for i in range(0,len(A)-1):

        if A[i][i]==0: #Sprawdzam czy niezerowy element na diagonali
            ####
            maxabs_el=0
            index=0
            for k in range(i+1,len(A)): #Znajdowanie elementu najwiekszego co do modułu w kolumnie
                if abs(A[k][i])>maxabs_el:
                    maxabs_el=A[k][i]
                    index=k                 

            b[i],b[index]=b[index],b[i] #zamiana elementów wyrazu wolnego
            
            for z in range(0,len(A[0])):
                A[i][z],A[index][z]=A[index][z],A[i][z] #zamiana wierszy macierzy A
            ###
                
        for j in range(i+1,len(A)): #eliminacja Gaussa
            mnoznik=A[j][i]/A[i][i]
            b[j]-=b[i]*mnoznik
            for k in range(i,len(A[0])):
                A[j][k]=A[j][k]-mnoznik*A[i][k]
    return A,b

def Mazur_Michał_ukladU(U,b):
    wynik=[0 for i in range(len(U))]
    n=len(U[0])
    for i in range(1,len(U)+1):
        suma=0
        for j in range(1,i):
            suma+=U[n-i][n-j]*wynik[n-j]
        wynik[n-i]+=(b[n-i]-suma)/U[n-i][n-i]
    return wynik

def MNK(x,y,k):
    n=len(x)
    A=[[1 for i in range(k+1)] for j in range(n)]
    for i in range(0,n):
        for j in range(0,k):
            A[i][j+1]=(x[i])**(j+1)
    AT=[[1 for i in range(n)] for j in range(k+1)]
    #print(A)
    
    for i in range(0,n+1):
        for j in range(0,k):
            AT[i][j]=A[j][i]
    #print(AT)
    
    ATA=Mazur_Michał_mnoz_mac(AT,A)
    print("ATA",ATA)  
    
    yt=[[y[i]]  for i in range(len(y))]
    #print(yt)
    ATY=Mazur_Michał_mnoz_mac(AT,yt)
    #print(ATY)  
    ATYt=[ATY[i][0] for i in range(len(ATY))]
    
    print("ATYt",ATYt)
    U=Mazur_Michał_gauss_pivot(ATA,ATYt)[0]
    b=Mazur_Michał_gauss_pivot(ATA,ATYt)[1]
    print(Mazur_Michał_ukladU(U, b))
    return Mazur_Michał_ukladU(U, b)
    
def Rysujwielomian(A):
    x_wielomian=np.linspace(-1,5,1000)
    print(x_wielomian)
    y_wielomian=np.linspace(0,0,1000)
    print(y_wielomian[0]+x_wielomian[1])
    for i in range(len(y_wielomian)):
        for j in range(len(A)):
            y_wielomian[i]+=A[j]*x_wielomian[i]**(j)
    for i in range(len(x)):
        plt.plot(x[i],y[i],'o',label='x')
    plt.plot(x_wielomian,y_wielomian,'-',label='wielomian')
        
    
x=[2,3,4,5]
y=[3,4,1,7] 
P=MNK(x,y,4)
Rysujwielomian(P)
