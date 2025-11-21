from random import randint
from time import sleep
lista = list()
print('--- SIMULADOR DE INICIATIVA ---')
num_jogadores = int(input('Quantos jogadores estão na partida?\n-->'))

for c in range(num_jogadores):
    iniciativa = dict()
    iniciativa["Nome"] = input(f'Digite o seu nome jogador nº {c+1}: ')
    iniciativa["Dado"] = randint(1, 20)  # d20
    print(f'O {c+1}º jogador rolou um {iniciativa["Dado"]}')
    lista.append(iniciativa)

for a in lista:
    print(f'Jogador: {a["Nome"]} e o seu dado: {a["Dado"]} ')


