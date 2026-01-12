'''
Crie uma classe ContaBancaria com
atributos titular, saldo e limite.
Adicione métodos para depositar() e
sacar(), alterando o saldo da conta de
acordo com a operação.
'''

class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self.limite = 400

    def sacar(self, valor):
        if valor > self.limite:
            print('Só pode levantar até 400€ por dia')
        else:
            self.saldo -= valor
            print(f'Levantou {valor}€')

    def depositar(self, valor):
        self.saldo += valor
        print(f'Depositou {valor}€')

    def consultar_saldo(self):
        print(f'Olá {self.titular}, o seu saldo é de {self.saldo:.2f}€')


def menu():
    while True:
        print(f'Olá {conta.titular}')
        print('[1] Levantar')
        print('[2] Depositar')
        print('[3] Consultar Saldo')
        print('[4] Sair')
        opcao = int(input('--> '))

        if opcao == 1:
            valor = float(input('Quanto dinheiro deseja levantar: '))
            conta.sacar(valor)
        if opcao == 2:
            valor = float(input('Quanto dinheiro quer depositar: '))
            conta.depositar(valor)
        if opcao == 3:
            conta.consultar_saldo()
        if opcao == 4:
            break

conta = Conta('Elvis Presley', 5000)

menu()
