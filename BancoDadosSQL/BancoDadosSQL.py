import mysql.connector

cnn= mysql.connector.connect(user="root",password="katrina",host="localhost",
                     database="sys")
cur=cnn.cursor()

print("Escolha a operacao : ")
print("1 - Ler : ")
print("2 - Escrever : ")

op= input()

if op == 1:
    cur.execute("SELECT * FROM nomes")
    data= cur.fetchall()
    for x in data:
        print(x)

if op == 2: 
    nome= raw_input("Nome: ")
    escola= raw_input("Escola: ")
    idade= raw_input("Idade: ")
    cur.execute("INSERT INTO nomes (nome, escola, idade) VALUES (%s, %s, %s)",
                (nome, escola, idade))
    cnn.commit()
