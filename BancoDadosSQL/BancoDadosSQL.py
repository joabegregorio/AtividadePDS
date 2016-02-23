import mysql.connector

cnn= mysql.connector.connect(user="root",password="katrina",host="localhost",
                     database="sys")
cur=cnn.cursor()


print("Digite a entrada : ")
nome= raw_input("Nome: ")
escola= raw_input("Escola: ")
idade= raw_input("Idade: ")

cur.execute("INSERT INTO nomes (nome, escola, idade) VALUES (%s, %s, %s)",
            (nome, escola, idade))

cnn.commit()

cur.execute("SELECT * FROM nomes")

data= cur.fetchall()

for x in data:
    print(x)
