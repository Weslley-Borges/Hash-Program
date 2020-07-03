import operator           
from tkinter import ttk
from tkinter import Menu
import tkinter as wd
from tkinter import *

class ClassUI():         
    #Configurações gerais
    wd= Tk()      
    wd.title('Hashing program')  
    #Frames
    frameExterno = Frame(wd, width=1400, height=1400, bg='SteelBlue1')
    frameExterno.pack()
    frameExterno.place(x=0,y=0)
    frameList = Frame(wd, width=610, height=355, bg="Gray")
    frameList.pack()
    frameList.place(x=10, y=220)
    frameForm = Frame(wd, width=610, height=200, bg="Gray")
    frameForm.pack()
    frameForm.place(x=10, y=10)

    #Variáveis de entrada
    txtOriginal = StringVar()      
    txtHash = StringVar() 
    txtUso = StringVar()
   
    #Componentes da janela
    lblNome = Label(frameForm, text="Digite uma senha",bg="Gray",fg="White",font=("Courier sans-serif",16))
    lblNome.pack()
    lblNome.place(x=10,y=10)
    entNome = Entry(frameForm, textvariable=txtOriginal,width=80)
    entNome.pack()
    entNome.place(x=10,y=40)

    lblHash = Label(frameForm, text="Hash",bg="Gray",fg="White",font=("Courier sans-serif",13))
    lblHash.pack()
    lblHash.place(x=10,y=60)
    entHash = Entry(frameForm, textvariable=txtHash,width=80)
    entHash.pack()
    entHash.place(x=10,y=80)

    lblUso = Label(frameForm, text="Onde será usada",bg="Gray",fg="White",font=("Courier sans-serif",13))
    lblUso.pack()
    lblUso.place(x=10,y=100)
    entUso = Entry(frameForm, textvariable=txtUso,width=80)
    entUso.pack()
    entUso.place(x=10,y=120)

    btnCreate = Button(frameForm, text="Criar")
    btnCreate.pack()
    btnCreate.place(x=10,y=170)
    btnView = Button(frameForm, text="Ver todos")
    btnView.pack()
    btnView.place(x=50,y=170)
    btnSearch = Button(frameForm, text="Procurar")
    btnSearch.pack()
    btnSearch.place(x=115,y=170)
    btnDelete = Button(frameForm, text="Deletar")
    btnDelete.pack()
    btnDelete.place(x=176,y=170)

    #Cria uma lista e as suas configurações
    listPasswords= ttk.Treeview(frameList, column=("column1", "column2", "column3","column4"), show='headings',height=16)
    listPasswords.heading("#1", text="ID")
    listPasswords.heading("#2", text="Original")
    listPasswords.heading("#3", text="Hash")
    listPasswords.heading("#4", text="Uso")
    listPasswords.column('#1', width=40)
    listPasswords.column('#2', width=180)
    listPasswords.column('#3', width=180)
    listPasswords.column('#4', width=180)
    scrollPasswords = Scrollbar(frameList)
    #Associando a Scrollbar com a Listbox...
    listPasswords.configure(yscrollcommand=scrollPasswords.set)   
    scrollPasswords.configure(command=listPasswords.yview)       
    
    listPasswords.pack()
    listPasswords.place(x=5,y=5)
    scrollPasswords.pack()
    scrollPasswords.place(x=585,y=6,height=345)

    #Organiza os widgets na janela de acordo com a classe do widget ( para organizar a casa )
    wd.geometry("630x590")
    wd.resizable(width=False,height=False)
    def runEST():
        wd.mainloop() 

