import sqlite3

connection=sqlite3.connect(r'C:\Users\Administrator\Documents\UST Training\Python-Training\SQL_Learning\Chinook_Sqlite.sqlite')
cursor=connection.cursor()

print(cursor)

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

tables=cursor.fetchall()
for table in tables:
    print(table)