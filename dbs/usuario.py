class Usuario:
    def __init__(self,numeroDocumento,nombre,apellido,genero,correo):
        self.__numeroDocumento = numeroDocumento
        self.__nombre=nombre
        self.__apellido=apellido
        self.__genero=genero
        self.__correo=correo
        
    def verDatos(self):
        return f"{self.__numeroDocumento} {self.__nombre} {self.__apellido} {self.__genero} {self.__correo} "
    
    def getDocumento(self):
        return self.__numeroDocumento
    def getNombre(self):
        return self.__nombre
    def getApellido(self):
        return self.__apellido
    def getGenero(self):
        return self.__genero
    def getCorreo(self):
        return self.__correo