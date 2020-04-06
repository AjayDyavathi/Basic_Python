import sqlite3
import datetime
import time
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')


conn = sqlite3.connect('test1.db')
c = conn.cursor()


##def graph_data():
##    c.execute('SELECT unix, value FROM stuffToPlot')
##    dates = []
##    values = []
##    for row in c.fetchall():
##        dates.append(datetime.datetime.fromtimestamp(row[0]))
##        values.append(row[1])
##        
##    plt.plot_date(dates, values, '-')
##    plt.show()


def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]
    
    c.execute('UPDATE stuffToPlot SET value = 77 WHERE value = 7')
    conn.commit()
    print('\n\n',70*'#','\n\n')

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    c.execute('DELETE FROM stuffToPlot WHERE value = 77')
    conn.commit()
    print('\n\n',70*'#','\n\n')

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]



del_and_update()
#graph_data()
