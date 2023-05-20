import csv
from cliente import Cliente
from tecnico import Tecnico
from equipamento import Equipamento

class Assistencia:
    listOfClients = []
    listOfTech = []
    listOfOrdemServico = []
    listOfEquipamentos = []
        
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
    

    #Adição de equipamentos ao banco de dados
    @staticmethod
    def addDataBaseEquip():
        listEquip = Assistencia.listOfEquipamentos
        for x in listEquip:
            sn = x.sn
            descricao = x.descricao
            cpfCliente = x.cliente
            matriculaTecnico = x.tecnico
            with open('dados/equipamento.csv', 'a', newline='') as arquivo:
                writer = csv.writer(arquivo, delimiter= ';')
                equipamento = [sn, descricao, cpfCliente, matriculaTecnico]
                writer.writerow(equipamento)
    
    #Remoção de elementos do banco de dados
    @staticmethod
    def delDataBase(csvPath, x): #para "x" sendo nome do tecnico/cliente ou SN do equipamento
        #Ira extrair o csv em uma lista e excluirá o elemento com o indexador correspondente
        with open(csvPath, 'r', newline='') as arquivo:
            reader = csv.reader(arquivo)
            lines = list(reader)
            index = 0
            for line in lines:
                if x in line[0].split(';'):
                    break
                else:
                    index += 1
        lines.remove(lines[index])

        #Reescreverá o arquivo com o elemento desejado excluido
        with open(csvPath, 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerows(lines)
        
if __name__== "__main__":    
    #Adicionando o cliente Jobson
    c1 = Cliente('Jobson', '123.456.789-10', '0101-0101', None)
    t1 = Tecnico('Barbie', '010', 'Notebook')
    Assistencia.listOfClients.append(c1)
    Assistencia.listOfTech.append(t1)
    Assistencia.addDataBaseClient()
    Assistencia.addDataBaseTec()
    
    equip1 = Equipamento('010203', 'Computador Dell - Risco na parte lateral', c1.cpf, t1.matricula)
    Assistencia.listOfEquipamentos.append(equip1)
    Assistencia.addDataBaseEquip()

    #Excluindo o cliente Jobson
    ##Assistencia.delDataBase('dados/cliente.csv', 'Jobson')