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