# Ref https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html#scipy.sparse.csr_matrix
def carregar_matriz(m):
    va = []
    vj = []
    vi = [0]
    with open(m, 'r', encoding='utf-8') as entrada:
        for linha in entrada.readlines():
            j = 0
            for x in linha.replace('\n', '').split(" "):
                if x != '0':
                    if x[0] == '−':
                        va.append(-float(x[1:]))
                    else:
                        va.append(float(x))
                    vj.append(j)
                j += 1
            vi.append(len(va))
    return va, vj, vi


def carregar_valores(a):
    with open(a, 'r', encoding='utf8') as entrada:
        novo = []
        for linha in entrada.readlines():
            for x in linha.split(" "):
                if x[0] == '−':
                    novo.append(-float(x[1:]))
                else:
                    novo.append(float(x))
    return novo
