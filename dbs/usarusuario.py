import mysql.connector
from usuario import *

lista=[]
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="proyecto"
)

cursor=db.cursor()
numDocumento=int(input('Ingresa tu numero de documento: '))
nombre=input('Introduzca su nombre: ')
apellido=input('Introduce tu apellido: ')
genero=input('Introduce tu genero M o F: ')
correo=input('Introduce tu correo: ')

datos="INSERT INTO usuario (numDocumento,nombre,apellido,genero,correo) VALUES(%s,%s,%s,%s,%s) "
valores=(numDocumento,nombre,apellido,genero,correo)

cursor.execute(datos,valores)

cursor.execute("SELECT * FROM usuario")
registros=cursor.fetchall
print(registros)

db.commit()
#db.close()

for ap in cursor:
    ob=Usuario(ap[0],ap[1],ap[2],ap[3],ap[4])
    lista.append(ob)

for ap in lista:
    print(ap.getDocumento())
    print(ap.getNombre())
    print(ap.getApellido())
    print(ap.getGenero())
    print(ap.getCorreo())


