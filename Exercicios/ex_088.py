import sqlite3

def conectar():
    try:
        return sqlite3.connect('loja.db')
    except Exception as e:
        print(f'Erro ao iniciar a ligação à base de dados: {str(e)}')
        return ''

def editar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    values = [(10, 5), (60, 6), (80, 7)] # uma lista com os valores para a query

    cursor.executemany("UPDATE produtos SET preco = ? WHERE id = ?", values)

    conn.commit()
    conn.close()

editar_produtos()