'''
Crie uma classe ContaBancaria com
atributos privados nib, titular, saldo e
limite. Adicione métodos getters e
setters para os atributos.
'''

class ContaBancaria():
    def __init__(self, titular, nib, saldo, limite):
        self.__titular = titular
        self.__nib = nib
        self.__saldo = saldo
        self.__limite = limite

    def get_titular(self):
        return self.__titular

    def set_titular(self, novo_titular):
        self.__titular = novo_titular

    def get_nib(self):
        return self.__nib

    def set_nib(self, novo_nib):
        self.__nib = novo_nib

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def get_limite(self):
        return self.__limite

    def set_limite(self, novo_limite):
        self.__limite = novo_limite



