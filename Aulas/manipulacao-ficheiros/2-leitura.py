from pathlib import Path

caminho = Path(r'files/test.txt')

with caminho.open('r', encoding='utf-8', errors='ignore') as file:
    for linha in file:
        print(linha)