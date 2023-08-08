lista=["a","e","i","o","u"]
print(lista)
try:
    i=int(input("Ingrese el index que desea buscar: "))
    print(f"el index que pidio fue: ",lista[i])
except IndexError:
    print("parece que el indice esta fuera de rango (0 a 4), intente de nuevo!")
    i=int(input("Ingrese el index que desea buscar: "))
    print(f"el index que busco fue: ",lista[i])   


diccionario={"dog":"perro","cat":"gato","parrot":"loro","mouse":"raton"}
print(diccionario)
try:
    i=input("Ingrese la clave que desea buscar: ")
    print(f"la clave que pidio fue: ",diccionario[i])
except KeyError:
    print("parece que la clave es erronea, intente de nuevo!")
    i=input("Ingrese la clave que desea buscar: ")
    print(f"la clave que pidio fue: ",diccionario[i])