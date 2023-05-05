class Tecnico:
    def __init__(self, nome, matricula, especialidade) -> None:
        self.__nome = nome
        self.__matricula = matricula
        self.__especialidade = especialidade

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula

    @property
    def especialidade(self):
        return self.__especialidade
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    
    @especialidade.setter
    def especialidade(self, especialidade):
        self.__especialidade = especialidade

