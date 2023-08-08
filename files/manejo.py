import os

try: 
    stream=open('files/himno.txt','r', encoding='utf-8')
    cont=1
    linea=stream.readline()
    c=1
    while linea != "":
        print(f"{c} {linea}")
        linea=stream.readline()
        c+=1
except IOError as e:
    print(e,'. . .')
    
###

try:
    stream=open('files/himno.txt','r', encoding='utf-8')
    #print(stream.readlines())
    for linea in stream.readlines():
        print(linea)
except IOError as e:
    print(e,'. . .')       