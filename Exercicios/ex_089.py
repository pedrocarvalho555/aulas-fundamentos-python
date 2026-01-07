'''
Crie uma Interface Simples no Terminal
para Gestão de Produtos.
O programa deve permitir:

Adicionar novos produtos (com nome, preço e
stock),
Mostrar todos os produtos da base de dados,
Alterar um produto existente (nome, preço ou
stock).
'''

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

def adicionar_produtos() -> None:
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

def consulta_produtos() -> None:
    header('Lista de Produtos')
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()
    conn.close()

    for produto in produtos:
        print(f'ID: {produto[0]} | NOME: {produto[1]} | PREÇO: {produto[2]} € | STOCK: {produto[3]}' )
        print('-------------------------------------------------------------------------------------')

    print()# só para dar um \n

def editar_produto() -> None:
    header('Editar Produto')
    conn = conectar()
    cursor = conn.cursor()
    id = int(input('Digite o id do produto que deseja editar: '))
    novo_nome = input('Digite o novo nome do produto: ')
    novo_preco = float(input('Digite o novo preço do produto: '))
    novo_stock = int(input('Digite a nova quantia do produto: '))

    conn.execute("UPDATE PRODUTOS SET nome = ?, preco = ?, stock = ? WHERE id = ?", (novo_nome, novo_preco, novo_stock, id))

    conn.commit()
    conn.close()

def menu()-> None:
    while True:
        header('LOJA')
        print('[1] - Consultar Produtos')
        print('[2] - Adicionar Produtos')
        print('[3] - Editar Produtos')
        print('[4] - Sair')
        opcao = int(input('--> '))

        match opcao:
            case 1:
                consulta_produtos()
            case 2:
                adicionar_produtos()
            case 3:
                editar_produto()
            case 4:
                break
            case _:
                print('Inválido')


if __name__ == '__main__':
    menu()