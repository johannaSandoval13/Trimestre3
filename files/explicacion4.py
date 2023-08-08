from os import strerror
#se importa la funcion 'sterror' del modulo 'os', eso se usa para obtener mensajes de error 
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
#Aqui comienza el diccionario 'counters' en el que se van a almacenar las letras del abecedario ordenadas
file_name = input("Ingresa el nombre del archivo a analizar: ")
#se pide al usuario que ingrese el nombre del archivo que desea analizar
try:
    file = open(file_name, "rt")
#En este bloque try se intenta abrir el archivo que se indico arriba, si ocurre un error, se saltara al except
    for line in file:
#este for va a recorrer cada linea del archivo indicado
        for char in line:
#el programa va a recorrer cada caracter del archivo 
            if char.isalpha():
#el programa va a identificar si el caracter de la linea son letras 
                counters[char.lower()] += 1
#va a convertir las letras en minusculas con el metodo lower, y las añadira al contador

    file.close()
#el metodo close cerrara el archivo
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
#este bucle recorrera lo almacenado en el diccionario 'counters' y se imprimira la letra y el numero de veces que aparecio en el archivo
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
#para cerrar el try de la linea 7, esta este except, el cual gracias a la funcion sterror de la linea 1 dara una descripcion mas facil de entender de el error ocurrido 
