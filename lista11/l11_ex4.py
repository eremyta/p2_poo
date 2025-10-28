def menorValor(m):
    menor = m[0][0]
    resultado = []
    linha = 0
    coluna = 0
    for l in range(len(m)):
        for c in range(len(m[l])):
            if m[l][c] <= menor:
                menor = m[l][c]
                linha = l + 1
                coluna = c + 1
    resultado = []
    resultado.append(menor)
    resultado.append(linha)
    resultado.append(coluna)
    return resultado

m = [[1,2],
     [3,4]]
print(menorValor(m))
