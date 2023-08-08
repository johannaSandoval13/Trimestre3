import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="proyecto"
)
cursor=db.cursor()
cursor.execute('SHOW DATABASES')
for dbs in cursor:
    print(dbs)
    
cursor.execute("SHOW TABLES")
print(cursor)
for dbs in cursor:
    print(dbs)
    
cursor.execute("SELECT * FROM usuario")
for ap in cursor:
    print(ap)