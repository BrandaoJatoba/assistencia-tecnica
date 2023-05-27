import csv

class Equipamento:

    listaEquipamentos = []

    def __init__(self, sn, descricao, cpfCliente, matriculaTecnico) -> None:
        self.__sn = sn
        self.__descricao = descricao
        self.__cliente = cpfCliente
        self.__tecnico = matriculaTecnico

    @property
    def sn(self):
        return self.__sn

    @property
    def descricao(self):
        return self.__descricao

    @property
    def cliente(self):
        return self.__cliente

    @property
    def tecnico(self):
        return self.__tecnico    

    
    def populate():
        with open('dados/equipamento.csv', 'r') as arquivo_csv:
            arquivo_equipamento = csv.reader(arquivo_csv, delimiter = ';')
            for i, equipamento in enumerate(arquivo_equipamento):
                if i > 0:
                    Equipamento.listaEquipamentos.append(equipamento)


    #Adição de equipamentos ao banco de dados
    @staticmethod
    def addDataBaseEquip(lista):
        listEquip = lista
        for x in listEquip:
            sn = x.sn
            descricao = x.descricao
            cpfCliente = x.cliente
            matriculaTecnico = x.tecnico
            with open('dados/equipamento.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')
                equipamento = [sn, descricao, cpfCliente, matriculaTecnico]
                writer.writerow(equipamento)

    #Remoção de elementos do banco de dados
    @staticmethod
    def delDataBase(csvPath, SN):
        with open(csvPath, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            lines = list(reader)
            index = 0
            for line in lines:
                if SN in line[0].split(';'):
                    break
                else:
                    index += 1
        lines.remove(lines[index])

        #Reescreverá o arquivo com o elemento desejado excluido
        with open(csvPath, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    #Métodos que adicionaram e removeam
    def addEquipamento(equipamentoNovo):
        Equipamento.listaEquipamentos.append(equipamentoNovo)
        pass

    def delEquipamentos(self, equipamentoRemove):
        if equipamentoRemove in Equipamento.listaEquipamentos:
            Equipamento.listaEquipamentos.remove(equipamentoRemove)
        else:
            print("Equipamento não existente no banco de dados")