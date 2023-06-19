import sqlite3
from sys import exit
from usuario_db import cadastro_usuario, login_usuario
from produto_db import cadastro_produto, atualizar_produto, deletar_produto, listar_produto, buscar1_produto, venda_produto

conn = sqlite3.connect('sistema_database')
c = conn.cursor()

def login():
    email = input('Digite o seu email: ')
    senha = input('Digite a sua senha: ')
    usuario_autenticado = login_usuario(conn, email, senha)
    if usuario_autenticado is not None:
        print('Autenticado com Sucesso')
        main_interno()
    print(usuario_autenticado is not None)

def main_inicial():
    lista = {
        1: login,
        2: exit,
    }
    while True:
        opc = int(input('\nBem Vindo à Loja!\n1- Realizar Login\n2- Sair do Sistema\nDigite uma opção: '))
        if opc not in lista:
            print('Opção Inválida. Tente Novamente!')
        else:
            lista[opc]()

def cadastrar():
    nome = input('Digite o nome do produto que deseja cadastrar: ')
    qtd = int(input('Digite o estoque: '))
    marca = input('Digite a marca do produto: ')
    preco = input('Digite o preço: ')
    cadastro_produto(conn, nome, qtd, marca, preco)

def atualizar():
    id = int(input('Digite o ID do Produto: '))
    novo_produto = input('Digite o novo nome do Produto: ')
    atualizar_produto(conn, id, novo_produto)

def buscar():
    produto = listar_produto(conn)
    print(produto)

def deletar():
    id = input('Digite o ID do Produto para Deletar: ')
    deletar_produto(conn, id)

def buscar1():
    busca_name = input('Digite o nome do produto para buscar: ')
    buscar1_produto(conn, busca_name)

def venda():
    venda_data = input('Digite a data da venda: ')
    id_produto = int(input('Digite o ID do produto: '))
    id_cliente = input('Digite o ID do vendedor(a): ')
    quantidade = int(input('Digite a quantidade: '))

    # Atualizar a quantidade em estoque do produto vendido
    c.execute("SELECT produto_qtd FROM peças WHERE produto_id= ?", (id_produto,))
    result = c.fetchone()
    if result is not None:
        estoque_atual = result[0]  # Coluna de estoque (supondo que seja a segunda coluna)
        if estoque_atual >= quantidade:
            novo_estoque = estoque_atual - quantidade
            c.execute("UPDATE peças SET produto_qtd=? WHERE produto_id=?", (novo_estoque, id_produto))
            conn.commit()
        else:
            print("Quantidade insuficiente no estoque!")
            return
    else:
        print("Produto não encontrado!")
        return

    # Buscar o preço do produto na tabela "peças"
    c.execute("SELECT produto_preco FROM peças WHERE produto_id=?", (id_produto,))
    result = c.fetchone()
    if result is not None:
        preco_unitario = result[0]
        preco_total = quantidade * preco_unitario
        valor = round(float(preco_total.replace(',', '').replace('.', '')), 2)  # as virgulas convertem o valor em float
        
        print(f"Preço total da venda: R$ {valor}")
    else:
        print("Erro ao obter preço do produto.")

    venda_produto(conn, id_produto, id_cliente, quantidade, valor, venda_data)
    print("Venda registrada com sucesso!")

def main_interno():
    menu = {
        1: cadastrar,
        2: atualizar,
        3: buscar,
        4: deletar,
        5: buscar1,
        6: venda,
        7: cadastrar_usuario,
        8: exit,
    }
    while True:
        opcao = int(input('\n1- Cadastrar Produto\n2- Atualizar Produto\n3- Listar Produtos\n4- Deletar Produto\n5- Buscar 1 produto\n6- Venda\n7- Cadastrar Usuário\n8- Sair\nDigite a opção desejada: '))
        if opcao not in menu:
            print('Opção Inválida. Tente novamente!')
        else:
            menu[opcao]()

def cadastrar_usuario():
    name = input('Digite seu email: ')
    password = input('Digite sua senha: ')
    endereco = input('Digite seu endereço: ')
    cliente = input('Digite seu nome: ')
    telefone = input('Digite seu telefone: ')
    print('Cadastrado com sucesso!')
    cadastro_usuario(conn, name, password, endereco, cliente, telefone)

main_inicial()
