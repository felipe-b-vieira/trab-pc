import time

import numpy as np
from scipy.sparse import csr_matrix

import matriz as mtz


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
def grad_conj(m, b, eps=1e-5):
    n = b.shape[0]
    x = np.zeros(n)
    grad0 = (m * x) - b

    # Abaixo é tudo aplicação das fórmulas
    d = - grad0
    i = 0
    while np.linalg.norm(grad0) >= eps:
        print("---------------------")
        print("-----EXECUÇÃO " + str(i) + "------")
        print("---------------------")
        print("Gradiente: ")
        print("\n")

        # Alpha é multiplicação de d transposto e d dividido por d transposto vezes M, vezes d
        # np.dot funciona em matriz esparsa mas a matriz resultado não vai ser esparsa
        ad = m * d.T
        alpha = np.dot(grad0.T, grad0) / np.dot(ad, d)

        # Xi+1 = xi + di * alphai
        x = x + d * alpha

        print("X: ")
        print(x)
        print("\n")

        # Gera a próxima iteração do gradiente
        gradi = grad0 + d * (m * alpha)

        # Norma matricial que é feita como condição de parada
        # Se ele continuar executando sem entrar aqui ele vai virar nan
        print("Condição de parada:")
        print(i, "->", np.linalg.norm(gradi), "\n")

        # Mesma coisa que o alpha
        betai = np.dot(gradi.T, gradi) / np.dot(grad0.T, grad0)
        print("\n")

        # Acha o próximo d(diferença)
        d = - gradi + d * betai
        grad0 = gradi

        i += 1
    return x


if __name__ == '__main__':
    # coeficientes = input("Insira o nome do primeiro arquivo (coeficientes da Matriz):")
    # valores = input("Insira o nome do segundo arquivo (valores b):")
    mat = csr_matrix(mtz.criarmatriz("matriz.txt"))
    val = np.array(mtz.criarArray("valores.txt"))
    start_time = time.time()
    print("----------------------")
    gc = grad_conj(mat, val)
    res = open("resposta.txt", "w")
    print("Resultado:")
    for i in range(len(gc)):
        res.write(str(gc[i]))
        print(gc[i])
        res.write("\n")
    res.close()
    print("--- %s segundos de execução ---" % (time.time() - start_time))
