A=[[7,2,3,1],[1,11,4,1],[1,12,32,1],[1,1,3,15]]
b=[1,1,1,1]

def Mazur_Michał_Jacobi(A,b,eps):
    xp=[1 for i in range(len(b))]
    #sprawdzam czy jest diagonalnie dominująca
    dominujaca=1
    for i in range(len(A)):
        suma=0
        for j in range(len(A[0])):
            if i!=j:
                suma+=A[i][j]
        if A[i][i]<suma:
            dominujaca=0
    # Wyliczam elementy x(k+1) jeżeli zbieżna
    if dominujaca==1:
        epsilon=100
        while epsilon>eps:
            xk=[0 for i in range(len(b))]
            for i in range(len(xp)):
                xk[i]=b[i]
                for j in range(len(A)):
                    if i!=j:
                        xk[i]-=A[i][j]*xp[j]
                xk[i]*=1/A[i][i]
            #przypisuje elementy x(k+1) jako elementy x(k) w kolejnej
            #iteracji
            for i in range(len(xp)):
                xp[i]=xk[i]
            print(xp)

        #obliczanie błędów:
            r=[0 for i in range(len(xp))]
            for i in range(len(xp)):
                r[i]=b[i]
                for j in range(len(xp)):
                    r[i]-=A[i][j]*xp[j]
            #szukanie maksymalnego błędu
            epsilon=abs(r[0])        
            for i in range(len(r)):
                if abs(r[i])>epsilon:
                    epsilon=abs(r[i])
    else:
        print("Metoda nie jest zbiezna dla macierzy A")
    
    
Mazur_Michał_Jacobi(A,b,0.1)          
