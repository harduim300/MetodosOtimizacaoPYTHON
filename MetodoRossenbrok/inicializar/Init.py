import matplotlib.pyplot as plt
# Utilizando biblioteca numpy
# para instalar
# pip install numpy
import numpy as np
# Dados iniciais de ponto operado , erro, iterações
X_0 = np.array([[0,3]])
E = 0.01
cont = 12
# ---------------------------------------------------------------
# y(x)
# OBS: QUANDO O METODO DE NEWTON TRABALHA COM UM INTERVALO COM
#      MUITAS CURVAS, ELE TENDE A DAR UM VALOR NÃO PROCURADO.
def fx (x,Vx,d):
    x1 = (Vx[0][0]) + x*(d[0])
    x2 = (Vx[0][1]) + x*(d[1])
    # SÓ altera essa função abaixo
    return (x1 - 2)**4 + (x1 -2*x2)**2
# OBS: USAR NP AO INVES DE MATH
# Devemos sempre fazer a inversão no caso da maximização , senão
# o método não funciona (ELE É TOTALMENTE VOLTADO A MINIMIZAÇÃO)
# ---------------------------------------------------------------
