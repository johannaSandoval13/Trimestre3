import mysql.connector
from usuario import *

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="adso30"
)

cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuario (
        numDocumento INT PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(50),
        genero ENUM('M', 'F'),
        correo VARCHAR(100) UNIQUE
    )
''')
cursor.execute('ALTER TABLE usuario ADD COLUMN fecha_registro DATE')
cursor.execute('ALTER TABLE usuario DROP COLUMN fecha_registro')
cursor.execute('ALTER TABLE usuario DROP COLUMN fecha_registro')
cursor.execute('ALTER TABLE usuario CHANGE COLUMN apellido apellidos VARCHAR(50)')
cursor.execute('ALTER TABLE usuario MODIFY COLUMN numDocumento BIGINT')


numDocumento = int(input('Número de documento: '))
nombre = input('Nombre: ')
apellido = input('Apellido: ')
genero = input('Género (M o F): ')
correo = input('Correo: ')


datos = "INSERT INTO usuario (numDocumento, nombre, apellidos, genero, correo) VALUES ('" + numDocumento + "', '" + nombre + "', '" + apellido + "', '" + genero + "', '" + correo + "')"
valores = (numDocumento, nombre, apellido, genero, correo)
cursor.execute(datos, valores)
db.commit()


cursor.close()
db.close()
