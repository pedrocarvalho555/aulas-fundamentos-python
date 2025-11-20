from random import randint
from time import sleep
iniciativa = dict()
print('--- SIMULADOR DE INICIATIVA ---')
num_jogadores = int(input('Quantos jogadores estão na partida?\n-->'))

for c in range(num_jogadores):
    iniciativa["Nome"] = input(f'Digite o seu nome jogador nº {c+1}: ')
    iniciativa["Dado"] = randint(1, 20)  # d20
    print(f'O {c+1}º jogador rolou um {iniciativa["Dado"]}')

print(iniciativa)

