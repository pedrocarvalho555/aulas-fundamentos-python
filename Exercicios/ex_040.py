'''
#metodo gambiarra
maior = 0
menor = 1000
for c in range (0, 10):
    idade_in = int(input(f'Digite a idade da {c+1}ª pessoa: '))
    if idade_in > maior:
        maior = idade_in
    if idade_in < menor:
        menor = idade_in
print(f'A pessoa mais velha tem {maior} anos')
print(f'A pessoa mais nova tem {menor} anos')'''

maior = 0
menor = 0
for c in range (0, 10):
    idade_in = int(input(f'Digite a idade da {c+1}ª pessoa: '))
    if c == 0:
        maior_idade = idade_in
        menor_idade = idade_in
    else:
        if idade_in > maior:
            maior = idade_in
        if idade_in < menor:
            menor = idade_in
print(f'A pessoa mais velha tem {maior} anos')
print(f'A pessoa mais nova tem {menor} anos')