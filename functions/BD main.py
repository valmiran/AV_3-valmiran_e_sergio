import sqlite3
from usuario_db import cadastro_usuario, login_usuario
from produto_db import cadastro_produto, atualizar_produto, deletar_produto,listar_produto, buscar1_produto,venda_produto

conn = sqlite3.connect('sistema_database')
c = conn.cursor()
'''serve para cadastrar um usuario ou cliente no sistema '''
def cadastro():

    name = input('Digite seu email: ')
    password = input ('Digite sua senha: ') 
    endereco = input ('Digite seu endereço: ')
    cliente = input ('Digite seu nome: ')
    telefone = input ('Digite seu telefone: ')
    print('Cadastrado com sucesso!')
    cadastro_usuario(conn,name,password,endereco,cliente,telefone)

'''serve para fazer o inicio do login do usuario  '''
def login():
    
    email =  input('Digite o seu email: ')
    senha = input('Digite a sua senha: ')
    usuario_autenticado =  login_usuario (conn,email,senha)
    if len(usuario_autenticado) > 0:  
        print('Autenticado com Sucesso')
        main_interno()
    print(len(usuario_autenticado) > 0)   

''' é o menu inicial de entrada do sistema '''
def main_inicial():

    lista =  {
        1: cadastro,
        2: login,
        3: exit,
        
    }
    while True: 
      
        opc = int(input('\nBem Vindo a Loja !\n1- Cadastrar Usuario\n2- Realizar Login\n3- Sair Sistema \nDigite uma opção: '))
        if opc not in lista:
            print('Opção Inválida.Tente de Novo!')
        else: 
            lista[opc]()       

''' cadastra o um produto na tabela de bando de dados '''
def cadastrar():
    nome = input ('Digite o nome do produto que deseja Cadastrar: ')
    qtd = int (input('Digite o estoque: '))
    marca = input('Digite a marca do produto: ')
    preco = input ('Digite o preço: ')
    cadastro_produto(conn,nome,qtd,marca,preco)
''' atualiza um produto que já está inserido na tabela, serve para colocar o produto certo no lugar do errado '''
def atualizar():
    id = int(input('Digite o id do Produto: '))
    novo_produto = input ('Digite o novo nome do Produto: ')
    atualizar_produto(conn,id,novo_produto)
'''lista todos os produtos e suas informações ao todo '''
def buscar():
    produto = listar_produto(conn)
    print(produto)
    '''  '''
def deletar():
    id = (input('Digite o id do Produto para Deletar: '))
    deletar_produto(conn,id)
def buscar1():
    busca_name = (input('Digite o nome do produto para buscar: ')) 
    buscar1_produto(conn,busca_name)
def venda():
    venda = (input('Digite a data da venda: '))
    id_produto = int(input('Digite o id do produto: '))
    id_cliente = (input('Digite o id do cliente: '))
    quantidade =  int(input('Digite a quantidade: '))
    valor = input ('Insira o total da compra: ')
    print('Obrigado,volte sempre!')
    venda_produto(conn,venda,id_produto,id_cliente,quantidade,valor)
def main_interno():
    menu = {
        1: cadastrar,
        2: atualizar,
        3: buscar,
        4: deletar,
        5: buscar1,
        6: venda,
        7: exit,
    }
    while True:
        opcao = int(input('\n1- Cadastrar Produto\n2- Atualizar Produto\n3- Listar Produtos\n4- Deletar Produto\n5- Buscar 1 produto\n6- Venda\n7- Sair\nDigite a opção que deseja: '))
        if opcao not in menu:
            print('Opção Inválida. Tente novamente!')
        else:
            menu[opcao]()
main_inicial()