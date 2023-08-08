def añadeDatos():
    nombre=input("ingrese su nombre ")
    celular=input("ingrese su numero de celular ")
    correo=input("ingrese su correo ")
    edad=input("ingrese su edad ")
    nombreA=input("Ingrese un nombre para el archivo(al final escriba .txt) ")
    try:
        with open(nombreA,'w') as a:
            a.write(f"Nombre: {nombre}\n")
            a.write(f"Celular: {celular}\n")
            a.write(f"Edad: {edad}\n")
            a.write(f"Correo: {correo}\n")
        print("Se ha creado el archivo")
    except:
        print("ocurrio un error D':")
    
a1=(añadeDatos())