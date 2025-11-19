lista_base = []
lista_par = []
lista_impar = []

while True:
    user_in = int(input('Digite um número, digite um numero negativo para sair: '))
    if user_in < 0:
        break
    else:
        lista_base.append(user_in)

for valor in lista_base:
    if valor % 2 == 0:
        lista_par.append(valor)
    else:
        lista_impar.append(valor)

print(lista_base)
print(lista_par)
print(lista_impar)