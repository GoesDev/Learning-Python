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
    pass

def visualizar_contatos(conn):
    pass

def atualizar_contato_telefone(conn, id_contato, telefone):
    pass

def atualizar_contato_email(conn, id_contato, email):
    pass

def deletar_contato(conn, id_contato):
    pass

def visualizar_contato_por_nome(conn, nome):
    pass


conexao = conectar_db(DB_FILE)

if conexao:
    criar_tabela(conexao)