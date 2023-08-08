##Lectura
import csv
archivo_csv = "datos.csv"
with open(archivo_csv, "r") as file:
    lector_csv = csv.reader(file)
    encabezados = next(lector_csv) 

    for fila in lector_csv:
        nombre, edad, email = fila
        print(f"Nombre: {nombre}, Edad: {edad}, Email: {email}")

