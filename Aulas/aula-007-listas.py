from math import fsum
notas = list()

for c in range(5):
    nota = float(input(f'Digite a {c+1}ª nota: '))
    notas.append(nota)

media = fsum(notas) / len(notas)
print(media)
