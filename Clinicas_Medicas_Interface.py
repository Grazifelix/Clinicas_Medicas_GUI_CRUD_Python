from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysqlcn

def inserir():
    CodCli = e_codcli.get()
    NomeCli = e_NomeCli.get()
    Endereco = e_Endereco.get()
    Telefone = e_Telefone.get()
    Email = e_Email.get()
    if (CodCli == '' or NomeCli == "" or Endereco == '' or Telefone == "" or Email == ""):
        MessageBox.showinfo("Insira todas as informações para poder enviar.")
    else:
        db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208',
                                        database='clinicas_medicas')
        cursor = db_connection.cursor()
        sql = 'insert into CLINICA (CodCli, NomeCli, Endereco, Telefone, Email) VALUES (%s, %s, %s, %s, %s)'
        values = (CodCli, NomeCli, Endereco,  Telefone, Email)
        cursor.execute(sql, values)

        #limpando inputs
        e_codcli.delete(0, 'end')
        e_NomeCli.delete(0, 'end')
        e_Endereco.delete(0, 'end')
        e_Telefone.delete(0, 'end')
        e_Email.delete(0, 'end')

        MessageBox.showinfo(cursor.rowcount, "record inserted.")
        cursor.close()
        db_connection.commit()
        db_connection.close()

def delete():
    if (e_codcli.get()==""):
        MessageBox.showinfo("Adicione o codigo para clinica para excluir")
    else:
        db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208', database='clinicas_medicas')
        cursor = db_connection.cursor()
        cursor.execute("DELETE FROM clinica WHERE CodCli='"+e_codcli.get()+"'")
        cursor.execute("commit")
        e_codcli.delete(0, 'end')
        e_NomeCli.delete(0, 'end')
        e_Endereco.delete(0, 'end')
        e_Telefone.delete(0, 'end')
        e_Email.delete(0, 'end')

        MessageBox.showinfo(cursor.rowcount, "Delete Sucessfully.")
        cursor.close()
        db_connection.commit()
        db_connection.close()



#INDEXSCREEN
index = Tk()
index.geometry('500x600')
index['bg'] = '#4ED28E'
index.title("Clinicas Medicas")

#LABELS
CodCli = Label(index, text='Insira o Codigo:', font=('bold', 12), fg='white', bg='#4ED28E')
CodCli.place(x=50, y=20)
CodCli.grid(column=2, row=0, padx=10, pady=10)

NomeCli = Label(index, text='Insira o Nome:', font=('bold', 12), fg='white', bg='#4ED28E')
NomeCli.place(x=50, y=20)
NomeCli.grid(column=2, row=1, padx=10, pady=10)

Endereco = Label(index, text='Insira o Endereco:', font=('bold', 12), fg='white', bg='#4ED28E')
Endereco.place(x=50, y=20)
Endereco.grid(column=2, row=2, padx=10, pady=10)

Telefone = Label(index, text='Insira o Telefone:', font=('bold', 12), fg='white', bg='#4ED28E')
Telefone.place(x=50, y=20)
Telefone.grid(column=2, row=3, padx=10, pady=10)

Email = Label(index, text='Insira o Email:', font=('bold', 12), fg='white', bg='#4ED28E')
Email.place(x=50, y=20)
Email.grid(column=2, row=4, padx=10, pady=10)

#INPUTS
e_codcli = Entry()
e_codcli.place(x=200, y=50)
e_codcli.grid(column=3, row=0, padx=10, pady=10)

e_NomeCli = Entry()
e_NomeCli.place(x=200, y=50)
e_NomeCli.grid(column=3, row=1, padx=10, pady=10)

e_Endereco = Entry()
e_Endereco.place(x=200, y=50)
e_Endereco.grid(column=3, row=2, padx=10, pady=10)

e_Telefone = Entry()
e_Telefone.place(x=200, y=50)
e_Telefone.grid(column=3, row=3, padx=10, pady=10)

e_Email = Entry()
e_Email.place(x=200, y=50)
e_Email.grid(column=3, row=4, padx=10, pady=10)

#botão
inserirButton = Button(index, text='Inserir', font=('italic', 10), bg='white', command=inserir)
inserirButton.place(x=50, y=20)
inserirButton.grid(column=2, row=6, padx=10, pady=10)

visualizarButton = Button(index, text='Atualizar', font=('italic', 10), bg='white', command=atualizar)
visualizarButton.place(x=50, y=20)
visualizarButton.grid(column=3, row=6, padx=10, pady=10)

deleteButton = Button(index, text='Deletar', font=('italic', 10), bg='white', command=delete)
deleteButton.place(x=50, y=20)
deleteButton.grid(column=4, row=6, padx=10, pady=10)

index.mainloop()


#INSERT
#sql = "INSERT INTO medico (CodMed, NomeMed, Genero, Telefone, Email, CodEspec) VALUES (%s, %s, %s, %s, %s, %s)"
#values = (3063, "Maria Teresa", 'F', '93652165894', 'mariateresa@gmail.com', 3)
#cursor.execute(sql, values)
#print(cursor.rowcount, "record inserted.")

#DELETE
#sql = "DELETE FROM medico WHERE CodMed=3063"
#cursor.execute(sql)
#print(cursor.rowcount, "record Deleted")
#print("\n")
#cursor.close()
#db_connection.commit()
#db_connection.close()

#SELECT
#sql = "SELECT NomeMed FROM clinicas_medicas.medico join clinica_medico on medico.CodMed = clinica_medico.CodMed where CodEspec = 4 and clinica_medico.CargaHorariaSemanal > 20";
#cursor.execute(sql)
#for (NomeMed) in cursor:
  #print(NomeMed)