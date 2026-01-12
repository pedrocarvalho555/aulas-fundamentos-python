'''
Crie uma classe Produto com os atributos
nome e quantidade em stock. Adicione um
método que mostre o stock no estilo “O
produto X tem Y unidades em stock”.
Adicione um novo método que aumenta a
quantidade de stock numa determinada
quantidade.
'''

class Produto:
    def __init__(self, nome_produto, stock):
        self.nome_produto = nome_produto
        self.stock = stock

    def show_product(self):
        print(f'{self.nome_produto} - {self.stock} unid.')

    def mais_stock(self, valor):
        self.stock += valor

def menu():
    while True:
        print(f'[1] - {prod1.nome_produto} - {prod1.stock} unid.')
        print(f'[2] - {prod2.nome_produto} - {prod2.stock} unid.')
        print(f'[3] - {prod3.nome_produto} - {prod3.stock} unid.')
        print(f'[4] - Sair')
        opcao = int(input('Escolha um produto para aumentar a quantia: '))

        if opcao == 1:
            valor = int(input('Quer aumentar o stock em quanto?\n--> '))
            prod1.mais_stock(valor)
        if opcao == 2:
            valor = int(input('Quer aumentar o stock em quanto?\n--> '))
            prod2.mais_stock(valor)
        if opcao == 3:
            valor = int(input('Quer aumentar o stock em quanto?\n--> '))
            prod3.mais_stock(valor)
        if opcao == 4:
            break


prod1 = Produto('Coisa', 10)
prod2 = Produto('OutraCoisa',5)
prod3 = Produto('CoisaFinal', 2)

menu()
