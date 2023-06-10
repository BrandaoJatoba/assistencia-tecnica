from gui import * 


if __name__ == "__main__":

# Carregando estado do Banco de Dados
    try:
        # try to access files
        # if unsuccessful create file
        # finally populate classes
        
        Cliente.populate()
        Tecnico.populate()
        OrdemServico.populate()
        Log.populate()

    except:

        pass

    finally:  
          
    # Iniciando Interface Gráfica
        MenuScreen()
