import random
from time import sleep
par = 0
impar = 0

for c in range (0, 10):
    num = int(input('Digite um número: '))
    par_ou_impar = num % 2
    if par_ou_impar == 0:
        print(f'{num} é par')
        par+=1
    else:
        print(f'{num} é ímpar')
        impar+=1

print(f'Existem {par} números par e {impar} números ímpar')

#ou com números aleatorios

for c in range (0, 10):
    aleatorio = random.randrange(0, 1000)
    par_ou_impar = aleatorio % 2
    if par_ou_impar == 0:
        print(f'{aleatorio} é par')
        sleep(0.5)
    else:
        print(f'{aleatorio} é impar')
        sleep(0.5)

print(f'Existem {par} números par e {impar} números ímpar')