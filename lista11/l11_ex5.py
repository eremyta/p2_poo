def matrizPrima(m):
    for linha in m:
        for item in linha:
            is_Primo = False
            if numero <= 1:
                is_Primo = False
            elif numero <= 3:
                is_Primo = True
            elif numero % 2 == 0 or num % 3 == 0:
                is_Primo = False
            else:
                limite = int((item ** 0.5))

                i = 5
                is_Primo = True
                while i <= limite:
                    # Testa divisores no formato 6k - 1 (i) e 6k + 1 (i + 2)
                    if numero % i == 0 or numero % (i + 2) == 0:
                        is_primo = False
                        break 
                    i += 6