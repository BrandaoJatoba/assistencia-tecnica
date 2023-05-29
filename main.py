from gui import * 


if __name__ == "__main__":

# Carregando estado do Banco de Dados
    Cliente.populate()
    Tecnico.populate()
    OrdemServico.populate()
    
# Iniciando Interface Gráfica
    MenuScreen()
