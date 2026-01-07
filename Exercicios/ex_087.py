import sqlite3

def header (txt: str) -> None:
    '''
    Cabeçalho genérico que utilizo em literamente tudo que é lado
    '''
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

def conectar():
    try:
        return sqlite3.connect('loja.db')
    except Exception as e:
        print(f'Erro ao iniciar a ligação à base de dados: {str(e)}')
        return ''

def adicionar_produtos():
    header('Adicionar Produto')
    produtos = [] # lista que vai conter uma tuple com os detalhes dos produtos
    while True:
        produtos_temp = () # cria/apaga uma tuple
        nome = input('Digite o nome do produto [Digite SAIR para sair]\n--> ')
        if nome == 'SAIR':
            break
        preco = float(input('Digite o preço do produto: '))
        stock = int(input('Digite a quantia: '))
        produtos_temp = (nome, preco, stock) # preenche a tuple
        produtos.append(produtos_temp) # insere na lista

    conn = conectar()
    cursor = conn.cursor()

    cursor.executemany("INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)", produtos)

    conn.commit()
    conn.close()

    print('Produtos adicionados com sucesso')

adicionar_produtos()