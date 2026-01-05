'''
Crie um programa com uma função chamada
fatorial(), que receba dois parâmetros:
o primeiro será o número a calcular o
fatorial e o segundo será opcional e
lógico que indique se será exibido ou
não o processo de cálculo do fatorial. O
fatorial deve ser guardado num ficheiro
txt.
'''

from pathlib import Path
from math import factorial

def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def fatorial(num: int, visibilidade: bool):
    """
    Calcula o fatorial de um número e guarda o resultado num ficheiro .txt
    :param num: Número a ser utilizado para o cálculo
    :param visibilidade: se True vai exibir o cálculo completo no ficheiro .txt, se false apresenta apenas o resultado
    :return: null
    """
    path = Path(rf'files/ex_078.txt')
    contagem = []
    if visibilidade:
        resultado = factorial(num)
        for c in range (num, 0, -1): #contagem crescente para adicionar o calculo numa lista
            if c != 1:
                contagem.append(f'{c} x ')
            else:
                contagem.append(f'{c} = ') # quando chega ao final adiciona um igual

        with path.open('w', encoding='utf-8', errors='ignore') as file:
            for linha in contagem:
                file.write(f'{linha}')
            file.write(f'{resultado}')

    else:
        resultado = factorial(num)
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f'{resultado}')



header('FATORIAL')
num = int(input('Digite um número para calcularmos o fatorial: '))
visibilidade = input('Deseja visualizar o calculo completo?\n[1] - SIM\n[0] - NÃO\n--> ')
if visibilidade == '1':
    visibilidade = True
else:
    visibilidade = False
fatorial(num, visibilidade)