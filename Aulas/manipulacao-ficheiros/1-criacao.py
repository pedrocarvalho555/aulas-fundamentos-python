from pathlib import Path # classe path que dá métodos/funções típicas de ficheiro

# Informar qual é o caminho do ficheiro
# criar a variável que representa o caminho do ficheiro
caminho = Path(r'files/test.txt')


# O Python cria o ficheiro se ele não existir
# Podemos abrir o ficheiro em modo:
# Write - 'w'
# Read - 'r'
# Append - 'a'

with caminho.open('w', encoding='utf-8', errors='ignore') as file:
    file.write('Olá turma')
    file.write('Olá novamente')
