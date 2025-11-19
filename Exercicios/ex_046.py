# soma de varios numeros que o utilizador insira
contador = 0
soma = 0
print('Soma infinita (digite 0 para parar, não é tão infinita assim)')
while True:
    numero = int(input('Digite um número: '))
    if numero == 0:
        break
    else:
        soma = numero + soma
        contador += 1
print(f'A soma dos {contador} números inseridos é {soma}')