def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def conversor(num: float):
    fahrenheit = (num * 1.8) + 32
    print(f'{num}ºC = {fahrenheit:.2f}ºF')

# main

header('CONVERSOR DE TEMPERATURA')
num = float(input('Digite uma temperatura em Celsius para convertermos em Fahrenheit: '))

conversor(num)