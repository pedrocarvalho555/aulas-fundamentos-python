'''
Modifique o exercício 95 para ter atributos
privados para titular, saldo e limite.
Implemente getters e setters usando property
para esses atributos. Adicione métodos para
depositar() e sacar(), que devem alterar o
saldo da conta. Garanta que as operações
respeitem o limite da conta e que o saldo não
se torne negativo.
'''
from math import fabs

class ContaBancaria():
    def __init__(self, titular, nib, saldo):
        self.__titular = titular
        self.__nib = nib
        self.__saldo = saldo
        self.__limite = 400

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    @property
    def nib(self):
        return self.__nib

    @nib.setter
    def nib(self, novo_nib):
        self.__nib = novo_nib

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    def depositar(self):
        valor = fabs(float(input('Valor a depositar: ')))
        self.__saldo += valor

    def sacar(self):
        valor = fabs(float(input('Valor a levantar: ')))

        if valor > self.__limite or self.__saldo - valor < 0:
            print('ERRO NO LEVANTAMENTO')
        else:
            self.__saldo -= valor

conta = ContaBancaria('FansFans', 'PT50123456789', 5000)

conta.depositar()
print(conta.saldo)
conta.sacar()
print(conta.saldo)


