from typing import List, Any


def altura(m):
    return len(m)


def largura(m):
    return len(m[0])


def issparse(m):
    a = altura(m)
    l = largura(m)
    maxnumelem = a * l
    contador = 0
    for i in (range(a)):
        for j in range(l):
            if i == j and m[i][j] == 0.0:
                return False
            if m[i][j] != 0.0:
                contador += 1
    if contador > int(maxnumelem / 2):
        return False
    else:
        return True


def csr(m):
    csr = [[], [], []]  # type: List[List[float]]
    am = altura(m)
    lm = largura(m)
    if am == lm:
        for i in range(a):
            if m[i][i] != 0.0:
                csr[0].append(m[i][i])
                csr[1].append(i)
                csr[2].append(len(csr[0])-1)
            for j in range(l):
                if j != i and m[i][j] != 0.0:
                    csr[0].append(m[i][j])
                    csr[1].append(j)

    else:
        for i in range(a):
            for j in range(l):
                if m[i][j] != 0.0:
                    csr[0].append(m[i][j])
                    csr[1].append(i)
                    csr[2].append(len(csr[0]))
    return csr


def criarmatriz(m):
    entrada = open(m, 'r', encoding='utf8')
    novo = []
    for linha in entrada.readlines():
        vals = []
        for x in linha.split(" "):
            if x[0] == '−':
                vals.append(-float(x[1:]))
            else:
                vals.append(float(x))
        novo.append(vals)
    entrada.close()
    print(novo)
    return novo


def criarArray(a):
    entrada = open(a, 'r', encoding='utf8')
    novo = []
    for linha in entrada.readlines():
        for x in linha.split(" "):
            if x[0] == '−':
                novo.append(-float(x[1:]))
            else:
                novo.append(float(x))
    entrada.close()
    print(novo)
    return novo


def transpostalista(m):
    res = [[0]]*altura(m)
    print(res)
    for i in range(altura(m)):
        print(i)
        res[0][i] = m[0][i]
    return res


def transpostamatriz(m):
    res = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    return res


def listazero(n):
    listofzeros = [0] * n
    return listofzeros


def multiplicaarray(m):
    res = 0
    for i in range(altura(m)):
        res += m[i]*m[i]
    return res

def multiplicamatriz(m, n):
    am = altura(m)
    an = altura(l)
    ln = largura(l)
    result = listazero(am)*ln
    for i in range(am):
        for j in range(ln):
            for k in range(an):
                result[i][j] += m[i][k] * n[k][j]
    return result
