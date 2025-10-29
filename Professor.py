from Funcionario import Funcionario

class Professor(Funcionario):
    def __init__(self, nome='', endereco='', telefone='', email='', escritorio='', salario=0, admissao=None, qtd_ha=0, qtd_pe=0):
        super().__init__(nome, endereco, telefone, email, escritorio, salario, admissao)
        self.__qtd_ha = qtd_ha
        self.__qt_pe = qtd_pe
    
    def getAula(self):
        return self.__qtd_ha
    
    def getPesquisa(self):
        return self.__qt_pe