import math
# import matplotlib.pyplot as plt
# Utilizando biblioteca numpy
# para instalar
# pip install numpy
import numpy as np
X_a = 0.0
X_b = 3.0
E = 0.001
cont = 20
def fx (x):
    return x**3 -3*x -3
# OBS: USAR NP AO INVES DE MATH
# Devemos sempre fazer a inversão no caso da maximização , senão
# o método não funciona (ELE É TOTALMENTE VOLTADO A MINIMIZAÇÃO)