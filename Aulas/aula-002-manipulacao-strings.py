string = 'Python é poderoso'

# Fatiamento de string / String Slicer

print(string[7]) #é
print(string[-1]) #último caracter
print(string[:6]) #Python
print(string[9:]) #poderoso
print(string[::2]) # Inicio ao fim de dois em dois
print(string[::-1]) # Mostra a string ao contrário

# Analíse de String / String Analysis

print(len(string)) # Tamanho da string
print(string.count('o')) # Conta quantos "o" existem na string
print('Python' in string) # Verifica se existe a palavra "Python" na string devolvendo true ou false
print(string.find('é'))  # Devolve a posição do solicitado
print(string.find('Olé')) # não encontra e devolve -1
print(string.startswith('Python')) # Procura se a string começa com "Python" e devolve true ou false
print(string.endswith('Fraquinho')) # Procura se a string termina com "Fraquinho" e devolve true ou false

# Transformação de String / String Transfiguration
string = input('Digite uma frase:\n-->')

print(len(string)) #qual o tamanho da frase
print(len(string.strip())) #remove todos os espaços à esquerda e à direita da string
print(len(string.rstrip())) #remove todos os espaços à direita da string
print(string.lower()) #transforma todos os caracteres em minusculo
print(string.upper()) #transforma todos os caracteres em maiusculo
print(len(string.replace(' ', '')))


