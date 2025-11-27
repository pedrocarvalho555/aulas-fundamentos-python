def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def contagem(inicio: int, fim: int, passo: int): # vou fazer tudo na mesma contagem

    if passo > 0 or (inicio > fim): # para fazer as contagens normais (0-20) e as invertidas (30-10)
        for c in range(inicio,fim,passo):
            print(c)
    elif passo < 0: # faz quase a mesma coisa que o primeiro if
        for c in range(fim,inicio,passo): # mas serve para os casos em que o utilizador escrever
            print(c) # inicio = 30 fim = 10 passo = -1 por exemplo
    else:
        print('O passo não pode ser 0')


#main
header('EXERCÍCIO 72')
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contagem(inicio,fim,passo)

