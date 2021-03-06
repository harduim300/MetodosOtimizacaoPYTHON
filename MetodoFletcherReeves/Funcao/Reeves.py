import numpy as np
from inicializar import Init
def ReevesExE ():
    Xn = Init.X_0
    it = 0
    Aux = Xn[0]
    cont = [0]
    while(it < Init.cont):
        cont.append(it+1)    
        #------------------------------------------------------
        # Definição de Busca (Usando Reeves):
        #------------------------------------------------------
        # d1 = - ▼ f(x1,x2)
        #------------------------------------------------------
        d1 =  - grad(Xn[it])
        #------------------------------------------------------
        # Yj+1 = yj + λd1
        #------------------------------------------------------
        Aux = Aux + lambDaNewton(Aux,d1)*d1
        #------------------------------------------------------
        # αj = | ▼ f(Yj+1) | / | ▼ f(Yj+1) |
        #------------------------------------------------------
        alf = alfa(grad(Aux),grad(Xn[it]))
        #------------------------------------------------------
        # d2 = - ▼ f(Yj+1) + αjd1
        #------------------------------------------------------
        d2 = - grad(Aux) + alf*d1
        #------------------------------------------------------
        # Yj+2 = yj+1 + λd2
        #------------------------------------------------------
        Aux = Aux + lambDaNewton(Aux,d2)*d2
        #------------------------------------------------------
        # x1 = yj+2
        #------------------------------------------------------
        Xn = np.vstack([Xn,Aux])
        #------------------------------------------------------
        # Critério de Parada
        #------------------------------------------------------
        # (|x1 − x0| < E)
        if np.all(np.fabs(Aux - Xn[it]) < Init.E):
            break
        #------------------------------------------------------
        # Incremento
        #------------------------------------------------------
        it += 1
        #------------------------------------------------------
    print("| i |",cont,"|")
    print("----------------------------------------------")
    print("| Xn |")
    print("----------------------------------------------")
    print(Xn)
    print("----------------------------------------------")
    #--------------------------------------------------------



# ---------------------------------------------------------------
# Método de Newton(Ajustado)
# ---------------------------------------------------------------
h = 0.01
# y'(Lambda)
def f1X(x,Vx,d):
    return (1/(2*h))*(Init.fX(x + h,Vx,d) - Init.fX(x - h,Vx,d))
#-----------------------------------------------------------------
# df/dx
#-----------------------------------------------------------------
def f1x(x,y):
    return (1/(2*h))*(Init.fx(x + h,y) - Init.fx(x - h,y))
#-----------------------------------------------------------------
# df/dy
#-----------------------------------------------------------------
def f1y(x,y):
    return (1/(2*h))*(Init.fx(x, y + h) - Init.fx(x,y - h))
#-----------------------------------------------------------------
# y"(Lambda)
def f2x(x,Vx,d):
    return (1/h**2)*(Init.fX(x + h,Vx,d) + Init.fX(x - h,Vx,d) - 2*Init.fX(x,Vx,d))
# ---------------------------------------------------------------
def lambDaNewton(Vx,d):   
    E = 0.01
    cont = 10
    X = [0.0]
    for i in range(cont):
        Newton = X[i] - (f1X(X[i],Vx,d)/f2x(X[i],Vx,d))
        X.append(Newton)
        if np.fabs(X[i+1] - X[i]) < E: # faz modulo e avalai o erro
            break
    Xr = X.pop()
    return Xr
#-----------------------------------------------------------------
# ▼ f(x1,x2)
#-----------------------------------------------------------------
def grad(Xn):
    return np.array([f1x(Xn[0],Xn[1]),f1y(Xn[0],Xn[1])])
#------------------------------------------------------
# αj = | ▼ f(Yj+1) | / | ▼ f(Yj+1) |
#------------------------------------------------------
def alfa(X1,X):
    return (np.sqrt(np.dot(X1,X1)/np.dot(X,X)))**2
#-----------------------------------------------------------------