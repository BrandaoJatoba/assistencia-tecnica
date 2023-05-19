import csv
from cliente import Cliente
from tecnico import Tecnico

class Assistencia:
    listOfClients = []
    listOfTech = []
    listOfOrdemServico = []
        
    #Adição de clientes no banco de dados
    @staticmethod
    def addDataBaseClient():
        listClients = Assistencia.listOfClients
        for x in listClients:
            nome = x.nome
            cpf = x.cpf
            tel = x.telefone
            equip = x.equipamento
            with open('dados/cliente.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')
                cliente = [nome, cpf, tel, equip]
                writer.writerow(cliente)

    #Adição de tecnicos no banco de dados
    @staticmethod
    def addDataBaseTec():
        listTech = Assistencia.listOfTech
        for x in listTech:
            nome = x.nome
            matricula = x.matricula
            especialidade = x.especialidade
            with open('dados/tecnico.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')
                tecnico = [nome, matricula, especialidade]
                writer.writerow(tecnico)

    
if __name__== "__main__":    

    c1 = Cliente('Jobson', '123.456.789-10', '0101-0101', 'Celular')
    c2 = Cliente('Menina da porteira', '123.456.789-20', '0202-0202', 'Celular')
    c3 = Cliente('Zack Efron', '123.456.789-30', '0303-0303', 'Notebook')
    c4 = Cliente('Claudia Leite', '123.456.789-40', '0404-0404', 'Computador')
    c5 = Cliente('Ivete Sangalo', '123.456.789-50', '0505-0505', 'Computador')
    c6 = Cliente('Shakira', '123.456.789-60', '0606-0606', 'Celular')
    c7 = Cliente('Hebe Camargo', '123.456.789-70', '0707-0707', 'Notebook')
    c8 = Cliente('Michal Jackson', '123.456.789-80', '0808-0808', 'Computador')

    t1 = Tecnico('Tata Werneck', '007', 'Computadores')
    t2 = Tecnico('Silvio Santos', '008', 'Celular')

    Assistencia.listOfClients.append(c1)
    Assistencia.listOfClients.append(c2)
    Assistencia.listOfClients.append(c3)
    Assistencia.listOfClients.append(c4)
    Assistencia.listOfClients.append(c5)
    Assistencia.listOfClients.append(c6)
    Assistencia.listOfClients.append(c7)
    Assistencia.listOfClients.append(c8)

    Assistencia.listOfTech.append(t1)
    Assistencia.listOfTech.append(t2)

    Assistencia.addDataBaseClient()
    Assistencia.addDataBaseTec()

    #Para testar novamente, limpar as linhas do csv, exceto os respectivos cabeçalhos