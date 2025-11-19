maiores = 0
menores = 0
for c in range (0, 7):
    ano_nasc = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))
    idade = 2025 - ano_nasc
    if idade >= 18:
        print(f'Alguem com {idade} anos é maior de idade')
        maiores+=1
    else:
        print(f'Alguem com {idade} anos é menor de idade')
        menores+=1

print(f'Existem {maiores} pessoas que são maiores de idade')
print(f'Existem {menores} pessoas que são menores de idade')