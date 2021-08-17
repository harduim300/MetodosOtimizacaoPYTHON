import numpy as np
from inicializar import Init
def RossenbrockExE ():
    Xn = Init.X_0
    it = 0
    Aux = Xn
    cont = [0]
    while(it < Init.cont):
        cont.append(it+1)    # Pega quantas iterações foram feitas
        #------------------------------------------------------
        # Definição de Busca exploratória:
        #------------------------------------------------------
        if it == 0:
            lamb = np.array(0)
            d = Init.np.array([[1.0,0.0],[0.0,1.0]])
            for i in range(2): 
                lamb = np.vstack([lamb,lambDaNewton(Aux,d[i])])
                Aux = Aux + lambDaNewton(Aux,d[i])*d[i]
                Xn = np.vstack([Xn,Aux])
            it += 1
        #------------------------------------------------------
        # Definição de Busca (Usando Gram-Schimct):
        #------------------------------------------------------
        for i in range(2):
            if i == 0:
                a =  np.array(lamb[len(lamb)-1]*d[len(d)-1] + lamb[len(lamb)-2]*d[len(d) - 2])
                b = a / ((a[0]**2 + a[1]**2)**(1/2))
                d = np.vstack([d,b])
            else:
                a =  np.array(lamb[len(lamb)-1]*d[len(d)-1] + lamb[len(lamb)-2]*d[len(d) - 2])
                b = (a - (a[0]*d[len(d)-1][0] + a[1]*d[len(d)-1][1])*d[len(d)-1])/ ((a[0]**2 + a[1]**2)**(1/2))
                d = np.vstack([d,b])
            lamb = np.vstack([lamb,lambDaNewton(Aux,d[len(d)-1])])
            Aux = Aux + lambDaNewton(Aux,d[len(d)-1])*d[len(d)-1]
            Xn = np.vstack([Xn,Aux])
        #------------------------------------------------------
        # Critério de Parada
        #------------------------------------------------------
        # if np.all(np.fabs(Xn[len(Xn)-1] - Xn[len(Xn) - 2]) < Init.E):
        #      break
        it += 1
        #------------------------------------------------------
    print("| i |",cont,"|")
    print("----------------------------------------------")
    print("| Xn |")
    print("----------------------------------------------")
    print(Xn)
    print("----------------------------------------------")
    #--------------------------------------------------------
    # O dados serão escritos respectivamente 
    # - 0 : Meu ponto inicial
    # - 1 : Primeira iteração usando busca exploratória (em pares)
    # - 2..n : Minhas iterações usando direções definidas por Gram-Schimdt (em pares)
    #--------------------------------------------------------



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

