import csv

class OrdemServico:

    listaOS = []
    
    def __init__(self, id:int, client, tecnico, status) -> None:
        self.__int = int
        self.__client = client
        self.__tecnico = tecnico
        self.__status = status
        self.__log = []
        pass

    ###### GETTERS AND SETTERS #################

    ############################################

    def populate():
        with open('dados/OS.csv', 'r') as arquivo_csv:
            arquivo_ordemServico = csv.reader(arquivo_csv, delimiter = ';')
            for i, ordemServico in enumerate(arquivo_ordemServico):
                if i > 0:
                    OrdemServico.listaTecnico.append(ordemServico)
