try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    divisao = num1/num2

except ValueError:
    print('Por favor digite um número válido.')

except ZeroDivisionError:
    print('Não é possível dividir por zero.')

else:
    print(f'{num1} / {num2} = {divisao}')

finally:
    print('Programa encerrado!')