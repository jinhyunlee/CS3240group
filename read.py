__author__ = 'jl4vw'
#jinhyun lee
#jl4vw
#CS 3240

import csv
import sqlite3
database = 'lab3.db'

def write():
    cr = csv.reader(open("seas-courses-5years.csv","rU"))
    conn = sqlite3.connect(database)
    with conn:
        for row in cr:
            cur = conn.cursor()
            sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
            cur.execute(sql_cmd, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

def read():
    conn = sqlite3.connect(database)
    with conn:
        cur = conn.cursor()
        sql_cmd = "select * from coursedata"
        for row in cur.execute(sql_cmd):
            print row

if __name__ == '__main__':
    write()
    read()




