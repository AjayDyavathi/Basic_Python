import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS PersonalData(Name TEXT, Age REAL, Height REAL, DOB TEXT)')

def data_entry():
    c.execute("INSERT INTO PersonalData VALUES('Laxman', 20, 5.11, '03-09-1998')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
              
