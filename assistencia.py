import csv
from cliente import Cliente
from tecnico import Tecnico
from equipamento import Equipamento

class Assistencia:
    listOfClients = []
    listOfTech = []
    listOfOrdemServico = []
    listOfEquipamentos = []
    
        
if __name__== "__main__":    
    #Adicionando o cliente Jobson
    c1 = Cliente('Jobson', '123.456.789-10', '0101-0101', None)
    t1 = Tecnico('Barbie', '010', 'Notebook')

    # Assistencia.listOfClients.append(c1)
    # Cliente.addDataBaseClient(Assistencia.listOfClients)

    # Assistencia.listOfTech.append(t1)
    # Tecnico.addDataBaseTec(Assistencia.listOfTech)
    
    equip1 = Equipamento('010203', 'Computador Dell - Risco na parte lateral', c1.cpf, t1.matricula)
    equip2 = Equipamento('040506', 'Notebook Lenovo - Tela quebrada', '987.654.321-98', '005')
    equip3 = Equipamento('070809', 'Desktop HP - Placa de vídeo com defeito', '456.789.123-45', '007')
    equip4 = Equipamento('101112', 'Celular Samsung - Bateria descarregando rápido', '321.654.987-12', '012')
    equip5 = Equipamento('131415', 'Notebook Dell - Teclado com teclas falhando', '654.987.321-09', '003')
    equip6 = Equipamento('161718', 'Celular Apple - Tela trincada', '123.456.789-10', '010')
    Assistencia.listOfEquipamentos.append(equip1)
    Assistencia.listOfEquipamentos.append(equip2)
    Assistencia.listOfEquipamentos.append(equip3)
    Assistencia.listOfEquipamentos.append(equip4)
    Assistencia.listOfEquipamentos.append(equip5)
    Assistencia.listOfEquipamentos.append(equip6)

    Equipamento.addDataBaseEquip(Assistencia.listOfEquipamentos)