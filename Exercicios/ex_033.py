soma = 0
for c in range (0, 5):
    num = int(input(f'Digite o {c+1}º número: '))
    soma += num

print(f'A média é {soma/5}')