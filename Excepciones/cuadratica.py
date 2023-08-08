from math import *

print("Ingrese los valores para la formula, trate de que no sea 0:")
try:
 a=int(input("a="))
 b=int(input("b="))
 c=int(input("c="))
except ValueError:
    print("Ingrese los valores para la formula EN NUMEROS:")
    int(input("a="))
    int(input("b="))
    int(input("c="))

elevado1= b**2
resta1= -4*a*b
multi1= 2*a
suma1= elevado1 + multi1
try:
    raiz1= sqrt(suma1)
except ValueError:
    print("Lo siento, los valores ingresados no permiten el hacer una raiz")
try:
    positivo= -b + raiz1 / multi1
    negativo= -b - raiz1 / multi1
except ZeroDivisionError:
    print("lo siento, la division no puede ser ejecutada por 0, intente de nuevo")
    exit()
print ("Resultado con -: ",negativo)
print ("Resultado con +: ",positivo)