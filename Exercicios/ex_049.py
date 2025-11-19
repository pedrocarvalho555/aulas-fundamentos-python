from random import randrange
from time import sleep

contador = 0
print('!!! [PAR OU IMPAR] !!!')
while True:
    aleatorio = randrange(5)
    print('[0] PAR')
    print('[1] IMPAR')
    jogada1 = int(input('--> '))
    if jogada1 == 0 or jogada1 == 1:
        jogada2 = int(input('Quantos dedos vais soltar?\n--> '))
        par_impar = (aleatorio + jogada2) % 2
        if (par_impar == 0 and jogada1 == 0) or (par_impar!=0 and jogada1 == 1):
            print(f'CPU: {aleatorio}\nJogador: {jogada2} ')
            print('Ganhaste!!!!!!! Vamos jogar novamente!')
            sleep(1)
            contador+=1
        else:
            print(f'CPU: {aleatorio}\nJogador: {jogada2} ')
            print(f'Perdeste mas não chores, ainda venceste {contador} vezes')
            break
    else:
        print('Jogada inválida, vamos tentar novamente')
