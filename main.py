import matriz as mtz
import numpy as np
from scipy.sparse.linalg import cg
import time
from scipy.sparse import csr_matrix, linalg

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
def grad_conj(m, b, x0=None, eps=1e-5, maxiter=100):
    n = b.shape[0]
    # Se precisar zerar a matriz, então ela não pode ser densa inicialmente, converto em densa e torno esparsa depois
    if not x0:
        x = np.zeros((n,n))
    grad0 = m.multiply(x)
    grad0 = grad0 - b
    grad0 = csr_matrix(grad0)
    x = csr_matrix(x)
        
    # Abaixo é tudo aplicação das fórmulas
    d = - grad0     
    for i in range(maxiter):
        print("---------------------")
        print("-----EXECUÇÃO "+str(i)+"------")
        print("---------------------")
        print("Gradiente: ")
        # print(grad0)
        print("\n")
        
        # Alpha é multiplicação de d transposto e d dividido por d transposto vezes M, vezes d
        # np.dot funciona em matriz esparsa mas a matriz resultado não vai ser esparsa
        alpha = np.dot(grad0.T, grad0) / np.dot(np.dot(d.T, m), d)
        
        # Xi+1 é xi+ di * alphai
        # Multiply não é multiplicação da matriz, é multiplicação dos valores
        y = d.multiply(alpha[0])
        print(x.shape)
        print(y.tocsr().shape)
        print(type(x))
        print(type(y.tocsr()))
        x = x + y.tocsr()
        
        print("X: ")
        print(x)
        print("\n")
        
        # Gera a próxima iteração do gradiente
        gradi = m.multiply(alpha[0])
        gradi = np.dot(gradi, d)
        gradi = grad0 + gradi
        # print(gradi)
        
        # Norma matricial que é feita como condição de parada
        # Se ele continuar executando sem entrar aqui ele vai virar nan
        print("Condição de parada:")
        print(i, linalg.norm(gradi))
        print("\n")
        if linalg.norm(gradi) < eps:
            return x
            
        # Mesma coisa que o alpha
        betai = np.dot(gradi.T, gradi) / np.dot(grad0.T, grad0)
        print("BetaI ")
        # print(betai)
        print("\n")
        
        #Acha o próximo d(diferença)
        d = d.multiply(betai[0])
        d = - gradi + d
        grad0 = gradi
        
    return x
    

if __name__ == '__main__':
    #coeficientes = input("Insira o nome do primeiro arquivo (coeficientes da Matriz):")
    #valores = input("Insira o nome do segundo arquivo (valores b):")
    mat = csr_matrix(np.array(mtz.criarmatriz("matriz.txt")))
    val = np.array(mtz.criarmatriz("valores.txt"))
    start_time = time.time()
    print("----------------------")
    # Uso o todense só para printar
    gc = grad_conj(mat, val).toarray()
    res = open("resposta.txt", "w")
    print("Resultado:")
    for i in range(len(gc)):
        res.write(str(gc[i][0]))
        print(gc[i][0])
        res.write("\n")
    res.close()
    print("--- %s segundos de execução ---" % (time.time() - start_time))
