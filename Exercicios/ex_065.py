from random import randint

lista = list()
print('--- SIMULADOR DE INICIATIVA ---')
num_jogadores = int(input('Quantos jogadores estão na partida?\n-->'))

for c in range(num_jogadores):
    iniciativa = dict()
    iniciativa["Nome"] = input(f'Digite o seu nome jogador nº {c+1}: ')
    iniciativa["Dado"] = randint(1, 20)  # d20
    print(f'O {c+1}º jogador rolou um {iniciativa["Dado"]}')
    lista.append(iniciativa)

temp = lista.copy()
ranking = list()

'''
while temp:
    primeiro_jogador = ''
    maior_dado = 0

    for a in lista:
        if a["Dado"] > maior_dado:
            primeiro_jogador = a["Nome"]
            print(primeiro_jogador)
            maior_dado = a["Dado"]
    ranking.append((primeiro_jogador, maior_dado))
    del temp[primeiro_jogador]
    '''

print(f'Jogador: {a["Nome"]} e o seu dado: {a["Dado"]} ')



