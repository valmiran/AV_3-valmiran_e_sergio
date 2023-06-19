
def cadastro_usuario (conexao,name,password,endereco,cliente,telefone):
    
    cursor = conexao.cursor()
    sql = f'INSERT INTO locadora(cliente_email,cliente_password,cliente_endereco,cliente_nome,cliente_telefone) VALUES (?,?,?,?,?)'
    cursor.execute(sql,[name,password,endereco,cliente,telefone])
    conexao.commit()
def login_usuario(conexao,email):
           
        cursor = conexao.cursor()
        sql = 'select * from locadora WHERE cliente_email=? '
        cursor.execute(sql,
                   [email
    ])
       
        return cursor.fetchall()