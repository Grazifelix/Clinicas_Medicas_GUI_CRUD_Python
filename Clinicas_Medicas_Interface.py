#from tkinter import *

import mysql.connector
db_connection = mysql.connector.connect(host='127.0.0.1', user='root', password='Choich@n2208', database='clinicas_medicas')
cursor = db_connection.cursor()
#sql = "INSERT INTO medico (CodMed, NomeMed, Genero, Telefone, Email, CodEspec) VALUES (%s, %s, %s, %s, %s, %s)"
#values = (3063, "Maria Teresa", 'F', '93652165894', 'mariateresa@gmail.com', 3)
#cursor.execute(sql, values)
#print(cursor.rowcount, "record inserted.")

sql = "DELETE FROM medico WHERE CodMed=3063"
cursor.execute(sql)


print(cursor.rowcount, "record Deleted")
print("\n")

cursor.close()
db_connection.commit()
db_connection.close()