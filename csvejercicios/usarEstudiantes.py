from Estudiantes import *
import csv
from statistics import median, mode
estudiantes=[]
with open('C:\\Jojo\\pythonsandoval\\csvejercicios\\Saber_11__2019-2.csv') as csvarchivo:
    csvReader=csv.reader(csvarchivo)
    for row in csvReader:
        print(row[6],row[3],row[-7],row[-1])
        break

def sumacsv(ruta):
    columna7 = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna7 = row[-7]
                if valor_columna7.isdigit():
                    columna7.append(int(valor_columna7))
    suma7 = sum(columna7)
    return suma7

def mayorcsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna = row[-7]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return max(lista)

def menorcsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna = row[-7]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return min(lista)

def promediocsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna = row[-7]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return sum(lista) / len(lista)

def parescsv(ruta):
    pares = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna = row[-7]
                if valor_columna.isdigit():
                    numero = int(valor_columna)
                    if numero % 2 == 0:
                        pares.append(numero)
    return pares

def imparescsv(ruta):
    impares = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna = row[-7]
                if valor_columna.isdigit():
                    numero = int(valor_columna)
                    if numero % 2 != 0:
                        impares.append(numero)
    return impares

def mediacsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna = row[-7]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return sum(lista) / len(lista)

def modacsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        next(csvReader)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna = row[-7]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return mode(lista)

def medianacsv(ruta):
    lista = []
    with open(ruta) as csvarchivo:
        csvReader = csv.reader(csvarchivo)
        for row in csvReader:
            if len(row) >= 8:
                valor_columna = row[-7]
                if valor_columna.isdigit():
                    lista.append(int(valor_columna))
    return median(lista)
ruta = 'C:\\Jojo\\pythonsandoval\\csvejercicios\\Saber_11__2019-2.csv'
resultadoSuma = sumacsv(ruta)
print(".suma de los valores en la columna Resultado ICFES:", resultadoSuma)

mayorValor = mayorcsv(ruta)
print(".mayor valor en la columna Resultado ICFES:", mayorValor)

menorValor = menorcsv(ruta)
print(".menor valor en la columna Resultado ICFES:", menorValor)

promedio = promediocsv(ruta)
print(".promedio de los valores en la columna Resultado ICFES:", promedio)

numeros_pares = parescsv(ruta)
print(".pares en la columna Resultado ICFES:", numeros_pares)

numeros_impares = imparescsv(ruta)
print(".impares en la columna Resultado ICFES:", numeros_impares)

media = mediacsv(ruta)
print(".media de la columna Resultado ICFES:", media)

mediana= medianacsv(ruta)
print(".mediana de la columna Resultados ICFES:",mediana)

moda= modacsv(ruta)
print(".moda de la columna Resultados ICFES:", moda)

def resultadostxt():
    resultadoS=resultadoSuma
    resultadoM=mayorValor
    resultadom=menorValor
    resultadoP=promedio
    resultadoPar=numeros_pares
    resultadoIm=numeros_impares
    resultadomedia=media
    resultadomediana=mediana
    resultadomoda=moda

    with open('C:\\Jojo\\pythonsandoval\\csvejercicios\\resultados.txt','w') as n:
        n.write(f".suma de los valores en la columna Resultado ICFES:{resultadoS}\n")
        n.write(f".mayor valor en la columna Resultado ICFES:{resultadoM}\n")
        n.write(f".menor valor en la columna Resultado ICFES:{resultadom}\n")
        n.write(f".promedio de los valores en la columna Resultado ICFES:{resultadoP}\n")
        n.write(f".pares en la columna Resultado ICFES:{resultadoPar}\n")
        n.write(f".impares en la columna Resultado ICFES:{resultadoIm}\n")
        n.write(f".media de la columna Resultado ICFES:{resultadomedia}\n")
        n.write(f".mediana de la columna Resultado ICFES:{resultadomediana}\n")
        n.write(f".moda de la columna Resultado ICFES:{resultadomoda}\n")

a1=(resultadostxt())