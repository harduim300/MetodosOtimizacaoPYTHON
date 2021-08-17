# Utilizando biblioteca numpy
# para instalar
# pip install numpy
import numpy as np
# Dados iniciais de ponto operado , erro, iterações
X_0 = np.array([[2,1]])
E = 0.01
cont = 200
# ---------------------------------------------------------------
# y(x)
def fX (x1,Vx,d):
    x = (Vx[0]) + x1*(d[0])
    y = (Vx[1]) + x1*(d[1])
    #altera essa função abaixo
    return (x - y**3)**2 + 3*(x - y)**4
# ---------------------------------------------------------------
# Definição de função para o calculo do gradiente
def fx (x,y):
    # É necessário tambem ser alterada essa função abaixo
    return (x - y**3)**2 + 3*(x - y)**4
#-----------------------------------------------------
