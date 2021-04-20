import matriz as mtz
import numpy as np
from scipy.sparse.linalg import cg
import time

# Dado um Xo
# rk = b - Axk
# dk = rk -  alfak1d1 - alfak2d2 -....
#   Simplifica para -> Betak+1 = rk+1T A dk /dkT A dk
#   E dk+1 = rk+1 += bk+1 dk
# alphak = dkrk / dkTAdk
# xk+1 = xk + alphakdk

# Fórmulas: https://youtu.be/sjvNzP44Lks?t=2357
# Explicação: https://www.youtube.com/watch?v=hePxJL_KBn4&t=1300s

# Método do gradiente:
# Busca utilizar o resíduo da diferença entre o resultado inicial e final e usar isso para aproximar da solução
# O gradiente é a direção do maior crescimento. O gradiente é - f(x), dado f(x) = Ax* - b
# O gradinte normal realiza diversos passos em ortogonal.
# Aproxima várias vezes, invés de tentar seguir direto ao resultado

# O gradiente conjugado busca fazer em poucos passos
# A ideia do gradiente conjugado é pegar só o ultimo gradiente e ajustar ele
def grad_conj(m, b, x0=None, eps=1e-5, maxiter=10):

    n = len(b)
    if not x0:
        x = np.zeros(n)
        
    # np.dot é multiplicação de Matriz
    grad0 = np.dot(m, x) - b      
    d = - grad0     
    # POSSÍVEL ERROS NOS CÁLCULOS
    # NÃO É ERRO, TIRAR O ROUND
    for i in range(maxiter):
        print("----------------------")
        print(grad0)
        
        # Alpha é multiplicação de d transposto e d dividido por d transposto vezes M, vezes d
        alpha = np.dot(grad0.T, grad0) / np.dot(np.dot(d.T, m), d)
        
        # Xi+1 é xi+ di * alphai
        x = x + d*(alpha[0])
        print(x)
        
        gradi = grad0 + np.dot(m*(alpha[0]), d)
        print(gradi)
        
        # Norma matricial que é feita como condição de parada
        #print(i, np.linalg.norm(gradi))
        if np.linalg.norm(gradi) < eps:
            return np.round(x, 2)
            
        betai = np.dot(gradi.T, gradi) / np.dot(grad0.T, grad0)
        print(betai)
        
        d = - gradi + (betai[0])*d
        grad0 = gradi
        print(grad0)
        
    return np.round(x, 2)
    

if __name__ == '__main__':
    #coeficientes = input("Insira o nome do primeiro arquivo (coeficientes da Matriz):")
    #valores = input("Insira o nome do segundo arquivo (valores b):")
    mat = np.array(mtz.criarmatriz("matriz.txt"))
    val = np.array(mtz.criarmatriz("valores.txt"))
    start_time = time.time()
    gc = grad_conj(mat, val)
    res = open("resposta.txt", "w")
    for i in range(len(gc[0])):
        res.write(str(gc[i][0]))
        print(gc[i][0])
        res.write("\n")
    res.close()
    print("--- %s segundos de execução ---" % (time.time() - start_time))
