import numpy as np
from inicializar import Init
def SimplexExE ():
    # ----------------------------------------------------------
    # Metodo para incializar a ordenção
    # ----------------------------------------------------------
    # Iremos fazer a ordenação dos vertices de valor inicial
    Xn = ordenacao(Init.X_0)
    Xf = np.array(Xn[0])
    # ----------------------------------------------------------
    it = 0
    cont = [0]
    while(it < Init.cont):
        cont.append(it+1) 
        #------------------------------------------------------
        # Definição do centroide 
        #   C = 0.5(Xbest - Xintr)
        #------------------------------------------------------
        C = 0.5*(Xn[0] + Xn[1])
        #------------------------------------------------------
        # Calculo Xr = C + a(C - Xw) com a = 1
        #------------------------------------------------------
        Xr = C + (C - Xn[2])
        #------------------------------------------------------
        # Comparação entre f(Xr)| f(Xbest)| f(Xintr)| f(Xworst)|
        #------------------------------------------------------
        auxf = Init.fx(Xr[0],Xr[1])
        auxbest = Init.fx(Xn[0][0],Xn[0][1])
        auxintr = Init.fx(Xn[1][0],Xn[1][1])
        auxworst = Init.fx(Xn[2][0],Xn[2][1])
        #------------------------------------------------------
        #   Expansão
        #------------------------------------------------------
        if(auxf < auxbest):
            Xb = C + 2*(Xr - C)
            Xn[2] = menor(Xr,Xb)
            Xn = ordenacao(Xn)
        #------------------------------------------------------
        #   Contração
        #------------------------------------------------------
        if(auxf > auxworst):
            Xc = C + 0.5*(Xn[2] - C)
            auxc = Init.fx(Xc[0],Xc[1])
            if(auxc < auxworst):
                Xn[2] = Xc
                Xn = ordenacao(Xn)
        #------------------------------------------------------
        #   Reflexão
        #------------------------------------------------------
        if(auxf > auxbest and auxf < auxworst):
            Xn[2] = Xr
            Xn = ordenacao(Xn)
        #------------------------------------------------------
        it += 1
        #------------------------------------------------------
        # Armazenado os melhores X
        Xf = np.vstack([Xf,Xn[0]])
        #------------------------------------------------------
    print("| i |",cont,"|")
    print("----------------------------------------------")
    print("| Xn |")
    print("----------------------------------------------")
    print(Xf)
    print("----------------------------------------------")
    #--------------------------------------------------------
    # Retorno o Melhores Pontos Xbest em n iterações.
    #--------------------------------------------------------

#------------------------------------------------------
#   Função de verificação do melhor valor de expansão
#------------------------------------------------------
def menor(Xr,Xb):
    auxb = Init.fx(Xb[0],Xb[1])
    auxn = Init.fx(Xr[0],Xr[1])
    if(auxb < auxn):
        return Xb
    else:
        return Xr
#------------------------------------------------------
#   Função de Ordenação do vetor
#------------------------------------------------------
#   Xr = [Xmelhor,Xintermediario,Xpior]
#------------------------------------------------------
def ordenacao(Xn):
    aux = []
    for j in range(3):
        aux.append(Init.fx(Xn[j][0],Xn[j][1]))
    indbest = aux.index(min(aux))
    indworst = aux.index(max(aux))
    for j in range(3):
        if(j != indbest and j != indworst):
            indint = j
    Xb = Xn[indbest]
    Xi = Xn[indint]
    Xw = Xn[indworst]
    return np.array([Xb,Xi,Xw])
#------------------------------------------------------