def somaElementos(m):
    i = 0
    soma = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            soma += m[i][j]
            j += 1
        i += 1
    return soma

m = [[1,2],
     [1,2]]
teste = somaElementos(m)
print(teste)
        
    
    