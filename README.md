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