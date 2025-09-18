import sqlite3

DB_FILE = 'agenda.db'

def conectar_db(db_file):

    conn = None

    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(f"Erro {e}")
    
    return conn

def criar_tabela(conn):

    if conn is not None:
        try:

            cursor = conn.cursor()

            sql_create_table = """CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY, nome TEXT NOT NULL, telefone TEXT NOT NULL, email TEXT NOT NULL);"""

            cursor.execute(sql_create_table)
            conn.commit()

            print('Tabela contatos criada com sucesso')
        
        except sqlite3.Error as e:
            print(f'Erro: {e}')
    else:
        print("Não há conexão com o banco de dados")

def novo_contato(conn, contato):
    sql_insert_into = """INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)"""

    cursor = conn.cursor()
    cursor.execute(sql_insert_into, contato)
    conn.commit()
    return cursor.lastrowid

def visualizar_contatos(conn):
    sql_select = 'SELECT id, nome, telefone, email FROM contatos'

    cursor = conn.cursor()
    cursor.execute(sql_select)

    linhas = cursor.fetchall()

    if linhas:
        print('\nMeus Contatos')
        for linha in linhas:
            print(f'ID: {linha[0]} | Nome: {linha[1]} | Telefone: {linha[2]} | Email: {linha[3]}')
    else:
        print('Nenhuma tarefa encontrada.')

def atualizar_contato_telefone(conn, id_contato, telefone):
    sql_update = """UPDATE contatos SET telefone = ? WHERE id = ?"""

    cursor = conn.cursor()
    cursor.execute(sql_update, (telefone, id_contato))

    conn.commit()

    print(f"Telefone do Contato ID {id_contato} atualizado para {telefone}")

def atualizar_contato_email(conn, id_contato, email):
    sql_update = """UPDATE contatos SET email = ? WHERE id = ?"""

    cursor = conn.cursor()
    cursor.execute(sql_update, (email, id_contato))

    conn.commit()

    print(f"Email do Contato ID {id_contato} atualizado para {email}")

def deletar_contato(conn, id_contato):
    sql_delete_contato = """DELETE FROM contatos WHERE id = ?"""

    cursor = conn.cursor()
    cursor.execute(sql_delete_contato, (id_contato,))

    conn.commit()

    print(f'\nContato ID {id_contato} deletado com sucesso')

def visualizar_contato_por_nome(conn, nome):
    sql_select = 'SELECT id, telefone, email FROM contatos WHERE nome = ?'

    cursor = conn.cursor()
    cursor.execute(sql_select, (nome,))

    linha = cursor.fetchone()

    print(f'ID: {linha[0]} | Nome: {nome} | Telefone: {linha[1]} | Email: {linha[2]}')


conexao = conectar_db(DB_FILE)

if conexao:
    # criar_tabela(conexao)

    # contato = ('Kassandra', '777', 'kas@email')
    # contato_id = novo_contato(conexao, contato)

    # visualizar_contatos(conexao)

    # atualizar_contato_telefone(conexao, '1', '776')
    # atualizar_contato_email(conexao, '2', 'novo@email.com')

    # deletar_contato(conexao, 2)

    # visualizar_contatos(conexao)

    visualizar_contato_por_nome(conexao, 'Kassandra')

