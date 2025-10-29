from Funcionario import Funcionario

class Servidor(Funcionario):
    CARGAS_VALIDAS = [20,40]
    def __init__(self, nome='', endereco='', telefone='', email='', escritorio='', salario=0, admissao=None, carga=20,titulacao=''):
        super().__init__(nome, endereco, telefone, email, escritorio, salario, admissao)
        self.setCarga(carga)
        self.setTitulacao(titulacao)
    
    def setCarga(self, nova_carga):
        if nova_carga not in self.CARGAS_VALIDAS:
            raise ValueError ('Carga inadequada')
        else:
            self.__carga = nova_carga
    
    def getCarga(self):
        return self.__carga
    
    def setTitulacao(self, nova_titulacao):
        self.__titulacao = nova_titulacao
    
    def getTitulacao(self):
        return self.__titulacao
