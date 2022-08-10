# _*_ coding: utf-8 _*_

# dbteste.py

import sqlite3

connection = sqlite3.connect("bdlivraria3.db") # definimos o banco de dados Livraria

csr = connection.cursor()

#Criação de Tabelas
def create_tables():
    csr.execute("""CREATE TABLE IF NOT EXISTS Cliente
               (codigo integer primary key, telefone text, endereco text,
                cpf text, tipo text)
                """)

    csr.execute("""CREATE TABLE IF NOT EXISTS Livro
               (ISBN integer primary key, quantidade integer, assunto text, Autor text,
                codeditora integer)
                """)

    csr.execute("""CREATE TABLE IF NOT EXISTS Editora
               (CodigoE integer primary key, enderecoE text, Telefone integer, gerente text)
                """)

    csr.execute("""CREATE TABLE IF NOT EXISTS ClienteCompraLivro
               (codigoCliente integer primary key, ISBN text)
                """)
#inclusao de clientes
def insert_Cliente(codigo, telefone, endereco, cpf, tipo):
    csr.execute("""INSERT INTO Cliente VALUES(?,?,?,?,?)""", 
                   (codigo, telefone, endereco, cpf, tipo))

#exibe lista de clientes
def exibe_Clientes():
    rows = csr.execute("""SELECT * FROM Cliente""")

    for row in rows:
        print("codigo = " + str(row[0]))
        print("telefone = " + row[1])
        print("endereco = " + row[2])
        print("cpf = " + row[3])
        print("tipo = " + row[4])
        print()

def Update_Cliente(codigo, telefone, endereco, cpf, tipo):
    csr.execute("UPDATE Cliente SET telefone =?, endereco =?, cpf =?, tipo =? WHERE codigo = ?", (telefone,endereco,cpf,tipo,codigo))

def Delete_Cliente(codigo):
    csr.execute("DELETE FROM Cliente WHERE codigo =?", (codigo,))

def Search_Cliente(codigo):
    rows = csr.execute("""SELECT * FROM Cliente WHERE codigo =?""", (codigo,))
    
    for row in rows:
        print("codigo = " + str(row[0]))
        print("telefone = " + row[1])
        print("endereco = " + row[2])
        print("cpf = " + row[3])
        print("tipo = " + row[4])
        print()



#Livro

def insert_Livro(isbn, quantidade, assunto, autor, codeditora):
    csr.execute("""INSERT INTO Livro VALUES(?,?,?,?,?)""", 
                   (isbn, quantidade, assunto, autor, codeditora))     

def exibe_Livros():
    rows = csr.execute("""SELECT * FROM Livro""")

    for row in rows:
        print("ISBN = " + str(row[0]))
        print("quantidade = " + str(row[1]))
        print("assunto = " + row[2])
        print("autor = " + row[3])
        print("codeditora = " + str(row[4]))
        print()

def Update_Livro(isbn, quantidade, assunto, autor, codeditora):
    csr.execute("UPDATE Livro SET quantidade =?, assunto =?, autor =?, codeditora =? WHERE ISBN = ?", (quantidade, assunto, autor, codeditora, isbn))

def Delete_Livro(isbn):
    csr.execute("DELETE FROM Livro WHERE ISBN =?", (isbn,))

def Search_Livro(isbn):
    rows = csr.execute("""SELECT * FROM Livro WHERE ISBN =?""", (isbn,))
    
    for row in rows:
        print("ISBN = " + str(row[0]))
        print("quantidade = " + str(row[1]))
        print("assunto = " + row[2])
        print("autor = " + row[3])
        print("cod editora = " + str(row[4]))
        print()
        



#tabela Editora


def insert_Editora(CodigoE, enderecoE, Telefone, gerente):
    csr.execute("""INSERT INTO Editora VALUES(?,?,?,?)""", 
                   (CodigoE, enderecoE, Telefone, gerente))     

def exibe_Editora():
    rows = csr.execute("""SELECT * FROM Editora""")

    for row in rows:
        print("CodigoE = " + str(row[0]))
        print("endereco = " + row[1])
        print("Telefone = " + str(row[2]))
        print("gerente = " + row[3])
        print()

def Update_Editora(CodigoE, enderecoE, Telefone, gerente):
    csr.execute("UPDATE Editora SET enderecoE =?, Telefone =?, gerente =? WHERE CodigoE = ?", (enderecoE, Telefone, gerente, CodigoE))

def Delete_Editora(CodigoE):
    csr.execute("DELETE FROM Editora WHERE CodigoE =?", (CodigoE,))

def Search_Editora(CodigoE):
    rows = csr.execute("""SELECT * FROM Editora WHERE CodigoE =?""", (CodigoE,))
    
    for row in rows:
        print("Codigo = " + str(row[0]))
        print("endereco = " + row[1])
        print("Telefone = " + str(row[2]))
        print("gerente = " + row[3])
        print()




#tabela ClienteCompraLivro

def insert_ClienteCompraLivro(codigoCliente, ISBN):
    csr.execute("""INSERT INTO ClienteCompraLivro VALUES(?,?)""", 
                   (codigoCliente, ISBN))     

def exibe_ClienteCompraLivro():
    rows = csr.execute("""SELECT * FROM ClienteCompraLivro""")

    for row in rows:
        print("codigoCliente = " + str(row[0]))
        print("ISBN = " + str(row[1]))
        print()

def Update_ClienteCompraLivro(codigoCliente, ISBN):
    csr.execute("UPDATE ClienteCompraLivro SET ISBN =? WHERE codigoCliente = ?", (ISBN,codigoCliente))

def Delete_ClienteCompraLivro(codigoCliente):
    csr.execute("DELETE FROM ClienteCompraLivro WHERE codigoCliente =?", (codigoCliente,))

def Search_ClienteCompraLivro(codigo):
    rows = csr.execute("""SELECT * FROM ClienteCompraLivro WHERE codigoCliente =?""", (codigo,))
    
    for row in rows:
        print("codigoCliente = " + str(row[0]))
        print("ISBN = " + str(row[1]))
        print()



#Aqui começa o programa principal...
#professor eu testei todos e funcionaram perfeitamente.


connection.commit()


connection.close()