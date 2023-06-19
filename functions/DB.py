import sqlite3 
conn = sqlite3.connect('sistema_database')
c = conn.cursor()
'''Nesse folder esta a conexão da linguagem SQL para a integração do banco de dados 
para com o resto do programada sendo consultada no BD main.py  '''

c.execute('''
            CREATE TABLE locadora(
            clientes_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_email VARCHAR(150),
            cliente_password VARCHAR (150),
            cliente_endereco VARCHAR (150),
            cliente_nome VARCHAR (150),
            cliente_telefone INTEGER (22)
            )

        ''')
conn.commit()
conn = sqlite3.connect('sistema_database')
c = conn.cursor()
c.execute('''
    CREATE TABLE peças (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        produto_nome TEXT,
        produto_qtde INTEGER,
        produto_marca TEXT,
        produto_preco REAL
    )
''')

conn.commit()
conn = sqlite3.connect('sistema_database')
c = conn.cursor()
c.execute('''
            CREATE TABLE venda(
            venda_id INTEGER PRIMARY KEY AUTOINCREMENT,
            venda_data VARCHAR (150),
            venda_qtd  NUMERIC (22),
            venda_total NUMERIC (22),
            produto_id INTEGER NOT NULL REFERENCES produto(produto_id),
            clientes_id INTEGER NOT NULL REFERENCES clientes(clientes_id)
            )
        
        ''')
conn.commit()
