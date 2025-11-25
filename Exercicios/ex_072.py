def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def contagem(inicio,fim,passo): # vou fazer tudo na mesma contagem
    if passo > 0:
        for c in range(inicio,fim+1,passo):
            print(c)
    elif passo < 0:
        for c in range(fim,inicio-1,passo):
            print(c)
    else:
        print('O passo não pode ser 0')


#main
header('EXERCÍCIO 72')
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
contagem(inicio,fim,passo)

