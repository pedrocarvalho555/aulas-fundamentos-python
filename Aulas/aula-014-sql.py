# Estabelecer a ligação
# 1 - Importar a biblioteca necessária
import sqlite3

def header (txt: str) -> None:
    '''
    Cabeçalho genérico que utilizo em literamente tudo que é lado
    '''
    print('-'*30)
    print(f'{txt:-^30}')
    print('-'*30)

# 2 - Iniciar a conexão
def conectar():
    try:
        return sqlite3.connect('tarefas.db')
    except Exception as e:
        print(f'Erro ao iniciar a ligação à base de dados: {str(e)}')
        return ''

# Criar uma tabela
def criar_tabela():
    # criar conexão
    conn = conectar()

    # criar o cursor
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL,
            estado TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_tarefa():
    header('Adicionar Tarefa')
    desc = input('Descrição: ').strip()
    estado = 'Pendente'

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (descricao, estado) VALUES (?, ?)", (desc, estado))
    conn.commit()
    conn.close()

    print(f'Tarefa "{desc}" adicionada com sucesso')

def consultar_tarefa():
    header('Consultar Tarefas')

    conn = conectar()
    cursor = conn.cursor()
    conn.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()

    for tarefa in tarefas:
        print(f'ID: {tarefa[0]} | DESCRIÇÃO: {tarefa[1]} | ESTADO: {tarefa[2]}')
        print('---------------------------------------------------------------')


def terminar_tarefa():
    header('Terminar Tarefa')
    id_tarefa = input('Digite o ID da tarefa: ')

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("UPDATE tarefas SET estado = ? WHERE id = ?", ('Concluido', int(id_tarefa)))

    conn.commit()
    conn.close()

    print(f'Tarefa nº{id_tarefa} concluída')


def apagar_tarefa():
    header('Apagar Tarefa')
    id_tarefa = input('Digite o ID da tarefa: ')

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (int(id_tarefa),))

    conn.commit()
    conn.close()

    print(f'Tarefa nº{id_tarefa} apagada')

def menu():
    criar_tabela()
    while True:
        header('Tarefas')
        print('[1] - Adicionar tarefa')
        print('[2] - Consultar tarefas')
        print('[3] - Concluir tarefa')
        print('[4] - Apagar tarefa')
        print('[5] - Sair')
        opcao = int(input('--> '))

        match opcao:
            case 1:
                adicionar_tarefa()
            case 2:
                consultar_tarefa()
            case 3:
                terminar_tarefa()
            case 4:
                apagar_tarefa()
            case 5:
                break
            case _:
                print('Opção inválida...')


if __name__ == '__main__':
    menu()