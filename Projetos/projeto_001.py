print(' --- CALCULADORA IMC --- ')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

IMC = peso / (altura * altura)

if IMC < 18.5:
    print(f'Abaixo do peso - IMC: {IMC:.2f}')
elif IMC > 18.5 and IMC < 24.9:
    print(f'Peso normal - IMC: {IMC:.2f}')
elif IMC > 25.0 and IMC < 29.9:
    print(f'Sobrepeso - IMC: {IMC:.2f}')
elif IMC >30 and IMC < 34.9:
    print(f'Obesidade grau 1 - IMC: {IMC:2f}')
elif IMC > 35 and IMC <39.9:
    print(f'Obesidade grau 2 - IMC: {IMC:2f}')
else:
    print(f'Obesidade grau 3 (obesidade mórbida) - IMC: {IMC:2f}')