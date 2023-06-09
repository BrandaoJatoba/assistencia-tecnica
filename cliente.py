from dataAcess import dataAcess
import os
import csv

class Cliente(dataAcess):

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

    # Adição de clientes no banco de dados
    @staticmethod
    def addDataBase(cliente):
        lista = [cliente.nome, cliente.cpf, cliente.telefone]
        with open(Cliente.CSV_PATH, 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')               
                writer.writerow(lista)
                
    # Método para atualizar o DataBase
    @staticmethod
    def refreshDataBase():
        with open(Cliente.CSV_PATH, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            lines = list(reader)
        with open(Cliente.CSV_PATH, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)


    #Remoção de elementos do banco de dados
    @staticmethod
    def delDataBase(x): #Sendo x = CPF 
        with open(Cliente.CSV_PATH, 'r', newline='') as arquivo:
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
        with open(Cliente.CSV_PATH, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)

    @staticmethod
    def populate():
        with open(Cliente.CSV_PATH, 'r') as arquivo_csv:
            arquivo_cliente = csv.reader(arquivo_csv, delimiter = ';')
            for i, line in enumerate(arquivo_cliente):
                if i > 0:
                    client = Cliente(line[0], line[1], line[2])
                    Cliente.listaCliente.append(client)
