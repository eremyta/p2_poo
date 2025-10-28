class Conta():

    def __init__(self, saldo=0, senha=123, titular=''):
        self.__titular = titular
        self.__saldo = saldo
        self.__senha = senha

    def sacar(self):
        valorSaque = float(input('Quando você deseja sacar?'))
        if valorSaque <= self.__saldo and valorSaque > 0:
            self.__saldo -= valorSaque
            return self.__saldo
    
    def depositar(self):
        valorDeposito = float(input('Digite o valor a ser depositado:'))
        if valorDeposito > 0:
            self.__saldo += valorDeposito
            print(f'Depósito realizado, seu novo saldo é {self.__saldo}')
            return self.__saldo
    
    def verificarNegativo(self):
        if self.__saldo < 0:
            print('Saldo negativo')
        else:
            print('Saldo Positivo')

    def trocarSenha(self):
        senha_atual = input('Digite sua senha atual:')
        if senha_atual == self.__senha:
            nova_senha = input('Digite a nova senha:')
            self.__senha = nova_senha
    
    def getSaldo(self):
        print(f'R${self.__saldo:.2f}')

conta1 = Conta()
conta2 = Conta()
conta2.getSaldo()
conta2.depositar()


