def AureoExe():
    from inicializar import Init # Como dar include em python   
    A = [Init.X_a]
    B = [Init.X_b]
    cont = [0]
    for i in range(Init.cont):
        cont.append(i+1)    # Pega quantas iterações foram feitas
        lamb = A[i] + 0.382*(B[i]-A[i]); omeg = A[i] + 0.618*(B[i]-A[i])
        y_lamb = Init.fx(lamb); y_omeg = Init.fx(omeg)
        if y_lamb > y_omeg :
            A.append(lamb) # Cria um arredondamento para 5 casas decimais
            B.append(B[i])
        else:
            B.append(omeg)
            A.append(A[i])
        if B[i+1] - A[i+1] < 0: # faz modulo e avalai o erro
            aux = -(B[i+1] - A[i+1])
            if aux < Init.E:
                break
        else:
            aux = B[i+1] - A[i+1]
            if aux < Init.E:
                break
    print("| i  |",cont,"|")
    print("----------------------------------------------")
    print("| Ak |",A,"|")
    print("----------------------------------------------")
    print("| Bk |",B,"|")
    print("----------------------------------------------")
    Xr = (A.pop() + B.pop())/2
    print("| Xr |",round(Xr,5),"|")
    print("----------------------------------------------")
    # x = Init.np.linspace(A[0],B[0])  # Define os limites do grafico pelo nosso intervalo
    # Init.plt.plot(x, Init.fx (x))    # faz a plotagem do grafico
    # Init.plt.grid()                  # Apenas para problemas de minimização
    # Init.plt.show()                  # O grafico da apenas uma ideia para o caso MAX  

