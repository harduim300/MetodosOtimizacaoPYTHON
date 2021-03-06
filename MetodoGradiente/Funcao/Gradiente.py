import numpy as np
from inicializar import Init
def GradienteExE ():
    Xn = Init.X_0
    it = 0
    Aux = Xn[0]
    cont = [0]
    while(it < Init.cont):
        cont.append(it+1)    
        #------------------------------------------------------
        # Definição de Busca (Usando Gradiente):
        #------------------------------------------------------
        # d = - ▼ f(x1,x2)
        d =  - np.array([f1x(Xn[it][0],Xn[it][1]),f1y(Xn[it][0],Xn[it][1])])
        #------------------------------------------------------
        # Yj+1 = yj + λd1
        #------------------------------------------------------
        Aux = Aux + lambDaNewton(Aux,d)*d
        Xn = np.vstack([Xn,Aux])
        #------------------------------------------------------
        # Critério de Parada
        #------------------------------------------------------
        # |∇f (x)| < E
        #------------------------------------------------------
        if np.sqrt(np.dot(d,d)) < Init.E:
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
# ---------------------------------------------------------------