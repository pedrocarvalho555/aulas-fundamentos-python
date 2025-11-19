print('Calculadora de médias')
contador = 0
maior = 0
menor = 0
soma = 0
print('Digite 0 para sair do programa')
while True:
    nota = float(input(f'Digite a {contador+1}º nota: '))
    if nota == 0:
        print('A sair do programa')
        break
    if contador == 0:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota
    contador+=1
    soma = nota + soma

print(f'A média das {contador} notas é {soma / contador}')
print(f'A maior nota foi {maior} e a menor foi {menor}')