# Conexão do Python com o MySQL

!["Imagem da Conexao Python com MySQL"](https://www.learntek.org/blog/wp-content/uploads/2019/06/Mysql-python.png)

## Drive de comunicação com o MySQL
Para estabelecer a comunicação entre python e o banco de dados mysql, iremos usar o seguinte drive:
<a href="https://pypi.org/project/mysql-connector-python/"> https://pypi.org/project/mysql-connector-python/ </a>

### Comando para instalar o drive
```python
    python -m pip install mysql-connector-python
```
### Configuração do banco de dados MySQL
O nosso banco de dados está num container de docker. Para acessá-lo será necessário criar o container, então faremos os seguintes comandos em um servidor Fedora com o docker instalado:

#### Criação do volume
```shell
mkdir dadosclientes
```


#### Criação do container
<center>
<img src="https://cdn.iconscout.com/icon/free/png-512/free-docker-3521391-2944835.png?f=webp&w=256" height="250" width="250">
</center>

```shell
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=senac@123 -d mysql
```

### Criação do banco de dados  e da tabela clientes

```sql
CREATE DATABASE banco;
USE banco;
CREATE TABLE clientes(
cliente_id int auto_increment primary key,
nome_cliente varchar(50) not null,
email varchar(100) not null unique,
telefone varchar(20)
)
```

#### Arquivo clientes.py

```python
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



```

#### Arquivo para cadastrar clientes: cad_clientes.py

```python
import mysql.connector as mc
# Estabelecer conexão com o banco
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

# verificar se a conexão foi estabelecida
print(cx)

# Criação de váriaveis para o usuário passar os dados do cliente
nome        = input("DIgite o nome do cliente:")
email       = input("Digite o email do cliente:")
telefone    = input("Digite o telefone do cliente:")

cursor = cx.cursor()
cursor.execute("insert into clientes(nome_cliente, email, telefone)values('"+nome+"','"+email+"','"+telefone+"')")
# Confirmar a insersão dos dados na tabela
print(cx.commit())


```

#### Arquivo de atualização: up_clientes.py

```python
import mysql.connector as mc
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)

cursor = cx.cursor()
cursor.execute("Select * from clientes")
for i in cursor:
    print(i)

print("O que você deseja atualizar, digite:")
print("1 - para Nome")
print("2 - para E-mail")
print("3 - para Telefone")
op = input("Digite a opção desejada: ")
id = input("Agora digite o id do cliente: ")
dado = input("Digite a nova informação: ")
if(op == "1"):
    cursor.execute("update clientes set nome_cliente='{}' where cliente_id='{}'".format(dado, id))
elif(op == "2"):
    cursor.execute("update clientes set email='{}' where cliente_id='{}'".format(dado, id))
elif(op == "3"):
    cursor.execute("update clientes set telefone='{}' where cliente_id='{}'".format(dado, id))
else:
    print("Opção inválida!")

cx.commit()




```


#### Criação do arquivo del_clientes.py

```python
import mysql.connector as mc

con = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
cursor = con.cursor()
cursor.execute("select * from clientes")
for c in cursor:
    print(c)

id = input("Digite o id do cliente que deseja apagar: ")
rs = input("Você realmente deseja apagar este cliente. Digite (s ou n):")
if(rs == "s" or rs =="S"):
    cursor.execute("delete from clientes where cliente_id={}".format(id))
    con.commit()
else:
    print("--------- Opção inválida ---------")



```