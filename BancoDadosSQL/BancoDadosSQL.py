import mysql.connector

cnn=mysql.connector.connect(user="main",password="123",host="localhost",database="sys")

cur=cnn.cursor()

cur.execute("SELECT * FROM nomes")

data= cur.fetchall()

for x in data :
    print(x)
