from UI import *
from database import *
import database as DB

app = None                  
app = ClassUI()            

def insertCommand():                                                                                      
    DB.Process("Insert",app.txtOriginal.get(), app.txtUso.get())
    viewCommand()

def viewCommand():                                    
    rows = DB.viewAll()  
    try:                
        for row in app.listPasswords.get_children(): app.listPasswords.delete(row)                    
        for row in rows: app.listPasswords.insert("",wd.END,values=row)  
    except: print("Não deu certo")

def searchCommand():                                                                                            
    rows = DB.Process("Search",app.txtOriginal.get(),app.txtUso.get())                
    for row in app.listPasswords.get_children(): app.listPasswords.delete(row)  
    for row in rows: app.listPasswords.insert("",wd.END,values=row)         

def deleteCommand():                                
    DB.Process("Delete",app.txtOriginal.get(),app.txtUso.get())
    viewCommand()

def selected_item(event):                              
    GET = app.listPasswords.item(app.listPasswords.selection())               
    item = app.listPasswords.selection()[0]                                  
    app.entNome.delete(0,wd.END)                                         
    app.entNome.insert(wd.END, app.listPasswords.item(item)['values'][1]) 
    app.entHash.delete(0,wd.END)                                           
    app.entHash.insert(wd.END, app.listPasswords.item(item)['values'][2])   
    app.entUso.delete(0, wd.END)                                        
    app.entUso.insert(wd.END, app.listPasswords.item(item)['values'][3])  

app.btnCreate.configure(command=insertCommand)                
app.btnView.configure(command=viewCommand)              
app.btnSearch.configure(command=searchCommand) 
app.btnDelete.configure(command=deleteCommand)                            
app.listPasswords.bind('<<TreeviewSelect>>', selected_item)  


import keyboard                   
import string                        
from threading import *           
teclas = list(string.ascii_lowercase) 
teclas.append("Delete")      
teclas.append('Shift')      
def listen(tecla):            
    while True:                      
        keyboard.wait(tecla)          
        if tecla=='Delete':        
            deleteCommand()  
        elif tecla=='Shift':        
            viewCommand() 
threads = [Thread(target=listen, kwargs={"tecla":tecla}) for tecla in teclas]
for thread in threads:            
    thread.start()    

viewCommand()
ClassUI.runEST()