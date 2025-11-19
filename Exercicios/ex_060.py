user_in = input('Digite uma expressão matemática: ')

if user_in.count('(') == user_in.count(')'):
    print('A expressão está correta')
else:
    print('A expressão está incorreta')