class Carro():
    def __init__(self, capacidade=50, atual=20, consumo=10):
        self.__capacidade = capacidade
        self.atual = atual
        self.__consumo = consumo

    def abastecer(self):
        try:
            qtdAbastecer = float(input('Quanto lt vc quer bota '))
            if ((qtdAbastecer + self.atual) < self.__capacidade):
                self.atual += qtdAbastecer
                print(f'agora voce ta com {self.atual} parabens')
            else:
                print('Gasolina demais parcero')
        except ValueError:
            print("digita direito po pfv")
            
    
    def getAtual(self):
        return self.atual
    
    def consomeGasolina(self):
        distancia = float(input('Distancia'))
        restante = (distancia // self.__consumo)
        return restante
    
    def inReserva(self):
        if self.atual < (self.__capacidade * 0.1):
            return True
        else:
            return False
    
carro1 = Carro()

print(carro1.consomeGasolina())