import sqlite3
import fire
import pandas as pd

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS contact_info(ID INTEGER PRIMARY KEY AUTOINCREMENT, Name Text, Number Text , Tag Text)')
conn.commit()

def addcontact(name,number,tag):

    params = (name,number,tag)

    cursor.execute("INSERT INTO contact_info(Name,Number,Tag) VALUES (? , ? , ?)",params)

    conn.commit()
    conn.close()

def listcontacts():
    cursor.execute('SELECT * FROM contact_info')
    LC = cursor.fetchall()
    for i in LC :
        print(i)

def AddCsv():
    cursor.execute('SELECT * FROM contact_info')
    LC = cursor.fetchall()
    L1=[]
    L2=[]
    L3=[]
    for i in LC:
        L1.append(i[1])
        L2.append(i[2])
        L3.append(i[3])

    df = pd.DataFrame({  
    "Name": L1,
    "number": L2,
    "tag": L3
    })
    df.to_csv("Contacts.csv")



if __name__ == '__main__':
    fire.Fire()