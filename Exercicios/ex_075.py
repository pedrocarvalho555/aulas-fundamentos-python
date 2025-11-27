def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def tabuada(num: int):
    for c in range (1, 11):
        print(f'{num} x {c} = {num*c}')

header('TABUADA')
num = int(input('Digite um número para fazermos a tabuada: '))
tabuada(num)