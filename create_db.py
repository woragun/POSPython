import sqlite3
def createDatabase():
    con = sqlite3.connect(database=r'FMS.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS worker(id INTEGER PRIMARY KEY AUTOINCREMENT,name text,gender text,contact text,nationality text,wage text)")
    con.commit()
    
createDatabase()