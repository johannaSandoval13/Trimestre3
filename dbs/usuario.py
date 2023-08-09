class Usuario:
    def __init__(self,numeroDocumento,nombre,apellidos,genero,correo):
        self.__numeroDocumento = numeroDocumento
        self.__nombre=nombre
        self.__apellidos=apellidos
        self.__genero=genero
        self.__correo=correo
        
    def verDatos(self):
        return f"{self.__numeroDocumento} {self.__nombre} {self.__apellidos} {self.__genero} {self.__correo} "
    
    def getDocumento(self):
        return self.__numeroDocumento
    def getNombre(self):
        return self.__nombre
    def getApellidos(self):
        return self.__apellidos
    def getGenero(self):
        return self.__genero
    def getCorreo(self):
        return self.__correo