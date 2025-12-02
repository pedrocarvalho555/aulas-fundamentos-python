import os

# nome = 'files'
# os.mkdir(nome) # cria apenas uma pasta, se ela já existir dá erro

caminho = 'ficheiros/files'
os.makedirs(caminho, exist_ok=True) # cria varias pastas, exists_ok=True significa que se a pasta existir ele nao faz nada