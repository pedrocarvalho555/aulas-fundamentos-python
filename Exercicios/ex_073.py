def header(txt):
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def maior(lista: list):
    maior = 0
    for valor in lista:
        if valor > maior:
            maior = valor
    print(f'O maior valor é {maior}')

lista = list()
header('Qual o maior número')

while True:
    valor = int(input('Digite um número, digite 0 para sair\n---> '))
    if valor == 0:
        break
    else:
        lista.append(valor)

maior(lista)
