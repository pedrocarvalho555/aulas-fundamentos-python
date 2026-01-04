'''
Desenvolva um programa que permita ao utilizador
calcular o seu Índice de Massa Corporal (IMC). O
programa deve solicitar ao utilizador a sua altura e
o seu peso. De seguida, utilizando uma função, deve
calcular o IMC e o programa deve gerar um ficheiro
txt com uma mensagem com base no valor do IMC
calculado.
● IMC abaixo de 18,5: Abaixo do peso
● IMC entre 18,5 e 24,9: Peso normal
● IMC entre 25,0 e 29,9: Sobrepeso
● IMC entre 30,0 e 34,9: Obesidade grau 1
● IMC entre 35,0 e 39,9: Obesidade grau 2
● IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida)
'''
from pathlib import Path

def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def imc_calc(peso: float, altura: float):
    path = Path(rf'files/ex_081.txt')
    print(peso)
    IMC = peso/(altura*altura)
    print(IMC)

    if IMC < 18.5:
        print(f'Abaixo do peso - IMC: {IMC:.2f}')
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f'Abaixo do peso - IMC: {IMC:.2f}')
    elif IMC > 18.5 and IMC < 24.9:
        print(f'Peso normal - IMC: {IMC:.2f}')
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f'Peso normal - IMC: {IMC:.2f}')
    elif IMC > 25.0 and IMC < 29.9:
        print(f'Sobrepeso - IMC: {IMC:.2f}')
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f'Sobrepeso - IMC: {IMC:.2f}')
    elif IMC > 30 and IMC < 34.9:
        print(f'Obesidade grau 1 - IMC: {IMC:2f}')
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f'Obesidade grau 1 - IMC: {IMC:2f}')
    elif IMC > 35 and IMC < 39.9:
        print(f'Obesidade grau 2 - IMC: {IMC:2f}')
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f'Obesidade grau 2 - IMC: {IMC:2f}')
    else:
        print(f'Obesidade grau 3 (obesidade mórbida) - IMC: {IMC:2f}')
        with path.open('w', encoding='utf-8', errors='ignore') as file:
            file.write(f'Obesidade grau 3 (obesidade mórbida) - IMC: {IMC:2f}')



header('EXERCICIO 80')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura (ex: 1.80, 1.54): '))
imc_calc(peso, altura)