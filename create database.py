import sqlite3
conn=sqlite3.connect("m.db")
cursor=conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS ro(name TEXT,m INTEGER)''')
cursor.execute("INSERT INTO ro (name,m) VALUES ('adhi','1')")
    
cursor.execute("SELECT * FROM ro ")
rows = cursor.fetchall()
print(rows)
conn.commit()

import sqlite3
import io
import csv
d=open('C:\\ADITYA.G\\PYTHON FILES\\signup dbase.csv','w')
c=csv.writer(d)
connection=sqlite3.connect("m.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM ro")
co=[i[0]for i in cursor.description]
c.writerow(co)
data=cursor.fetchall()
for item in data:
    print(item)
    c.writerow(item)
d.close()

with open('C:\\ADITYA.G\\PYTHON FILES\\signup dbase.csv',"r",newline=None)as fd:
        r=csv.reader(fd)
        for line in fd:
            line=line.replace("\n","")
            print(line)
        cursor.close()
        connection.close()
        
