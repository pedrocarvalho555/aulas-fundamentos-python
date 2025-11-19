import random

print(' --- Adivinhe o número --- ')
print(' --- Receba um prémio --- ')

numero_input = int(input('Digite um número de 0 a 7\n--> '))
aleatorio = random.randrange(8)

if aleatorio == numero_input:
    print(' *** GANHOU *** ')
else:
    print('puts, perdeu')