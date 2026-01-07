import sqlite3

def conectar():
    try:
        return sqlite3.connect('loja.db')
    except Exception as e:
        print(f'Erro ao iniciar a ligação à base de dados: {str(e)}')
        return ''

def criar_tabela():
    conn = conectar()

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()