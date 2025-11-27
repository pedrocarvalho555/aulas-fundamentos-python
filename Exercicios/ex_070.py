def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def area(altura: float, largura: float):
    largura = altura * largura
    print(f'O terreno tem {largura:.2f}m2 de área')

#main

header('Área de um terreno')
altura = float(input('Digite a altura do terreno: '))
largura = float(input('Digite a largura do terreno: '))
area(altura, largura)
