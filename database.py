from UI import *
app = ClassUI()

import sqlite3  as sql 

class DBHash():         
    database  = "DBHash.db"  
    conn  = None
    cur   = None    
    connected = False

    def connect(self):
        DBHash.conn = sql.connect(DBHash.database) 
        DBHash.cur  = DBHash.conn.cursor()        
        DBHash.connected = True                           
    def disconnect(self):
        DBHash.conn.close()   
        DBHash.connected = False   

    def execute(self, sql, parms = None):
        if DBHash.connected:
            if parms == None: 
                DBHash.cur.execute(sql) 
            else:                         
                DBHash.cur.execute(sql,parms)   
            return True           
        return False 

    def fetchall(self):
        return DBHash.cur.fetchall() 

    def persist(self):
        if DBHash.connected:       
            DBHash.conn.commit()  
            return True                         
        return False           


def initDB():
    trans = DBHash()        
    trans.connect()
    trans.execute("""CREATE TABLE IF NOT EXISTS Hashs(
                    ID INTEGER PRIMARY KEY, 
                    Original TEXT, 
                    Hash TEXT,
                    Uso TEXT)""")
    trans.persist() 
    trans.disconnect() 
initDB()

def viewAll():
    trans = DBHash()                    
    trans.connect()
    trans.execute("SELECT * FROM Hashs ORDER BY ID")
    rows = trans.fetchall()
    trans.persist()
    trans.disconnect()
    return rows
def Process(TipeOfProcess,Original,Uso):
    # Vai fazer todo o processo de criação, procura, atualização e exclusão do banco de dados
    import hashlib
    trans = DBHash()                    
    trans.connect()

    if TipeOfProcess == "Search" :
        trans.execute("SELECT * FROM Hashs WHERE Original=? OR Uso=? ",(Original,Uso))
        rows = trans.fetchall()             
        trans.disconnect()                         
        return rows

    elif TipeOfProcess == "Insert" or TipeOfProcess == "Delete":
        if TipeOfProcess == "Insert":
            m = hashlib.md5()
            m.update(Original.encode())
            trans.execute("INSERT INTO Hashs VALUES(NULL,?,?,?)",(Original,str(m.hexdigest()),Uso))
            trans.persist()             
            trans.disconnect()
            
        elif TipeOfProcess == "Delete":
            m = hashlib.md5()
            m.update(Original.encode())
            trans.execute("DELETE FROM Hashs WHERE Hash=? and Original=?",(str(m.hexdigest()),Original))
            trans.persist()             
            trans.disconnect()

        