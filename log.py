import time

class Log:

    listaDeLogs = []

    def __init__(self, id, id_da_os, comentario) -> None:
        self.__id = id
        self.__os = id_da_os
        self.__comentario = comentario
        self.__timestamp = time.time()

########### GETTERS E SETTERS #############
    @property
    def id(self):
        return self.__id
    @property
    def os(self):
        return self.__os
    @property
    def comentario(self):
        return self.__comentario    
    @property
    def timestamp(self):
        savedTime = time.localtime(self.__timestamp)
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", savedTime)
        return time_string
    @id.setter
    def id(self, id):
        self.__id = id
    @os.setter
    def os(self, os):
        self.__os = os
    @comentario.setter
    def comentario(self, comentario):
        self.__comentario = comentario
###########################################

# Outros Métodos

    def __str__(self):
        return f"{self.timestamp}\n{self.comentario}"