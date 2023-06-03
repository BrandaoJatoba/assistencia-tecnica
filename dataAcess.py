from abc import ABC, abstractmethod

class dataAcess(ABC):
    
    @abstractmethod
    def addDataBase(csvPath):
        pass

    @abstractmethod
    def delDataBase(x, csvPath): #Para x sendo o atributo de cada objeto de classe que o torne único
        pass   

    @abstractmethod
    def populate(csvPath):
        pass