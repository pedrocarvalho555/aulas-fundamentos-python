try:
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    divisao = num1/num2


#except Exception as e: #apenas para dev, guarda a exception num variavel
#print('Ups! Algo correu mal')
#print(str(e))

except ValueError:
    print('Por favor digite um número válido.')

except ZeroDivisionError:
    print('Não é possível dividir por zero.')

except KeyboardInterrupt:
    print('O utilizador encerrou o programa.')

else:
    print(f'{num1} / {num2} = {divisao}')

finally:
    print('Programa encerrado!')