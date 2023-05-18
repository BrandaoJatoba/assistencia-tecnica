import csv

class Cliente:

    def __init__(self, nome, cpf, telefone, equipamento) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__equipamento = [equipamento]
        pass
    
    #Getter e Setter do atributo nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        pass
    
    #Getter e Setter do atributo cpf
    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        pass
    
    #Getter e Setter do atributo telefone
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
        pass

    #Getter do atributo equipamento + função de adição e remoção de equipamentos
    @property
    def equipamento(self) -> list:
        return self.__equipamento

    def addEquipamento(self, equipamentoNovo):
        self.__equipamento.append(equipamentoNovo)
        pass

    def delEquipamentos(self, equipamentoRemove):
        if equipamentoRemove in self.__equipamento:
            self.__equipamento.remove(equipamentoRemove)
        else:
            print("Equipamento não existente no bancod de dados")
    
    #############Métodos
    
    
    
    #Método de população da lista de clientes
    def populate():
        listaCliente = []
        with open('dados/cliente.csv', 'r') as arquivo_csv:
            arquivo_cliente = csv.reader(arquivo_csv, delimiter = ';')
            for i, cliente in enumerate(arquivo_cliente):
                if i > 0:
                    listaCliente.append(cliente)
                else:
                    pass
        return listaCliente