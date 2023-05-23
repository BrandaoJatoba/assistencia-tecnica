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

    def addEquipamento(equipamentoNovo):
        Equipamento.listaEquipamentos.append(equipamentoNovo)
        pass

    def delEquipamentos(self, equipamentoRemove):
        if equipamentoRemove in Equipamento.listaEquipamentos:
            Equipamento.listaEquipamentos.remove(equipamentoRemove)
        else:
            print("Equipamento não existente no banco de dados")