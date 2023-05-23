import especialidade
import csv

class Tecnico:

    listaTecnico = []

    def __init__(self, nome, matricula, especialidade) -> None:
        self.__nome = nome
        self.__matricula = matricula
        self.__especialidade = especialidade

##### GETTERS AND SETTERS############################
    @property
    def nome(self):
        return self.__nome
    @property
    def matricula(self):
        return self.__matricula
    @property
    def especialidade(self):
        return self.__especialidade    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula    
    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade
###################################################

#### Outros Métodos
    
    def populate():
        with open('dados/tecnico.csv', 'r') as arquivo_csv:
            arquivo_tecnico = csv.reader(arquivo_csv, delimiter = ';')
            for i, tecnico in enumerate(arquivo_tecnico):
                if i > 0:
                    Tecnico.listaTecnico.append(tecnico)

if __name__== "__main__":
    lista = Tecnico.populate()
    print(lista)
