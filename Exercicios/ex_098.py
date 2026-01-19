'''
Crie uma classe chamada Produto que inclua
atributos para o nome e a quantidade em
stock. Utilize a property para aceder a
quantidade em stock, garantindo que ela nunca
seja negativa. Inclua um método mostrar_stock
que exibe uma mensagem indicando quantas
unidades do produto estão disponíveis.
Adicione também um método adicionar_stock que
permite aumentar a quantidade de stock de um
produto.
'''

class Produto:
    def __init__(self, nome, qtd=0):
        self.__nome = nome
        self.__qtd_stock = self.__e_negativo(qtd)

    def __e_negativo(self, valor: int):
        if valor < 0:
            print('O VALOR DE STOCK É NEGATIVO')
            return None
        else:
            print('STOCK OK')
            return valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def qtd_stock(self):
        return self.__qtd_stock

    @qtd_stock.setter
    def qtd_stock(self, novo_stock):
        self.__qtd_stock = self.__e_negativo(novo_stock)

    def aumentar_stock(self, valor):
        valor = self.__e_negativo(valor)
        self.__qtd_stock = valor


batatas = Produto('Batatas', 50)