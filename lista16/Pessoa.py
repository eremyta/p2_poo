class Pessoa ():
    def __init__(self, nome='', endereco='', telefone='', email=''):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email
    
    def informaDescricao(self):
        p = f'Pessoa {self.__nome}'
        return p
        
