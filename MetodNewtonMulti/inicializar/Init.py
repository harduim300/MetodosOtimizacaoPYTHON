# Bibliotecas necessárias
#pip install sympy
#pip install numpy
from sympy import *
import numpy as np
# Dados iniciais de ponto operado , erro, iterações
X_0 = np.array([[0,3]])
E = 0.01
cont = 49
x1, x2 = symbols('x1 x2')
# ---------------------------------------------------------------
# fx (x,y):
# Substitui apenas essa função
# ---------------------------------------------------------------
expr="(x1 - 2)**4 + (x1 -2*x2)**2"
# ---------------------------------------------------------------
# associa expr a f(x1,x2)
f = lambdify([x1,x2],expr)
#-----------------------------------------------------
# ▼ f(x1,x2)
def grad(Xn):
    x = diff(expr,x1)
    y = diff(expr,x2)
    dx = lambdify([x1,x2],x)
    dy = lambdify([x1,x2],y)
    return np.matrix([[float(dx(Xn[0],Xn[1])),float(dy(Xn[0],Xn[1]))]])
# ---------------------------------------------------------------
# H^(-1) = Inverso da Hessiana
def Hinver(Xn):
    # ---------------------------------------------------------------
    # ▼^2 f(x1,x2)
    xx = diff(diff(expr,x1),x1)
    xy = diff(diff(expr,x1),x2)
    yy = diff(diff(expr,x2),x2)
    dxx = lambdify([x1,x2],xx)
    dxy = lambdify([x1,x2],xy)
    dyy = lambdify([x1,x2],yy)
    # ---------------------------------------------------------------
    # Matriz H , Hessiana
    H = np.matrix([[float(dxx(Xn[0],Xn[1])),float(dxy(Xn[0],Xn[1]))],
    [float(dxy(Xn[0],Xn[1])),float(dyy(Xn[0],Xn[1]))]])
    return H**-1
    # ---------------------------------------------------------------
# ---------------------------------------------------------------

