def nuevoA(nuevo_nombre):
    try:
        with open(nuevo_nombre,'r') as yaExiste: 
            lineas= yaExiste.readlines()
            numLineas= len(lineas)
            print(nuevo_nombre,'ya esta en la carpeta y su cantidad de lineas es:',numLineas)
    except:
        with open(nuevo_nombre,'w') as nuevoA:
            print("se creo el archivo",nuevoA)
            

nuevo_nombre= input("ingrese el nombre de archivo ")
nuevoA(nuevo_nombre)
    

a1 =(nuevoA(nuevo_nombre))
print(a1)