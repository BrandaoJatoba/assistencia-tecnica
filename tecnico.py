from dataAcess import dataAcess
import especialidade
import csv

class Tecnico(dataAcess):
    CSV_PATH = 'dados/tecnico.csv'

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

    #Adição de tecnicos no banco de dados
    @staticmethod
    def addDataBase(tec):
        lista = [tec.nome, tec.matricula, tec.especialidade]
        with open(Tecnico.CSV_PATH, 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')               
                writer.writerow(lista)  

    @staticmethod
    def refreshDataBase():
        with open(Tecnico.CSV_PATH, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            lines = list(reader)
        with open(Tecnico.CSV_PATH, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    #Remoção de elementos do banco de dados
    @staticmethod
    def delDataBase(x): #Sendo x = CPF 
        with open(Tecnico.CSV_PATH, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            lines = list(reader)
            index = 0
            for line in lines:
                if x in line[0].split(';'):
                    break
                else:
                    index += 1
        lines.remove(lines[index])

        #Reescreverá o arquivo com o elemento desejado excluido
        with open(Tecnico.CSV_PATH, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    @staticmethod
    def populate():
        with open(Tecnico.CSV_PATH, 'r') as arquivo_csv:
            arquivo_tecnico = csv.reader(arquivo_csv, delimiter = ';')
            for i, line in enumerate(arquivo_tecnico):
                if i > 0:
                    tec = Tecnico(line[0], line[1], line[2])
                    Tecnico.listaTecnico.append(tec)
