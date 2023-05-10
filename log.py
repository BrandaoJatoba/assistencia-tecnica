import time

class Log:
    def __init__(self, id, os, comentario) -> None:
        self.__id = id
        self.__timestamp = time.localtime
        self.__os = os
        self.__comentario = comentario
        pass

    @property
    def id(self):
        return self.__id

    @property
    def timestamp(self):
        return self.__timestamp

    @property
    def os(self):
        return self.__os

    @property
    def comentario(self):
        return self.__comentario
    
    @id.setter
    def id(self, id):
        self.__id = id
        pass

    @os.setter
    def os(self, os):
        self.__os = os

    @comentario.setter
    def comentario(self, comentario):
        self.__comentario = comentario