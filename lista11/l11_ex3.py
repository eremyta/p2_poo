def maiorTexto(m):
    maior = ''
    for i in m:
        for j in i:
            if len(j) > len(maior):
                maior = j
    return maior

m = [['aaaaaa', 'aaaaaaaaa'],
     ['aaa', 'aaaa']]
print(maiorTexto(m))
