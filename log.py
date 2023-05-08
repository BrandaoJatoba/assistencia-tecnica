import datetime as dt

class Log:
    def __init__(self, id, timestamp:dt.datetime, os, comentario) -> None:
        self.__id = id
        self.__timestamp = timestamp
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

    @timestamp.setter
    def timestamp(self, timestamp:dt.datetime):
        self.__timestamp = timestamp
        pass

    @os.setter
    def os(self, os):
        self.__os = os

    @comentario.setter
    def comentario(self, comentario):
        self.__comentario = comentario