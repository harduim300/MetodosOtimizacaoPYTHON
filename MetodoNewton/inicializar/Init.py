import matplotlib.pyplot as plt
# Utilizando biblioteca numpy
# para instalar
# pip install numpy
import numpy as np
# Dados iniciais de ponto operado , erro, iterações
X_0 = 0.0
E = 0.01
cont = 10
# estabelece o intervalo para plotar o grafico
# A = 0.0   
# B = 4.0
# ---------------------------------------------------------------
# y(x)
# OBS: QUANDO O METODO DE NEWTON TRABALHA COM UM INTERVALO COM
#      MUITAS CURVAS, ELE TENDE A DAR UM VALOR NÃO PROCURADO.
def fx (x):
    return ((x) - 2)**4 + ((x) - 2*(3))**2
# OBS: USAR NP AO INVES DE MATH
# Devemos sempre fazer a inversão no caso da maximização , senão
# o método não funciona (ELE É TOTALMENTE VOLTADO A MINIMIZAÇÃO)
# ---------------------------------------------------------------