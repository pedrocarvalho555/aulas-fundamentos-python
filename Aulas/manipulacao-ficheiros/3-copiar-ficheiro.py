from pathlib import Path

input_data = Path(r'files/test.txt')
output = Path(r'files/test2.txt')

with input_data.open('r', encoding='utf-8', errors='ignore') as file:
    dados = file.readlines()

with output.open('w', encoding='utf-8', errors='ignore') as output:
    for linha in dados:
        output.write(linha)