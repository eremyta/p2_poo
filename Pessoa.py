class Pessoa ():
    def __init__(self, nome='', endereco='', telefone='', email=''):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email
    
    def getNome(self):
        return self.__nome

    def informaDescricao(self):
        nome_pessoa = self.getNome()
        nome_classe = self.__class__.__name__
        p = f'{nome_pessoa} {nome_classe}'
        return p
        