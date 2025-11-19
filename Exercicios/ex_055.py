tuple_mgs = ('Metal Gear Solid', 1998, 'Metal Gear Solid 2: Sons of Liberty', 2001, 'Metal Gear Solid 3: Snake Eater', 2004,
             'Metal Gear Solid 4: Guns of the Patriots', 2008, 'Metal Gear Solid: Peace Walker', 2010,
             'Metal Gear Solid V: Ground Zeroes', 2014, 'Metal Gear Solid V: The Phantom Pain', 2015)
# fiz com ano de lançamento em vez de preço porque a informação está mais accessivel, será que conta?
# a solução fácil para alinhar seria remover todos os subtitulos mas aí não tem graça
# cumprimento maximo = 50
espaco = 0
print('-------------- CRONOLOGIA METAL GEAR ----------------')
print('[NOME] --------------------------------------- [DATA]')
for c in range (0, len(tuple_mgs), 2):
    tamanho_linha = len(f'{tuple_mgs[c]}{tuple_mgs[c + 1]}') # o correto seria talvez fazer len separados para nome e ano e somar
    espaco = 50 - tamanho_linha
    tracos = '-'*espaco
    print(f'{tuple_mgs[c]} {tracos} {tuple_mgs[c+1]}')