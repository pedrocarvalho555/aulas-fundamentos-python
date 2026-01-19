'''
Crie uma classe chamada “Aluno” que
possua atributos para armazenar o nome e
as notas de um aluno. Adicione métodos
para calcular a média das notas e
verificar a situação do aluno (aprovado
ou reprovado).
'''
from statistics import mean

class Aluno():
    def __init__(self, nome: str, notas: list):
        self.__nome = nome
        self.__notas = notas
        self.__media = self.media()
        self.__situacao = self.situacao()

    def media(self):
        return mean(self.__notas)

    def situacao(self):
        if self.__media > 9.5:
            return 'Aprovado'
        else:
            return 'Reprovado'

    def mostra(self):
        print(f'{self.__nome} | {self.__notas} | {self.__media} | {self.__situacao}')

lista_notas = [10,8,9,12,14]
new = Aluno('FansFans', lista_notas)

new.mostra()