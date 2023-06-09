from dataAcess import dataAcess
from log import Log
import csv

class OrdemServico(dataAcess):

    CSV_PATH = 'dados/OS.csv'

    listaOS = []
    osCount = 0
    
    def __init__(self, id, client, tecnico, status, equipamento, descricao) -> None:
        self.__id = id
        self.__client = client
        self.__tecnico = tecnico
        self.__status = status
        self.__equipamento = equipamento
        self.__descricao = descricao
        pass

    ###### GETTERS AND SETTERS #################

    @property
    def id(self):
        return self.__id
    @property
    def client(self):
        return self.__client
    @property
    def tecnico(self):
        return self.__tecnico
    @property
    def status(self):
        return self.__status   
    @property
    def equipamento(self):
        return self.__equipamento   
    @property
    def descricao(self):
        return self.__descricao   
    @id.setter
    def id(self, id):
        self.__id = id    
    @client.setter
    def client(self, client):
        self.__client = client    
    @tecnico.setter
    def tecnico(self, tecnico):
        self.__tecnico = tecnico
    @status.setter
    def status(self, status):
        self.__status = status
    @equipamento.setter
    def equipamento(self, equipamento):
        self.__equipamento = equipamento   
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao  

    ############################################
    #Adição de OS no banco de dados
    @staticmethod
    def addDataBase(os):
        lista = [os.id, os.client, os.tecnico, os.status, os.equipamento, os.descricao]
        with open(OrdemServico.CSV_PATH, 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')               
                writer.writerow(lista)      
    
    
    @staticmethod
    def refreshDataBase():
        with open(OrdemServico.CSV_PATH, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            lines = list(reader)
        with open(OrdemServico.CSV_PATH, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    #Remoção de elementos do banco de dados
    @staticmethod
    def delDataBase(x): #Sendo x = id 
        with open(OrdemServico.CSV_PATH, 'r', newline='') as arquivo:
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
        with open(OrdemServico.CSV_PATH, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    @staticmethod
    def populate():
        with open(OrdemServico.CSV_PATH, 'r') as arquivo_csv:
            arquivo_ordemServico = csv.reader(arquivo_csv, delimiter = ';')
            for i, line in enumerate(arquivo_ordemServico):
                if i > 0:
                    Os = OrdemServico(line[0], line[1], line[2], line[3], line[4], line[5])
                    OrdemServico.listaOS.append(Os)
        OrdemServico.currentOsId()
    
    @staticmethod
    def logOS(idUnique): #idOS precisa ser uma string
        listLogFull = Log.listaDeLogs
        listLogUnique = []
        for log in listLogFull:
            if log.idOS == idUnique:
                listLogUnique.append(log)
            else:
                pass
        return listLogUnique
    
    @staticmethod
    def currentOsId():
        with open(OrdemServico.CSV_PATH, 'r') as arquivo_csv:
            OrdemServico.osCount = sum(1 for line in arquivo_csv) - 1
