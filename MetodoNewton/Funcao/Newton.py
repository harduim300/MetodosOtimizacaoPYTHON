from inicializar import Init # Como dar include em python
# Aproximações Lineares das derivadas 
h = 0.01
# y'(x)
def f1x(x):
    return (1/(2*h))*(Init.fx(x + h) - Init.fx(x - h))
# y"(x)
def f2x(x):
    return (1/h**2)*(Init.fx(x + h) + Init.fx(x - h) - 2*Init.fx(x))
# ---------------------------------------------------------------
def NewtonExe():   
    X = [Init.X_0]
    cont = [0]
    for i in range(Init.cont):
        cont.append(i+1)    # Pega quantas iterações foram feitas
        Newton = X[i] - (f1x(X[i])/f2x(X[i]))
        X.append(round(Newton,8))
        if Init.np.fabs(X[i+1] - X[i]) < Init.E: # faz modulo e avalai o erro
            break
    print("| i  |",cont,"|")
    print("----------------------------------------------")
    print("| Xn |",X,"|")
    print("----------------------------------------------")
    Xr = X.pop()
    print("| Xr |",round(Xr,5),"|")
    print("----------------------------------------------")
    # ------------------------------------------------------
    # Definição do grafico da função
    # x = Init.np.linspace(Init.A,Init.B)  # Define os limites do grafico pelo nosso intervalo
    # Init.plt.plot(x, Init.fx(x))    # faz a plotagem do grafico
    # Init.plt.grid()                  # Apenas para problemas de minimização
    # Init.plt.show()                  # O grafico da apenas uma ideia para o caso MAX  
    # -----------------------------------------------------------