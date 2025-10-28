def mostraMatriz(matriz):
    for linha in matriz:
        for j in linha:
            print(f'{j}', end=' ')
        print()       


m = [[1,2],
     [1,2]]
mostraMatriz(m)