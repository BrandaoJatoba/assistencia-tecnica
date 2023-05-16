import os

class Cliente:

    diretorio = os.path.dirname(__file__)
    caminhoRelativo = "/bd/clientes.txt"
    enderecoArquivo = os.path.join(diretorio, caminhoRelativo)

    def __init__(self, nome, cpf, telefone, equipamento) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.__equipamento = [equipamento]
        pass

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def equipamento(self) -> list:
        return self.__equipamento
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
        pass

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf
        pass

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone
        pass

    def addEquipamento(self, equipamentoNovo):
        self.__equipamento.append(equipamentoNovo)
        pass

    def carregarClientes(self):
        with open(Cliente.enderecoArquivo, "r") as clientes:
            # Parse TEXT from DataBase
            pass
        pass
            
