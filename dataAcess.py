from abc import ABC, abstractmethod

class dataAcess(ABC):
    
    CSV_PATH = ''

    @abstractmethod
    def addDataBase(item):
        pass    
    
    @abstractmethod
    def refreshDataBase():
        pass

    @abstractmethod
    def delDataBase(identifier): #Para 'identifier' sendo o atributo de cada objeto de classe que o torne único
        pass   

    @abstractmethod
    def populate():
        pass