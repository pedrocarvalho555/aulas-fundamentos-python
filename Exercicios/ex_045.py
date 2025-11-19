numero = int(input('Digite um número: '))
range = 1
previous_number = 0
current_number = 1
fibonacci = 0

while range <= numero:
    print(f'{previous_number} ', end='')
    fibonacci = previous_number + current_number
    previous_number = current_number
    current_number = fibonacci
    range+=1