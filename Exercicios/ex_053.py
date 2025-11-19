from random import randint
#tuple cheio de randints
random_tuple = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))

print(sorted(random_tuple)) # primeira parte do exercicio

for c in range (0, len(random_tuple)): # verifica qual o menor e o maior
    if c == 0: # inicia as variaveis maior e menor com o valor do primeiro indice
        maior = random_tuple[c]
        menor = random_tuple[c]
    else:
        if random_tuple[c] > maior:
            maior = random_tuple[c]
        elif random_tuple[c] < menor:
            menor = random_tuple[c]

print(f'O maior valor é: {maior}\nO menor é: {menor}')