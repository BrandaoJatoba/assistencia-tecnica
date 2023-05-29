import csv

class OrdemServico:

    listaOS = []
    
    def __init__(self, id:int, client, tecnico, status, equipamento) -> None:
        self.__int = int
        self.__client = client
        self.__tecnico = tecnico
        self.__status = status
        self.__log = []
        self.__equipamento = equipamento
        pass

    ###### GETTERS AND SETTERS #################

    ############################################
    #Adição de OS ao banco de dados
    @staticmethod
    def addDataBaseOS(lista):
        listOS = lista
        for x in listOS:
            id = x.id
            client = x.client
            tecnico = x.tecnico
            status = x.status
            log = x.log
            with open('dados/OS.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')
                OS = [id, client, tecnico, status]
                writer.writerow(OS)

    #Remoção de elementos do banco de dados
    @staticmethod
    def delDataBase(csvPath, id): 
        with open(csvPath, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            lines = list(reader)
            index = 0
            for line in lines:
                if id in line[0].split(';'):
                    break
                else:
                    index += 1
        lines.remove(lines[index])

        #Reescreverá o arquivo com o elemento desejado excluido
        with open(csvPath, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    def populate():
        with open('dados/OS.csv', 'r') as arquivo_csv:
            arquivo_ordemServico = csv.reader(arquivo_csv, delimiter = ';')
            for i, ordemServico in enumerate(arquivo_ordemServico):
                if i > 0:
                    OrdemServico.listaTecnico.append(ordemServico)
