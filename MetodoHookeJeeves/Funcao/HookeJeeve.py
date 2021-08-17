import numpy as np
from inicializar import Init # Como dar include em python
def HookeJeevesExE ():
    Xn = Init.X_0
    it = 0
    Aux = Xn
    cont = [0]
    while(it < Init.cont):
        cont.append(it+1)    # Pega quantas iterações foram feitas
        #------------------------------------------------------
        # Definição de Busca exploratória:
        #------------------------------------------------------
        dexp = Init.np.array([[1.0,0.0],[0.0,1.0]])
        for i in range(2): 
            Aux = Aux + lambDaNewton(Aux,dexp[i])*dexp[i]
        Xn = np.vstack([Xn,Aux])
        #------------------------------------------------------
        # Definição de Busca padrão:
        #------------------------------------------------------
        if it == 0:
            d =  np.array(Xn[len(Xn)-1] - Xn[len(Xn) - 2])
        else:
            d =  np.array(Xn[len(Xn)-1] - Xn[len(Xn) - 3])
        Aux = Aux + lambDaNewton(Aux,d)*d
        Xn = np.vstack([Xn,Aux])
        #------------------------------------------------------
        # Critério de Parada
        #------------------------------------------------------
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


# ---------------------------------------------------------------
# Método de Newton(Ajustado)
# ---------------------------------------------------------------
h = 0.01
# y'(x)
def f1x(x,Vx,d):
    return (1/(2*h))*(Init.fx(x + h,Vx,d) - Init.fx(x - h,Vx,d))
# y"(x)
def f2x(x,Vx,d):
    return (1/h**2)*(Init.fx(x + h,Vx,d) + Init.fx(x - h,Vx,d) - 2*Init.fx(x,Vx,d))
# ---------------------------------------------------------------
def lambDaNewton(Vx,d):   
    E = 0.01
    cont = 10
    X = [0.0]
    for i in range(cont):
        Newton = X[i] - (f1x(X[i],Vx,d)/f2x(X[i],Vx,d))
        X.append(Newton)
        if np.fabs(X[i+1] - X[i]) < E: # faz modulo e avalai o erro
            break
    Xr = X.pop()
    return Xr

