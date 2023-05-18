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


    def carregarClientes(self):
        with open(Cliente.enderecoArquivo, "r") as clientes:
            # Parse TEXT from DataBase
            pass
        pass
            

    def delEquipamentos(self, equipamentoRemove):
        if equipamentoRemove in self.__equipamento:
            self.__equipamento.remove(equipamentoRemove)
        else:
            print("Equipamento não existente no bancod de dados")
