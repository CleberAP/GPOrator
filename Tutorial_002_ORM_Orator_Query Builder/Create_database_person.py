import sqlite3

# nome do banco de dados que será criado
db_name = 'person.db'

# Bloco que cria a tabela person
try:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Declarando a query de criação da tabela person
    sql = """
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name Varchar(20),
        last_name Varchar(30),
        sex Char,
        birth_date DATE
    )
    """

    # Executando a query
    try:
        cursor.execute(sql)
        conn.commit()
    except sqlite3.IntegrityError as erro:
        print(erro)
        
except sqlite3.Error as erro:
    print(erro)

# Bloco que adiciona a coluna age na tabela person
try:
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Declarando a query de criação da tabela person
    sql = """ALTER TABLE person ADD COLUMN age INTEGER DEFAULT 0"""

    # Executando a query
    try:
        cursor.execute(sql)
        conn.commit()
    except sqlite3.IntegrityError as erro:
        print(erro)
        
except sqlite3.Error as erro:
    print(erro)

    
