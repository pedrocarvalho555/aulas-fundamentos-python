def soma (n1: int, n2: int):
    s = n1 + n2
    print(f'A soma deu {s}')
    return s

resultado = soma(5, 5)
print(f'O return é {resultado}')

def soma2 (lista: list):
    soma = 0
    for numeros in lista:
        soma += numeros
    return soma

notas = [10, 14, 16, 10, 20]

media = soma2(notas) / len(notas)

print(f'A média é {media}')
