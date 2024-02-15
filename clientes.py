# importando a biblioteca de conexão com o banco de dados
#  vamos adicionar um alias a biblioteca
import mysql.connector as mc


# vamos estabelecer a conexão com o banco de dados
# e para tal, iremos passar os seguintes dados:
# servidor, porta, usuario, senha, banco
conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
# Estamos testando a conexão pedindo para exibir o ID da conexão
# Caso exiba uma pilha de erros, então tem um erro na linha
# de conexão
print(conexao)

# Para se movimentar dentro da estrutura de banco de dados
# E retonar dos dados necessáios, iremos criar um cursor
cursor = conexao.cursor()


# Vamos executar um comando usando o cursor
# cursor.execute("Create database Ola")

# cursor.execute("insert into clientes(nome_cliente, email, telefone)values('Ana','Anacarol@gmail.com','(11) 96532-6548')")

# Vamos selecionar todos os dados da tabela clientes
cursor.execute("Select * from banco.clientes")
print(cursor)
for c in cursor:
    print(f"Id do cliente: {c[0]}")
    print(f"Nome do cliente: {c[1]}")
    print(f"Email do cliente: {c[2]}")
    print(f"Telefone do cliente: {c[3]}")