# Utilizando biblioteca numpy
# para instalar
# pip install numpy
import numpy as np
# Dados iniciais de ponto operado , erro, iterações
X_0 = np.array([[0.0,0.0],[1.0,2.0],[0.0,2.0]])
cont = 12
# ---------------------------------------------------------------
# y(x)
def fx (x1,x2):
    # SÓ altera essa função abaixo
    return (x1 - 2)**4 + (x1 -2*x2)**2
# o método não funciona Maximização(ELE É TOTALMENTE VOLTADO A MINIMIZAÇÃO)
# ---------------------------------------------------------------
