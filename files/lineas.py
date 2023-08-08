import os

try: 
    stream=open('files/himno.txt','r', encoding='utf-8')
    lineas=stream.readline()
    stream1=open('files/resultado.txt','w', encoding='utf-8')
    for numero, linea in enumerate(lineas, 1):
        cantidad=sum(1 for character in linea if character.isalpha)
        resultado=f"linea{numero}:{cantidad}letras"
        stream1.write(resultado)
        
except IOError as e:
    print(e,'. . .')



