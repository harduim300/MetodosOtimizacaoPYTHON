# Bibliotecas necessárias
#pip install sympy
#pip install numpy
from sympy import *
import numpy as np
from inicializar import Init
def NewtonExE():
    Xn = Init.X_0
    it = 0
    cont = [0]
    while(it < Init.cont):
        cont.append(it+1)
        #---------------------------------------------------------  
        # f(x1,x2) 
        fx = float(Init.f(Xn[it][0],Xn[it][1]))
        #---------------------------------------------------------
        # grad = ▼ f(x1,x2)   
        grad = Init.grad(Xn[it])
        #---------------------------------------------------------
        # Hinver = H^(-1) = (1/det(H))*H
        Hinver = Init.Hinver(Xn[it])
        #---------------------------------------------------------
        # Xn = Xn-1 - ▼ f(x1,x2) * H^(-1)
        X = np.array(Xn[it] - grad*Hinver)
        Xn = np.vstack([Xn,X])
        #------------------------------------------------------
        # Critério de Parada
        #------------------------------------------------------
        # | Xn - Xn-1 | < E
        if np.all(np.fabs(Xn[len(Xn)-1] - Xn[len(Xn) - 2]) < Init.E):
            break
        it += 1
        #------------------------------------------------------
    print("| i |",cont,"|")
    print("----------------------------------------------")
    print("| Xn |")
    print("----------------------------------------------")
    print(Xn)
    print("----------------------------------------------")
    #--------------------------------------------------------






