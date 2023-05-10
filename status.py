from enum import Enum

class Status(Enum):
    ABERTO = 0
    EM_ANDAMENTO = 1
    SUSPENSO = 2
    CANCELADO = 3
    ENCERRADO = 4