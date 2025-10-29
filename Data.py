class Data():
    def __init__(self, dia=0, mes=0, ano=0):
        self.__dia = 1
        self.__ano = 1900
        self.__mes = 1
        self.setAno(ano)
        self.setMes(mes)
        self.setDia(dia)
    
    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes
    
    def getAno(self):
        return self.__ano
    
    def isBissexto(self, ano):
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    def setDia(self, novo_dia):
        if novo_dia < 1:
            raise ValueError('Dia fora do limite')
        mesesCom30 = [4,6,9,11]
        mesesCom31 = [1,3,5,7,8,10,12]
        maxDias = 31
        if self.__mes in mesesCom30:
            maxDias = 30

        elif self.__mes == 2:
            if self.isBissexto(self.__ano):
                maxDias = 29
            else:
                maxDias = 28
        if maxDias < novo_dia:
            raise ValueError('Dia inválido meu amor...')
        else:
            self.__dia = novo_dia
            
    def setMes(self, novo_mes):
        if novo_mes < 1 or novo_mes > 12:
            raise ValueError('Mês inválido, digite um mês entre 1 e 12')
        self.__mes = novo_mes
    
    def setAno(self, novo_ano):
        if novo_ano < 0:
            raise ValueError ('Ano negativo mds vc ta biruta')
        else:
            self.__ano = novo_ano



