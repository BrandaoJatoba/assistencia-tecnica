class Log:
    def __init__(self, id, data, os, comentario) -> None:
        self.__id = id
        self.__data = data
        self.__os = os
        self.__comentario = comentario
        pass

    @property
    def id(self):
        return self.__id

    @property
    def data(self):
        return self.__data

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

    @data.setter
    def data(self, data):
        self.__data = data
        pass

    @os.setter
    def os(self, os):
        self.__os = os

    @comentario.setter
    def comentario(self, comentario):
        self.__comentario = comentario
