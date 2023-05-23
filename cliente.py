import os
import csv

class Cliente:

    listaCliente = []

    def __init__(self, nome, cpf, telefone, equipamento) -> None:
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

### Outros Métodos
    @staticmethod
    def populate():
        with open('dados/cliente.csv', 'r') as arquivo_csv:
            arquivo_cliente = csv.reader(arquivo_csv, delimiter = ';')
            for i, cliente in enumerate(arquivo_cliente):
                if i > 0:
                    Cliente.listaCliente.append(cliente)

if __name__== "__main__":
    lista = Cliente.populate()
    print(lista)

