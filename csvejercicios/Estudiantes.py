class Estudiantes:
    def __init__(self,id, genero, puntaje, genE):
        self.__id=id
        self.__genero=genero
        self.__puntaje=puntaje
        self.__genE=genE
    def verDatos(self):
        return f"{self.__id} {self.__genero} {self.__puntaje} {self.__genE}"
    def getNombre(self):
        return self.__id