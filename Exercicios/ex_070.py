def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def area(altura, largura):
    largura = altura * largura
    print(f'O terreno tem {largura}m de área')

#main

header('Área de um terreno')
altura = int(input('Digite a altura do terreno: '))
largura = int(input('Digite a largura do terreno: '))
area(altura, largura)
