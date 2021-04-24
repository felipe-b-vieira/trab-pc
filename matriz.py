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
