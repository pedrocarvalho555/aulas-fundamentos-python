lista = []
maior = 0
menor = 0

'''indice_maior = 0
indice_menor = 0'''

for c in range (5):
    in_lista = int(input(f'Digite o {c+1}º número: '))
    lista.append(in_lista)
    if c == 0:
        maior = in_lista
        menor = in_lista
    else:
        if in_lista > maior:
            maior = in_lista
        if in_lista < menor:
            menor = in_lista

print(lista)
print(f'O maior valor é {maior} posicionado no índice {lista.index(maior)}')
print(f'O menor valor é {menor} posicionado no índice {lista.index(menor)}')