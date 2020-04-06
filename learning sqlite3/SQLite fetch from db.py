import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('test1.db')
c = conn.cursor()


##def create_table():
##    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, Keyword TEXT, value REAL)')
##
##def data_entry():
##    c.execute("INSERT INTO stuffToPlot VALUES(176782389, '29-08-2018', 'Python', 7)")
##    conn.commit()
##    c.close()
##    conn.close()
##
##
##
##def dynamic_data_entry():
##    unix = time.time()
##    datestamp = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
##    Keyword = 'Ajay'
##    value = random.randrange(0,10)
##    c.execute("INSERT INTO stuffToPlot (unix, datestamp, Keyword, value) VALUES (?, ?, ?, ?)",
##              (unix, datestamp, Keyword, value))
##    conn.commit()
##    


def read_from_db():
    #c.execute('SELECT *FROM stuffToPlot')
    #c.execute("SELECT *FROM stuffToPlot WHERE value > 3 AND Keyword = 'Ajay'")
    c.execute('SELECT unix, value FROM stuffToPlot')
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)
        #print(row[0])
    
read_from_db()

#$create_table()

#for x in range(10):
#    dynamic_data_entry()
#    time.sleep(1)


c.close()
conn.close()
