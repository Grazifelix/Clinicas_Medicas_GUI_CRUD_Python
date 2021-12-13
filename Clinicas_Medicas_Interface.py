from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysqlcn

# Função inserir
def inserir():
    CodCli = e_codcli.get()
    NomeCli = e_NomeCli.get()
    Endereco = e_Endereco.get()
    Telefone = e_Telefone.get()
    Email = e_Email.get()
    if (CodCli == '' or NomeCli == "" or Endereco == '' or Telefone == "" or Email == ""):
        MessageBox.showinfo("Insert Status", "Insira todas as informações para poder enviar.")
    else:
        db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208',
                                        database='clinicas_medicas')
        cursor = db_connection.cursor()
        sql = 'insert into CLINICA (CodCli, NomeCli, Endereco, Telefone, Email) VALUES (%s, %s, %s, %s, %s)'
        values = (CodCli, NomeCli, Endereco,  Telefone, Email)
        cursor.execute(sql, values)
        db_connection.commit()
        #limpando inputs
        show()
        e_codcli.delete(0, 'end')
        e_NomeCli.delete(0, 'end')
        e_Endereco.delete(0, 'end')
        e_Telefone.delete(0, 'end')
        e_Email.delete(0, 'end')

        MessageBox.showinfo("Insert Status", "Dados Inseridos")
        cursor.close()
        db_connection.close()

#Função Deletar
def delete():
    if (e_codcli.get()==""):
        MessageBox.showinfo("Delete Status", "Adicione o codigo para clinica para excluir")
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
        show()
        MessageBox.showinfo(cursor.rowcount, "Excluido com sucesso")
        cursor.close()
        db_connection.commit()
        db_connection.close()

#Função atualizar
def atualizar():
    CodCli = e_codcli.get()
    NomeCli = e_NomeCli.get()
    Endereco = e_Endereco.get()
    Telefone = e_Telefone.get()
    Email = e_Email.get()
    if (CodCli == '' or NomeCli == "" or Endereco == '' or Telefone == "" or Email == ""):
        MessageBox.showinfo("Update Status", "Insira todas as informações para poder atualizar")
    else:
        db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208',
                                        database='clinicas_medicas')
        cursor = db_connection.cursor()
        cursor.execute("UPDATE clinica SET NomeCli='"+ NomeCli +"', Endereco='"+Endereco+"', Telefone='"+Telefone+"', Email='"+Email+"' where CodCli='" + CodCli + "'")
        cursor.execute("commit")

        #limpando inputs
        e_codcli.delete(0, 'end')
        e_NomeCli.delete(0, 'end')
        e_Endereco.delete(0, 'end')
        e_Telefone.delete(0, 'end')
        e_Email.delete(0, 'end')
        show()
        MessageBox.showinfo(cursor.rowcount, "Atualizado com sucesso")
        cursor.close()
        db_connection.commit()
        db_connection.close()

# Função limpar inputs
def limparGet():
    e_codcli.delete(0, 'end')
    e_NomeCli.delete(0, 'end')
    e_Endereco.delete(0, 'end')
    e_Telefone.delete(0, 'end')
    e_Email.delete(0, 'end')

#Função Obter dados
def get():
    if (e_codcli.get()==""):
        MessageBox.showinfo("Get Status", "Adicione o codigo para clinica para excluir")
    else:
        db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208', database='clinicas_medicas')
        cursor = db_connection.cursor()
        cursor.execute("SELECT * FROM clinica WHERE CodCli='" + e_codcli.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e_NomeCli.insert(0, row[1])
            e_Endereco.insert(0, row[2])
            e_Telefone.insert(0, row[3])
            e_Email.insert(0, row[4])

        cursor.close()
        db_connection.commit()
        db_connection.close()

# função listar clinicas
def show():
    db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208', database='clinicas_medicas')
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM clinica")
    rows = cursor.fetchall()
    lista.delete(0, lista.size())

    for row in rows:
        insertData = str(row[0]) + ' | '+ row[1]+' | '+row[2]+' | '+row[3]+' | '+row[4] + '\n'
        lista.insert(lista.size()+1, insertData)

#Função listar medicos
def showMedico():
    db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208', database='clinicas_medicas')
    cursor = db_connection.cursor()
    cursor.execute("SELECT medico.*, CargaHorariaSemanal FROM medico inner join clinica_medico on clinica_medico.CodMed = medico.CodMed;")
    rows = cursor.fetchall()
    lista.delete(0, lista.size())

    for row in rows:
        insertData = str(row[0]) + ' | ' + row[1] + ' | ' + row[2] + ' | ' + str(row[3]) + ' | ' + row[4] + ' | ' + str(row[5]) + ' | ' +str(row[6])
        lista.insert(lista.size() + 1, insertData)

#Funções de exemplo: Agregação e agrupamento
def groupBy():
    db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208', database='clinicas_medicas')
    cursor = db_connection.cursor()
    cursor.execute(
        "SELECT distinct C.NomeCli as Nome_clinica, count(CM.CodMed) as Num_medico FROM clinicas_medicas.clinica as C, clinicas_medicas.clinica_medico as CM WHERE C.CodCli = CM.CodCli GROUP BY CM.CodCli;")
    rows = cursor.fetchall()
    lista.delete(0, lista.size())

    for row in rows:
        insertData = str(row[0]) + ' | ' + str(row[1])
        lista.insert(lista.size() + 1, insertData)

def AgregationFunction():
    db_connection = mysqlcn.connect(host='127.0.0.1', user='root', password='Choich@n2208', database='clinicas_medicas')
    cursor = db_connection.cursor()
    cursor.execute(
        "select  E.CodEspec, E.NomeEspec, count(*) as Num_Medicos from especialidade as E left join medico as M on E.CodEspec = M.CodEspec group by E.CodEspec having count(*) > 1;")
    rows = cursor.fetchall()
    lista.delete(0, lista.size())

    for row in rows:
        insertData = str(row[0]) + ' | ' + str(row[1]) + ' | ' + str(row[2])
        lista.insert(lista.size() + 1, insertData)

#INDEXSCREEN
index = Tk()
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
deleteButton.grid(column=2, row=7, padx=10, pady=10)

getButton = Button(index, text='Obter Dados', font=('italic', 10), bg='white', command=get)
getButton.place(x=50, y=20)
getButton.grid(column=3, row=7, padx=10, pady=10)

limparButton = Button(index, text='Limpar Dados', font=('italic', 10), bg='white', command=limparGet)
limparButton.place(x=50, y=20)
limparButton.grid(column=2, row=8, padx=10, pady=10)

#LISTAGEM LATERAL
scrollbar = Scrollbar(index, orient="vertical")
lista = Listbox(index, width=80, height=20, yscrollcommand=scrollbar.set)
scrollbar.config(command=lista.yview)

lista.grid_rowconfigure(0, weight=1)
lista.grid_columnconfigure(0, weight=1)
scrollbar.grid(row=0, column=5, sticky="ns")
lista.grid(row=0, column=4, sticky="nsew")
#lista.grid(column=4, row=0, padx=10, pady=10)
show()

#BUTOES EXTRAS (para fins de demostração)
#CLINICA
clinicaButton = Button(index, text='Clinica', font=('italic', 10), bg='white', command=show)
clinicaButton.place(x=50, y=20)
clinicaButton.grid(column=4, row=1, padx=10, pady=10)

#MEDICO
medicoButton = Button(index, text='Medico', font=('italic', 10), bg='white', command=showMedico)
medicoButton.place(x=50, y=20)
medicoButton.grid(column=4, row=2, padx=10, pady=10)

#QTD_MEDICOS-CLINICA
QTDmedicoButton = Button(index, text='GroupBy', font=('italic', 10), bg='white', command=groupBy)
QTDmedicoButton.place(x=50, y=20)
QTDmedicoButton.grid(column=4, row=3, padx=10, pady=10)

#Agregar
agregarButton = Button(index, text='Agregar', font=('italic', 10), bg='white', command=AgregationFunction)
agregarButton.place(x=50, y=20)
agregarButton.grid(column=4, row=4, padx=10, pady=10)

index.mainloop()




