# Nao funciona em todas as situações

lista=[]

for a in range (5):
    list_in = int(input(f'Digite o {a+1}º número: '))
    if a == 0: # vai ser o valor base para o resto do procedimento
        lista.append(list_in)

    if list_in > lista[-1]:
        lista.append(list_in)

    else:
        for b in range(len(lista)): # vai correr a lista para verificar onde colocar o dito cujo
            if list_in < lista[b]:
                lista.insert(b,list_in)
                break
print(lista)