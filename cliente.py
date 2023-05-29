import os
import csv

class Cliente:

    CSV_PATH = 'dados/cliente.csv'

    listaCliente = []

    def __init__(self, nome, cpf, telefone) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        pass
    
## GETTERS AND SETTERS ############################
    @property
    def nome(self):
        return self.__nome    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        pass    
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        pass    
    @property
    def telefone(self):
        return self.__telefone    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
        pass
##################################################

# Outros Métodos

### Adição de clientes no banco de dados
    @staticmethod
    def addSingleCliente(lista):
        with open('dados/cliente.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')               
                writer.writerow(lista)

    @staticmethod
    def addDataBaseClient(lista):
        listClients = lista
        for x in listClients:
            nome = x.nome
            cpf = x.cpf
            tel = x.telefone
            with open('dados/cliente.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')
                cliente = [nome, cpf, tel]
                writer.writerow(cliente)

    #Remoção de elementos do banco de dados
    @staticmethod
    def delDataBase(CPF): 
        with open(Cliente.CSV_PATH, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            lines = list(reader)
            index = 0
            for line in lines:
                if CPF in line[0].split(';'):
                    break
                else:
                    index += 1
        lines.remove(lines[index])

        #Reescreverá o arquivo com o elemento desejado excluido
        with open(Cliente.CSV_PATH, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    @staticmethod
    def populate():
        with open(Cliente.CSV_PATH, 'r') as arquivo_csv:
            arquivo_cliente = csv.reader(arquivo_csv, delimiter = ';')
            for i, cliente in enumerate(arquivo_cliente):
                if i > 0:
                    Cliente.listaCliente.append(cliente)

if __name__== "__main__":
    lista = Cliente.populate()
    print(lista)

