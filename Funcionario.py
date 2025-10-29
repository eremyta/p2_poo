from Pessoa import Pessoa
from Data import Data

class Funcionario(Pessoa):
    def __init__(self, nome='', endereco='', telefone='', email='', escritorio='', salario=0, admissao=None):
        super().__init__(nome, endereco, telefone, email)
        self.__escritorio = escritorio
        self.__salario = salario
        
