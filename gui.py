from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from cliente import Cliente
from tecnico import Tecnico
from ordemServico import OrdemServico

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
####### place try except here
        name = nameEntry.get()
        cpf = cpfEntry.get()
        phone = phoneEntry.get()
        lista = [name, cpf, phone]
        Cliente.listaCliente.append(lista)
        Cliente.addSingleCliente(lista)
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
####### place try except here
        name = nameEntry.get()
        cpf = cpfEntry.get()
        phone = phoneEntry.get()
        lista = [name, cpf, phone]
        for x in Cliente.listaCliente:
            if x[1]==cpf:
                Cliente.listaCliente.remove(x)
        Cliente.listaCliente.append(lista)
        Cliente.delDataBase(cpf)
        Cliente.addSingleCliente(lista)
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
    nameEntry.insert(0, clientToUpdate[0])
    
    cpfEntry = Entry(clientToUpdateScreen, width=20)
    cpfEntry.grid(row=1, column=1)
    cpfEntry.insert(0, clientToUpdate[1])
    cpfEntry.config(state= "disabled")
    
    phoneEntry = Entry(clientToUpdateScreen, width=20)
    phoneEntry.grid(row=2, column=1)
    phoneEntry.insert(0, clientToUpdate[2])

    clienButt = BButton(clientToUpdateScreen, text="Atualizar Cliente", command=updateClientInMemory)
    clienButt.grid(row=3, column=0, columnspan=2, padx=15, pady=20)

def selectClienteScreen():

    def openUpdateClientScreen():
      indexTuple = clientesListbox.curselection()
      if len(indexTuple) != 0:
        index = indexTuple[0]
        updateClientScreen(index)
    
    def updateList():
        clientesListbox.delete(0, END)
        for cliente in Cliente.listaCliente:
            clientesListbox.insert(tk.END, cliente[0])
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

    Os2Butt2 = BButton(Os2Screen, text="Abrir Ordem de Serviço", command=None)
    Os2Butt2.grid(row=2, column=1, pady=5)

def NovaOSScreen():
    NOsScreen = tk.Toplevel()
    NOsScreen.title("AT9000 Nova OS")
    NOsScreen.config(bg="#333", padx=50, pady=50)

    NOsLabel = Label(NOsScreen, text="Selecionar Cliente", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=0, column=0, padx=10, pady=(2, 10))

    NOsCombobox = ttk.Combobox(NOsScreen)
    NOsCombobox['values'] = ["".join(x[1]+" - "+x[0]) for x in Cliente.listaCliente]
    NOsCombobox.grid(row=1, column=0, padx=10, pady=2)

    NOsLabel = Label(NOsScreen, text="Selecionar Técnico", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=2, column=0, padx=10, pady=2)

    NOsCombobox = ttk.Combobox(NOsScreen)
    NOsCombobox['values'] = [tecnico[0] for tecnico in Tecnico.listaTecnico]
    NOsCombobox.grid(row=3, column=0, padx=10, pady=2)

    NOsLabel = Label(NOsScreen, text="Descrição", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=0, column=1, padx=10, pady=(2, 10))

    NOsEntry = Text(NOsScreen, height=10, width=30)
    NOsEntry.grid(row=1, column=1, padx=10, pady=2, rowspan=5)

    NOsLabel = Label(NOsScreen, text="Equipamento(s)", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=6, column=0, padx=10, pady=2)
    equipamentDescription = Text(NOsScreen, height=10, width=30)
    equipamentDescription.grid(row=7, column=0, padx=10, pady=2, rowspan=5)

    NOsButton = BButton(NOsScreen, text="Salvar", command=None)
    NOsButton.grid(row=6, column=1, padx=10, pady=2)

def TecnicoScreen():
    TecnicoScreen = tk.Toplevel()
    TecnicoScreen.title("AT9000 Tecnicos")
    TecnicoScreen.config(bg="#333", padx=50, pady=50)

    TecText = Label(TecnicoScreen, text="Nome", fg="#F5F5F5", bg="#333")
    TecText.grid(row=0, column=1, padx=10, pady=2)
    
    TecText = Label(TecnicoScreen, text="Matricula", fg="#F5F5F5", bg="#333")
    TecText.grid(row=1, column=1, padx=10, pady=2)

    TecText = Label(TecnicoScreen, text="Especialidade", fg="#F5F5F5", bg="#333")
    TecText.grid(row=2, column=1, padx=10, pady=2)

    TecWrite = Entry(TecnicoScreen, width=20)
    TecWrite.grid(row=0, column=2)

    TecWrite = Entry(TecnicoScreen, width=20)
    TecWrite.grid(row=1, column=2)

    TecWrite = Entry(TecnicoScreen, width=20)
    TecWrite.grid(row=2, column=2)
    
    TecButt = BButton(TecnicoScreen, text="Adicionar Tecnico", command=None)
    TecButt.grid(row=3, column=2, padx=7, pady=20)

if __name__ == "__main__":
    MenuScreen()
