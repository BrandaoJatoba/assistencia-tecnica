from dataAcess import dataAcess
import time
import csv

class Log(dataAcess):

    CSV_PATH = 'dados/log.csv'

    listaDeLogs = []

    def __init__(self, id, idOS, comentario, timestamp) -> None:
        self.__id = id
        self.__idOS = idOS
        self.__comentario = comentario
        self.__timestamp = timestamp

########### GETTERS E SETTERS #############
    @property
    def id(self):
        return self.__id
    @property
    def idOS(self):
        return self.__idOS
    @property
    def comentario(self):
        return self.__comentario    
    @property
    def timestamp(self):
        return self.__timestamp
    @id.setter
    def id(self, id):
        self.__id = id
    @idOS.setter
    def idOS(self, idOS):
        self.__idOS = idOS
    @comentario.setter
    def comentario(self, comentario):
        self.__comentario = comentario
###########################################

# Outros Métodos

    @staticmethod
    def addDataBase(csvPath = CSV_PATH):
        listLog = Log.listaDeLogs
        for x in listLog:
            id = x.id
            idOS = x.idOS
            comentario = x.comentario
            with open(csvPath, 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')
                log = [id, idOS, comentario]
                writer.writerow(log)

    @staticmethod
    def delDataBase(x, csvPath = CSV_PATH): #Sendo x = id 
        with open(csvPath, 'r', newline='') as arquivo:
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
        with open(csvPath, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    @staticmethod
    def populate(csvPath = CSV_PATH):
        with open(csvPath, 'r') as arquivo_csv:
            arquivo_Log = csv.reader(arquivo_csv, delimiter = ';')
            for i, line in enumerate(arquivo_Log):
                if i > 0:
                    log = Log(line[0], line[1], line[2], line[3])
                    Log.listaDeLogs.append(log)

    def __str__(self):
        return f"{self.timestamp}\n{self.comentario}"
    
if __name__== "__main__":
    
    # Teste do método de adição
    logTeste = Log(
        '001', '001', 'Computador designado para o técnico menino da porteira.'
    )
    logTeste2 = Log(
        '002', '001', 'Computador em questão apresenta falha na memória, necessário de uma nova.'
    )
    logTeste3 = Log(
        '003', '002', 'Notebook designado para a técnica Barbie'
     )
    logTeste4 = Log(
        '004', '001', 'Computador pronto para ser entregue.'
     )
    # Log.listaDeLogs.append(logTeste)
    # Log.listaDeLogs.append(logTeste2)
    # Log.listaDeLogs.append(logTeste3)
    Log.listaDeLogs.append(logTeste4)
    Log.addDataBase()

    #Teste do método de remoção
    # Log.delDataBase('001')

    #Teste do método de populate
    # Log.populate()
