class Equipamento:

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
