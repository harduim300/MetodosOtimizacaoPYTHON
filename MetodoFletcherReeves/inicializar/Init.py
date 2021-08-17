# Utilizando biblioteca numpy
# para instalar
# pip install numpy
import numpy as np
# Dados iniciais de ponto operado , erro, iterações
X_0 = np.array([[0,3]])
E = 0.01
cont = 8
# ---------------------------------------------------------------
# y(x)
# ---------------------------------------------------------------
# Definição de função para o calculo do Lambida
# ---------------------------------------------------------------
def fX (x,Vx,d):
    x1 = (Vx[0]) + x*(d[0])
    x2 = (Vx[1]) + x*(d[1])
    # altera essa função abaixo
    return (x1 - 2)**4 + (x1 -2*x2)**2
# ---------------------------------------------------------------
# Definição de função para o calculo do gradiente
def fx (x,y):
    x1 = x
    x2 = y
    # altera essa função abaixo
    return (x1 - 2)**4 + (x1 -2*x2)**2
#-----------------------------------------------------
