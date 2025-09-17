import sqlite3

# Definindo o nome do arquivo de banco de dados
DB_FILE = 'todo_list.db'

def conectar_db(db_file):
    """Cria uma conexão com o banco de dados"""

    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print("Conexão estabelecida com sucesso")
    except sqlite3.Error as e:
        print(f'Erro ao conectar ao banco de dados {e}')
    
    return conn

def criar_tabela(conn):
    """Cria a tabela 'tarefas'"""

    if conn is not None:
        try:
            # Um 'cursor' é necessário para executar comandos SQL
            cursor = conn.cursor()
            
            # O Comando SQL para criar a tabela
            sql_create_tarefas_table = """CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY, descricao TEXT NOT NULL, concluida BOOLEAN);
            """

            cursor.execute(sql_create_tarefas_table)
            conn.commit() # Salvando as alterações no arquivo

            print("Tabela 'tarefas' criada com sucesso ou já existente")
        
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela {e}")
    else:
        print("Não há conexão com o banco de dados.")

def inserir_tarefa(conn, tarefa):
    """Insere uma nova tarefa na tabela 'tarefas'
    A tarefa é uma tupla no formato: (descricao, concluida)"""

    sql = """INSERT INTO tarefas(descricao, concluida) VALUES (?, ?)"""

    cursor = conn.cursor()
    cursor.execute(sql, tarefa)
    conn.commit()
    return cursor.lastrowid #Retorna o ID da tarefa

def selecionar_todas_tarefas(conn):
    """Consulta todas as linhas na tabela 'tarefas'"""
    sql = 'SELECT id, descricao, concluida FROM tarefas'

    cursor = conn.cursor()
    cursor.execute(sql)

    # O metódo 'fetchall()' recupera todos os resultados
    linhas = cursor.fetchall()

    if linhas:
        print('\n---Minha Lista de Tarefas---')
        for linha in linhas:
            # Verifica o valor booleano (0 ou 1) e converte para um texto
            status = "CONCLUÍDA" if linha[2] else "PENDENTE"

            print(f'ID: {linha[0]} | Status : {status} | Descrição: {linha[1]}')
    else:
        print("Nenhuma tarefa encontrada")

def atualizar_tarefa_status(conn, id_tarefa, status):
    """Atualiza o status (concluida) de uma tarefa pelo ID"""

    sql = """UPDATE tarefas SET concluida = ? WHERE id = ?"""

    cursor = conn.cursor()
    # Os valores que serão substituidos nos '?' são passados na tupla

    cursor.execute(sql, (status, id_tarefa))
    conn.commit()
    print(f'Status da Tarefa ID {id_tarefa} atualizado para {status}')

# Tentativa de Conexão
conexao = conectar_db(DB_FILE)

# Executa a criação da tabela
# if conexao:
#     criar_tabela(conexao)

# if conexao:
#     # A primeira tarefa: (descricao, concluida)
#     tarefa_1 = ('Aprender a criar BD em Python', 0)
#     tarefa_id_1 = inserir_tarefa(conexao, tarefa_1)

#     # A segunda tarefa> (descricao, concluida)
#     tarefa_2 = ('Ler o livro SQL', 0)
#     tarefa_id_2 = inserir_tarefa(conexao, tarefa_2)

# Retornando todas as tarefas do To-Do
# if conexao:
#     selecionar_todas_tarefas(conexao)

if conexao:
    # Marca a tarefa de ID 1 como concluida (status = 1)
    atualizar_tarefa_status(conexao, 1, 1)

    # Vamos ver a lista novamente para conferir
    selecionar_todas_tarefas(conexao)
