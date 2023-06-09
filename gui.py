from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import time
from cliente import Cliente
from tecnico import Tecnico
from ordemServico import OrdemServico
from especialidade import Especialidade
from log import Log
from status import Status


def BButton(master, text, command):
    style = ttk.Style()
    style.configure("RoundedButton.TButton", relief=RIDGE, background="#333", foreground="#333")
    button = ttk.Button(master, text=text, style="RoundedButton.TButton", command=command)
    return button

def MenuScreen():
    Menu = Tk()
    Menu.title("Assistencia Tecnica 9000")
    Menu.config(bg="#333", padx=100, pady=100)

    menuTitle = Label(Menu, text="Bem Vindo", fg="#F5F5F5", bg="#333")
    menuTitle.grid(row=0, column=1, pady=10, padx=10)

    menuButt = BButton(Menu, text="Cliente", command=ClientScreen)
    menuButt.grid(row=2, column=1, padx=10, pady=10)

    menuButt = BButton(Menu, text="Tecnico", command=TecnicoScreen)
    menuButt.grid(row=3, column=1, padx=10, pady=10)

    menuButt = BButton(Menu, text="Ordem de Serviço", command=Os2)
    menuButt.grid(row=4, column=1, padx=10, pady=10)
    Menu.mainloop()

def ClientScreen():

    ClienteScreen = tk.Toplevel()
    ClienteScreen.title("AT9000 Clientes")
    ClienteScreen.config(bg="#333", padx=50, pady=50)

    clienButt = BButton(ClienteScreen, text="Adicionar Cliente", command=AddClientScreen)
    clienButt.grid(row=0, column=0, padx=15, pady=20)

    clienButt = BButton(ClienteScreen, text="Atualizar Cliente", command=selectClienteScreen)
    clienButt.grid(row=0, column=1, padx=15, pady=20)

def AddClientScreen():

    def storeClientInMemory():
        name = nameEntry.get()
        cpf = cpfEntry.get()
        phone = phoneEntry.get()
        if (name == "") or (cpf == "") or (phone == ""):
            messagebox.showerror('Erro', 'Campos do formulário não podem estar vazios.')
        else:
            client = Cliente(name, cpf, phone)
            Cliente.listaCliente.append(client)
            Cliente.addDataBase(client)
            messagebox.showinfo('Dados Salvos', 'Cliente adicionado com sucesso!')
            AddClientScreen.destroy()

    AddClientScreen = tk.Toplevel()
    AddClientScreen.title("AT9000 Adicionar Cliente")
    AddClientScreen.config(bg="#333", padx=50, pady=50)

    clienText = Label(AddClientScreen, text="Nome", fg="#F5F5F5", bg="#333")
    clienText.grid(row=0, column=0, padx=10, pady=2)

    clienText = Label(AddClientScreen, text="CPF", fg="#F5F5F5", bg="#333")
    clienText.grid(row=1, column=0, padx=10, pady=2)

    clienText = Label(AddClientScreen, text="Telefone", fg="#F5F5F5", bg="#333")
    clienText.grid(row=2, column=0, padx=10, pady=2)

    nameEntry = Entry(AddClientScreen, width=20)
    nameEntry.grid(row=0, column=1)

    cpfEntry = Entry(AddClientScreen, width=20)
    cpfEntry.grid(row=1, column=1)
    
    phoneEntry = Entry(AddClientScreen, width=20)
    phoneEntry.grid(row=2, column=1)

    clienButt = BButton(AddClientScreen, text="Adicionar Cliente", command=storeClientInMemory)
    clienButt.grid(row=3, column=0, columnspan=2, padx=15, pady=20)
        
def updateClientScreen(index):

    def updateClientInMemory():
        name = nameEntry.get()
        cpf = cpfEntry.get()
        phone = phoneEntry.get()
        if (name == "") or (cpf == "") or (phone == ""):
            messagebox.showerror('Erro', 'Campos do formulário não podem estar vazios.')
        else:
            client = Cliente(name, cpf, phone)
            for x in Cliente.listaCliente:
                if x.cpf == cpf:
                    Cliente.listaCliente.remove(x)
            Cliente.delDataBase(cpf)
            Cliente.listaCliente.append(client)
            Cliente.addDataBase(client)
            messagebox.showinfo('Dados Salvos', 'Cliente atualizado com sucesso!')
            clientToUpdateScreen.destroy()
        
    clientToUpdate = Cliente.listaCliente[index]

    clientToUpdateScreen = tk.Toplevel()
    clientToUpdateScreen.title("AT9000 Atualizar Cliente")
    clientToUpdateScreen.config(bg="#333", padx=50, pady=50)

    clienText = Label(clientToUpdateScreen, text="Nome", fg="#F5F5F5", bg="#333")
    clienText.grid(row=0, column=0, padx=10, pady=2)

    clienText = Label(clientToUpdateScreen, text="CPF", fg="#F5F5F5", bg="#333")
    clienText.grid(row=1, column=0, padx=10, pady=2)

    clienText = Label(clientToUpdateScreen, text="Telefone", fg="#F5F5F5", bg="#333")
    clienText.grid(row=2, column=0, padx=10, pady=2)

    nameEntry = Entry(clientToUpdateScreen, width=20)
    nameEntry.grid(row=0, column=1)
    nameEntry.insert(0, clientToUpdate.nome)
    
    cpfEntry = Entry(clientToUpdateScreen, width=20)
    cpfEntry.grid(row=1, column=1)
    cpfEntry.insert(0, clientToUpdate.cpf)
    cpfEntry.config(state= "disabled")
    
    phoneEntry = Entry(clientToUpdateScreen, width=20)
    phoneEntry.grid(row=2, column=1)
    phoneEntry.insert(0, clientToUpdate.telefone)

    clienButt = BButton(clientToUpdateScreen, text="Atualizar Cliente", command=updateClientInMemory)
    clienButt.grid(row=3, column=0, columnspan=2, padx=15, pady=20)

def selectClienteScreen():
    # attention here add case if there is no selection
    def openUpdateClientScreen():
      indexTuple = clientesListbox.curselection()
      if len(indexTuple) != 0:
        index = indexTuple[0]
        updateClientScreen(index)
    
    def updateList():
        clientesListbox.delete(0, END)
        for cliente in Cliente.listaCliente:
            clientesListbox.insert(tk.END, cliente.nome)
        clientesListbox.grid(row=0, column=0, padx=10, pady=10)

    AtuClientScreen = tk.Toplevel()
    AtuClientScreen.title("AT9000 Atualizar Clientes")
    AtuClientScreen.config(bg="#333", padx=50, pady=50)

    clientesListbox = Listbox(AtuClientScreen, width=40)
    updateList()    

    AtuButt = BButton(AtuClientScreen, text="Atualizar Lista Cliente", command=updateList)
    AtuButt.grid(row=1, column=0, padx=10, pady=5)

    AtuButt = BButton(AtuClientScreen, text="Atualizar Cliente", command=openUpdateClientScreen)
    AtuButt.grid(row=1, column=1, padx=10, pady=5)

def Os2():
    Os2Screen = tk.Toplevel()
    Os2Screen.title("AT9000 OS")
    Os2Screen.config(bg="#333", padx=50, pady=50)

    Os2Butt1 = BButton(Os2Screen, text="Nova Ordem de Serviço", command=NovaOSScreen)
    Os2Butt1.grid(row=1, column=1, pady=5)

    Os2Butt2 = BButton(Os2Screen, text="Abrir Ordem de Serviço", command=selectOS)
    Os2Butt2.grid(row=2, column=1, pady=5)

def NovaOSScreen():

    def saveNewOs():
        OrdemServico.currentOsId()
        id = str(OrdemServico.osCount + 1).zfill(6)        
        client = ClientCombobox.get()
        client = client.split(" - ")        
        tecnico = TecCombobox.get()
        tecnico = tecnico.split(" - ")
        status = Status.ABERTO.name
        equipamento = equipamentDescriptionEntry.get("1.0",'end-1c').encode("unicode_escape").decode("utf-8")
        descricao = issueDescriptionEntry.get("1.0",'end-1c').encode("unicode_escape").decode("utf-8")
        if (client == "") or (tecnico == "") or (equipamento == "") or (descricao == ""):
            messagebox.showerror('Erro', 'Campos do formulário não podem estar vazios.')
        else:
            os = OrdemServico(id, client[0], tecnico[0], status, equipamento, descricao)
            OrdemServico.listaOS.append(os)
            OrdemServico.addDataBase(os)
            messagebox.showinfo('Dados Salvos', 'Ordem de Serviço Aberta com sucesso!')
            NOsScreen.destroy()

    NOsScreen = tk.Toplevel()
    NOsScreen.title("AT9000 Nova OS")
    NOsScreen.config(bg="#333", padx=50, pady=50)

    NOsLabel = Label(NOsScreen, text="Selecionar Cliente", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=0, column=0, padx=10, pady=(2, 10))

    ClientCombobox = ttk.Combobox(NOsScreen, width=40)
    ClientCombobox['values'] = ["".join(x.cpf+" - "+x.nome) for x in Cliente.listaCliente]
    ClientCombobox.grid(row=1, column=0, padx=20, pady=2)

    NOsLabel = Label(NOsScreen, text="Selecionar Técnico", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=2, column=0, padx=10, pady=2)

    TecCombobox = ttk.Combobox(NOsScreen, width=40)
    TecCombobox['values'] = ["".join(tecnico.matricula+" - "+tecnico.nome + " ("+tecnico.especialidade+")") for tecnico in Tecnico.listaTecnico]
    TecCombobox.grid(row=3, column=0, padx=20, pady=2)

    NOsLabel = Label(NOsScreen, text="Descrição", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=0, column=1, padx=10, pady=(2, 10))

    issueDescriptionEntry = Text(NOsScreen, height=10, width=30)
    issueDescriptionEntry.grid(row=1, column=1, padx=10, pady=2, rowspan=5)

    NOsLabel = Label(NOsScreen, text="Equipamento(s)", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=6, column=0, padx=10, pady=2)
    equipamentDescriptionEntry = Text(NOsScreen, height=10, width=30)
    equipamentDescriptionEntry.grid(row=7, column=0, padx=10, pady=2, rowspan=5)

    NOsButton = BButton(NOsScreen, text="Salvar", command=saveNewOs)
    NOsButton.grid(row=6, column=1, padx=10, pady=2)

def TecnicoScreen(): 
    TecnicoScreen = tk.Toplevel()
    TecnicoScreen.title("AT9000 Tecnicos")
    TecnicoScreen.config(bg="#333", padx=50, pady=50)

    TecButt = BButton(TecnicoScreen, text="Adicionar Tecnico", command=AddTecnicoScreen)
    TecButt.grid(row=0, column=0, padx=15, pady=20)

    TecButt = BButton(TecnicoScreen, text="Atualizar Tecnico", command=selectTecnicoScreen)
    TecButt.grid(row=0, column=1, padx=15, pady=20)

def AddTecnicoScreen():

    def storetTecInMemory():
        nome = TecNomeEntry.get()
        matricula = TecCpfEntry.get()
        especialidade = TecEspecialidadeCombobox.get()
        is_active = True
        if (nome == "") or (matricula == "") or (especialidade == ""):
            messagebox.showerror('Erro', 'Campos do formulário não podem estar vazios.')
        else:
            tec = Tecnico(nome, matricula, especialidade, is_active)
            Tecnico.listaTecnico.append(tec)
            Tecnico.addDataBase(tec)
            messagebox.showinfo('Dados Salvos', 'Técnico adicionado com sucesso!')
            addTecnicoScreen.destroy()

    addTecnicoScreen = tk.Toplevel()
    addTecnicoScreen.title("AT9000 Adicionar Tecnicos")
    addTecnicoScreen.config(bg="#333", padx=50, pady=50)

    LabelTecNome = Label(addTecnicoScreen, text="Nome", fg="#F5F5F5", bg="#333")
    LabelTecNome.grid(row=0, column=1, padx=10, pady=2)
    TecNomeEntry = Entry(addTecnicoScreen, width=20)
    TecNomeEntry.grid(row=0, column=2)
    
    LabelTecMatricula = Label(addTecnicoScreen, text="Matricula", fg="#F5F5F5", bg="#333")
    LabelTecMatricula.grid(row=1, column=1, padx=10, pady=2)
    TecCpfEntry = Entry(addTecnicoScreen, width=20)
    TecCpfEntry.grid(row=1, column=2)

    LabelTecEspecialidade = Label(addTecnicoScreen, text="Especialidade", fg="#F5F5F5", bg="#333")
    LabelTecEspecialidade.grid(row=2, column=1, padx=10, pady=2)
    TecEspecialidadeCombobox = ttk.Combobox(addTecnicoScreen)
    TecEspecialidadeCombobox['values'] = [especialidade.name for especialidade in Especialidade]
    TecEspecialidadeCombobox.grid(row=2, column=2, padx=17, pady=2)
    
    TecButt = BButton(addTecnicoScreen, text="Adicionar Tecnico", command=storetTecInMemory)
    TecButt.grid(row=3, column=2, padx=7, pady=20)

def selectTecnicoScreen():

    def updateList():
        TecListbox.delete(0, END)
        for tec in Tecnico.listaTecnico:
            TecListbox.insert(tk.END, tec.nome)
    
    def openUpdateClientScreen():
        indexTuple = TecListbox.curselection()
        if len(indexTuple) != 0:
            index = indexTuple[0]
            updateTecnicoScreen(index)
    
    TecnicoScreen = tk.Toplevel()
    TecnicoScreen.title("AT9000 Atualizar Tecnico")
    TecnicoScreen.config(bg="#333", padx=50, pady=50)

    TecListbox = Listbox(TecnicoScreen, width=40)
    TecListbox.grid(row=0, column=0, padx=10, pady=10)
    updateList()

    TecButt = BButton(TecnicoScreen, text="Atualizar Lista", command=updateList)
    TecButt.grid(row=1, column=0, padx=10, pady=5)

    TecButt = BButton(TecnicoScreen, text="Atualizar Tecnico", command=openUpdateClientScreen)
    TecButt.grid(row=1, column=1, padx=10, pady=5)

def updateTecnicoScreen(index):

    def updateTecInMemory():

        nome = TecNomeEntry.get()
        matricula = TecMatriculaEntry.get()
        especialidade = TecEspecialidadeCombobox.get()
        
        if (nome == "") or (matricula == "") or (especialidade == ""):
            messagebox.showerror('Erro', 'Campos do formulário não podem estar vazios.')
        else:
            tec = Tecnico(nome, matricula, especialidade)
            for x in Tecnico.listaTecnico:
                if x.matricula == matricula:
                    Tecnico.listaTecnico.remove(x)

            Tecnico.delDataBase(matricula)
            Tecnico.listaTecnico.append(tec)
            Tecnico.addDataBase(tec)
            messagebox.showinfo('Dados Salvos', 'Técnico atualizado com sucesso!')
            addTecnicoScreen.destroy()     

    tecToUpdate = Tecnico.listaTecnico[index]

    addTecnicoScreen = tk.Toplevel()
    addTecnicoScreen.title("AT9000 Adicionar Tecnicos")
    addTecnicoScreen.config(bg="#333", padx=50, pady=50)

    LabelTecNome = Label(addTecnicoScreen, text="Nome", fg="#F5F5F5", bg="#333")
    LabelTecNome.grid(row=0, column=1, padx=10, pady=2)
    TecNomeEntry = Entry(addTecnicoScreen, width=20)
    TecNomeEntry.grid(row=0, column=2)
    TecNomeEntry.insert(0, tecToUpdate.nome)
    
    LabelTecMatricula = Label(addTecnicoScreen, text="Matricula", fg="#F5F5F5", bg="#333")
    LabelTecMatricula.grid(row=1, column=1, padx=10, pady=2)
    TecMatriculaEntry = Entry(addTecnicoScreen, width=20)
    TecMatriculaEntry.grid(row=1, column=2)
    TecMatriculaEntry.insert(0, tecToUpdate.matricula)

    LabelTecEspecialidade = Label(addTecnicoScreen, text="Especialidade", fg="#F5F5F5", bg="#333")
    LabelTecEspecialidade.grid(row=2, column=1, padx=10, pady=2)
    TecEspecialidadeCombobox = ttk.Combobox(addTecnicoScreen)
    TecEspecialidadeCombobox['values'] = [especialidade.name for especialidade in Especialidade]
    TecEspecialidadeCombobox.grid(row=2, column=2, padx=17, pady=2)
    TecEspecialidadeCombobox.current(int(Especialidade[tecToUpdate.especialidade].value))
    
    TecButt = BButton(addTecnicoScreen, text="Adicionar Tecnico", command=updateTecInMemory)
    TecButt.grid(row=3, column=2, padx=7, pady=20)

def selectOS():
    def searchByCpf():
        cpf = searchBar.get()
        if cpf != "":
            OSListbox.delete(0, END)
            count = 0
            for os in OrdemServico.listaOS:
                if os.client == cpf:
                    count += 1
                    OSListbox.insert(tk.END, "".join("#"+os.id+" "+os.status+" - "+os.equipamento))
            if count < 1:
                messagebox.showinfo('Error', 'Nenhuma OS encontrada com os dados fornecidos.')
    
    def listAllOs():
        OSListbox.delete(0, END)        
        for os in OrdemServico.listaOS:
            OSListbox.insert(tk.END, "".join("#"+os.id+" "+os.status+" - "+str(os.equipamento).encode().decode("unicode_escape")))
        
    def openViewOS():
        osId = OSListbox.get(ANCHOR)
        if osId:
            osId = osId[1:7]
            selectedOs = [os for os in OrdemServico.listaOS if os.id == osId]
            if len(selectedOs)==0:
                print("Error")
            else:
                os = selectedOs[0]
            ViewOS(os)
        else:
            messagebox.showerror('Error', 'Nenhuma OS selecionada')
    
    selectOS = tk.Toplevel()
    selectOS.title("AT9000 Selecionar Ordem de Serviço")
    selectOS.config(bg="#333", padx=50, pady=50)
    selectOS.geometry("700x400")

    OSListbox = Listbox(selectOS, width=60)
    OSListbox.grid(row=1, column=0, padx=10, pady=10)

    searchBar = tk.Entry(selectOS, width=20)
    searchBar.grid(row=0, column=2, padx=10, pady=10)
    
    osSearchButton = BButton(selectOS, text="Pesquisar OS por CPF", command=searchByCpf)
    osSearchButton.grid(row=1, column=2, sticky=tk.N, padx=5, pady=5)

    listAllButton = BButton(selectOS, text="Listar todas OS's", command=listAllOs)
    listAllButton.grid(row=2, column=2, sticky=tk.N, padx=5, pady=5)

    osOpenButton = BButton(selectOS, text="Abrir OS Selecionada", command=openViewOS)
    osOpenButton.grid(row=3, column=2, sticky=tk.N, padx=5, pady=5)

def ViewOS(selectedOs):
    
    def NewComentScreen(selectedOs):    
        def saveLog():
            logText = newLogEntry.get("1.0",'end-1c').encode("unicode_escape").decode("utf-8")
            savedTime = time.localtime(time.time())
            timeString = time.strftime("%d/%m/%Y", savedTime)
            Log.currentlogId()
            if (logText == ""):
                messagebox.showerror('Error', 'Comentário Vazio. Insira comentário ou feche a janela.')
            else: 
                log = Log((Log.logCount + 1), selectedOs.id, logText, timeString)
                Log.listaDeLogs.append(log)
                Log.addDataBase(log)
                newLogScreen.destroy()
                messagebox.showinfo('Log', 'Novo log salvo com sucesso')

        newLogScreen = tk.Toplevel()
        newLogScreen.title("AT9000 Novo Comentario")
        newLogScreen.config(bg="#333", padx=25, pady=25)

        newLogLabel = Label(newLogScreen, text="Comentário", fg="#F5F5F5", bg="#333")
        newLogLabel.grid(row=0, column=0, padx=10, pady=2, sticky=N)

        newLogEntry = Text(newLogScreen, height=10 ,width=30)
        newLogEntry.grid(row=0, column=1, padx=10, pady=2, sticky=S)

        newLogButton = BButton(newLogScreen, text=("Adicionar Comentário"), command=saveLog)
        newLogButton.grid(row=1, column=1, padx=10, pady=2, sticky=W)

        newLogScreen.wait_window(newLogScreen)

        ComentariosText.config(state=NORMAL)
        ComentariosText.delete('1.0', END)
        comentarios = [log for log in Log.listaDeLogs if log.idOS == selectedOs.id]
        for comentario in comentarios:
            ComentariosText.insert(END, str(comentario).encode("utf-8").decode("unicode_escape") + "\n")
        ComentariosText.config(state=DISABLED)

    def AttScreen(selectedOs):

        def updateStatus():
            selectedOs.status = StatusComboBox.get()
            for x in OrdemServico.listaOS:
                if x.id == selectedOs.id:
                    OrdemServico.listaOS.remove(x)
            OrdemServico.delDataBase(selectedOs.id)
            OrdemServico.listaOS.append(selectedOs)
            OrdemServico.addDataBase(selectedOs)
            messagebox.showinfo('Dados Salvos', 'Status atualizado com sucesso!')
            AttScreen.destroy()

        AttScreen = tk.Toplevel()
        AttScreen.title("AT9000 Atualizar Status")
        AttScreen.config(bg="#333", padx=25, pady=25)

        StatusLabel = Label(AttScreen, text="Status", fg="#F5F5F5", bg="#333")
        StatusLabel.grid(row=0, column=0, padx=10, pady=2)

        StatusComboBox = ttk.Combobox(AttScreen)
        StatusComboBox['value'] = [status.name for status in Status]
        StatusComboBox.current(int(Status[selectedOs.status].value))
        StatusComboBox.grid(row=0, column=1, padx=10, pady=2)

        StatusButton = BButton(AttScreen, text="Atualizar", command=updateStatus)
        StatusButton.grid(row=1, column=1, padx=10, pady=2)
        AttScreen.wait_window(AttScreen)
        StatusText.config(text = selectedOs.status)

    ViewOSScreen = Tk()
    ViewOSScreen.title("AT9000 Visualizar OS")
    ViewOSScreen.config(bg="#333", padx=50, pady=50)
    
    CodigoLabel = Label(ViewOSScreen, text="Código :", fg="#F5F5F5", bg="#333")
    CodigoText = Label(ViewOSScreen, text=selectedOs.id, fg="#F5F5F5", bg="#333")
    CodigoLabel.grid(row=0, column=0, padx=10, pady=2, sticky=W)
    CodigoText.grid(row=0, column=1, padx=10, pady=2, sticky=W)

    TecnicoLabel = Label(ViewOSScreen, text="Técnico :", fg="#F5F5F5", bg="#333")

    try:
        TecnicoText = Label(ViewOSScreen, text=[tec.nome for tec in Tecnico.listaTecnico if tec.matricula == selectedOs.tecnico][0], fg="#F5F5F5", bg="#333")
    except:
        TecnicoText = Label(ViewOSScreen, text="Não cadastrado no banco de dados", fg="#F5F5F5", bg="#333")

    TecnicoLabel.grid(row=0, column=3, padx=10, pady=2, sticky=E)
    TecnicoText.grid(row=0, column=4, padx=10, pady=2, sticky=W)

    ClienteLabel = Label(ViewOSScreen, text="Cliente :", fg="#F5F5F5", bg="#333")
    
    try:
        ClienteText = Label(ViewOSScreen, text=[cliente.nome for cliente in Cliente.listaCliente if cliente.cpf == selectedOs.client][0], fg="#F5F5F5", bg="#333")
    except:
        ClienteText = Label(ViewOSScreen, text="Não cadastrado no banco de dados", fg="#F5F5F5", bg="#333")

    ClienteLabel.grid(row=1, column=0, padx=10, pady=2, sticky=W)
    ClienteText.grid(row=1, column=1, padx=10, pady=2, sticky=W)

    StatusLabel = Label(ViewOSScreen, text="Status :", fg="#F5F5F5", bg="#333")
    StatusText = Label(ViewOSScreen, text=selectedOs.status, fg="#F5F5F5", bg="#333")
    StatusLabel.grid(row=1, column=3, padx=10, pady=2, sticky=E)
    StatusText.grid(row=1, column=4, padx=10, pady=2, sticky=W)

    EquipamentoLabel = Label(ViewOSScreen, text="Equipamento :", fg="#F5F5F5", bg="#333")
    EquipamentoText = Label(ViewOSScreen, text=str(selectedOs.equipamento).encode("utf-8").decode('unicode_escape'), fg="#F5F5F5", bg="#333")
    EquipamentoLabel.grid(row=2, column=0, padx=10, pady=2, sticky=W)
    EquipamentoText.grid(row=2, column=1, padx=10, pady=2, sticky=W)    
    
    descricaoLabel = Label(ViewOSScreen, text="Descrição do Problema :", fg="#F5F5F5", bg="#333")
    descricaoLabel.grid(row=3, column=0, padx=10, pady=2, sticky=W)
    
    descricaoText = Label(ViewOSScreen, text=str(selectedOs.descricao).encode("utf-8").decode('unicode_escape'), fg="#F5F5F5", bg="#333")
    descricaoText.grid(row=3, column=1, padx=10, pady=2, sticky=W)

    ComentariosLabel = Label(ViewOSScreen, text="Comentários :", fg="#F5F5F5", bg="#333")
    ComentariosLabel.grid(row=4, column=0, padx=10, pady=2, sticky=W)
    
    comentarios = [log for log in Log.listaDeLogs if log.idOS == selectedOs.id]
    scrollbar = tk.Scrollbar(orient="horizontal")
    ComentariosText = Text(ViewOSScreen, fg="#F5F5F5", bg="#333", xscrollcommand=scrollbar.set)
    ComentariosText.grid(row=5, column=1, padx=10, pady=2, sticky=W)
    for comentario in comentarios:
        ComentariosText.insert(END, str(comentario) + "\n")
    ComentariosText.config(state=DISABLED)

    NewComentButton = BButton(ViewOSScreen, text=("Adicionar Comentário"), command=lambda: NewComentScreen(selectedOs))
    NewComentButton.grid(row=6, column=1, padx=10, pady=2, sticky=W)

    AttButton = BButton(ViewOSScreen, text=("Atualizar Status"), command=lambda: AttScreen(selectedOs))
    AttButton.grid(row=6, column=1, padx=10, pady=2, sticky=E)
