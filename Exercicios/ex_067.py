'''

fm24 só que melhor

'''

lista = list()
qtd_jogadores = int(input('Quantos jogadores quer adicionar?\n--> '))

for c in range (qtd_jogadores):
    database = dict()
    database["Nome"] = input('Qual o nome do jogador?\n--> ')
    database["Jogos"] = int(input('Quantos jogos jogou?\n--> '))
    database["Golos"] = int(input('Quantos golos marcou?\n--> '))
    database["GoloPorJogo"] = database["Golos"] / database["Jogos"]
    lista.append(database)



for a in lista:
    print(f'Jogador: {a["Jogador"]}')
    print(f'Jogos: {a["Jogos"]}')
    print(f'Golos: {a["Golos"]} | {a["GoloPorJogo"]} golos por jogo')