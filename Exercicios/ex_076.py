def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def conversor(num):
    fahrenheit = (num * 1.8) + 32
    print(f'{num}ºC = {fahrenheit}ºF')

# main

header('CONVERSOR DE TEMPERATURA')
num = int(input('Digite uma temperatura em Celsius para convertermos em Fahrenheit: '))

conversor(num)