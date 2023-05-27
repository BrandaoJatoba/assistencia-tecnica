from tkinter import *
from tkinter import ttk
import tkinter as tk

# PlaceHolder
ListaDeProduto = [1, 2, 3, 4, 5]
ListaDeClientes = ["João", "Maria", "José", "Ana", "Carlos"]
ListaDeTecnicos = ["Jorge", "Marcelo", "Josepha", "Carla"]
# PlaceHolder

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
    def NovoCli():
        ClienteScreen.destroy()
        AddClientScreen()
    def ATTCli():
        ClienteScreen.destroy()
        AttClientScreen()

    ClienteScreen = tk.Toplevel()
    ClienteScreen.title("AT9000 Clientes")
    ClienteScreen.config(bg="#333", padx=50, pady=50)

    clienButt = BButton(ClienteScreen, text="Adicionar Cliente", command=NovoCli)
    clienButt.grid(row=0, column=0, padx=15, pady=20)

    clienButt = BButton(ClienteScreen, text="Atualizar Cliente", command=ATTCli)
    clienButt.grid(row=0, column=1, padx=15, pady=20)


def AddClientScreen():
    AddClientScreen = tk.Toplevel()
    AddClientScreen.title("AT9000 Adicionar Cliente")
    AddClientScreen.config(bg="#333", padx=50, pady=50)

    clienText = Label(AddClientScreen, text="Nome", fg="#F5F5F5", bg="#333")
    clienText.grid(row=0, column=0, padx=10, pady=2)

    clienText = Label(AddClientScreen, text="CPF", fg="#F5F5F5", bg="#333")
    clienText.grid(row=1, column=0, padx=10, pady=2)

    clienText = Label(AddClientScreen, text="Telefone", fg="#F5F5F5", bg="#333")
    clienText.grid(row=2, column=0, padx=10, pady=2)

    clienWrite = Entry(AddClientScreen, width=20)
    clienWrite.grid(row=0, column=1)

    clienWrite = Entry(AddClientScreen, width=20)
    clienWrite.grid(row=1, column=1)
    
    clienWrite = Entry(AddClientScreen, width=20)
    clienWrite.grid(row=2, column=1)

    clienButt = BButton(AddClientScreen, text="Adicionar Cliente", command=None)
    clienButt.grid(row=3, column=0, columnspan=2, padx=15, pady=20)

def AttClientScreen():
    AtuClientScreen = tk.Toplevel()
    AtuClientScreen.title("AT9000 Atualizar Clientes")
    AtuClientScreen.config(bg="#333", padx=50, pady=50)

    listbox = Listbox(AtuClientScreen, width=40)
    for cliente in ListaDeClientes:
        listbox.insert(tk.END, cliente)
    listbox.grid(row=0, column=0, padx=10, pady=10)

    AtuButt = BButton(AtuClientScreen, text="Remover Cliente", command=None)
    AtuButt.grid(row=1, column=0, padx=10, pady=5)

    AtuButt = BButton(AtuClientScreen, text="Atualizar Cliente", command=None)
    AtuButt.grid(row=1, column=1, padx=10, pady=5)


def Os2():
    def NovaOS():
        Os2Screen.destroy()
        NovaOSScreen()
    def AbrirOS():
        Os2Screen.destroy()
        AbrirOSScreen()

    Os2Screen = tk.Toplevel()
    Os2Screen.title("AT9000 OS")
    Os2Screen.config(bg="#333", padx=50, pady=50)

    Os2Butt1 = BButton(Os2Screen, text="Nova Ordem de Serviço", command=NovaOS)
    Os2Butt1.grid(row=1, column=1, pady=5)

    Os2Butt2 = BButton(Os2Screen, text="Abrir Ordem de Serviço", command=AbrirOS)
    Os2Butt2.grid(row=2, column=1, pady=5)

def NovaOSScreen():
    NOsScreen = tk.Toplevel()
    NOsScreen.title("AT9000 Nova OS")
    NOsScreen.config(bg="#333", padx=50, pady=50)

    NOsLabel = Label(NOsScreen, text="Selecionar Cliente", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=0, column=0, padx=10, pady=(2, 10))

    NOsCombobox = ttk.Combobox(NOsScreen)
    NOsCombobox.grid(row=1, column=0, padx=10, pady=2)

    NOsLabel = Label(NOsScreen, text="Selecionar Técnico", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=2, column=0, padx=10, pady=2)

    NOsCombobox = ttk.Combobox(NOsScreen)
    NOsCombobox.grid(row=3, column=0, padx=10, pady=2)

    NOsLabel = Label(NOsScreen, text="Descrição", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=0, column=1, padx=10, pady=(2, 10))

    NOsEntry = Text(NOsScreen, height=10, width=30)
    NOsEntry.grid(row=1, column=1, padx=10, pady=2, rowspan=5)

    NOsLabel = Label(NOsScreen, text="Equipamento", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=6, column=0, padx=10, pady=2)

    NOsEntry = Entry(NOsScreen)
    NOsEntry.grid(row=7, column=0, padx=10, pady=2)

    def adicionar_equipamento():
        equipamento = NOsEntry.get()
        NOsListbox.insert(END, equipamento)
        NOsEntry.delete(0, END)

    NOsButton = BButton(NOsScreen, text="Adicionar", command=adicionar_equipamento)
    NOsButton.grid(row=8, column=0, padx=10, pady=2)

    NOsListbox = Listbox(NOsScreen)
    NOsListbox.grid(row=9, column=0, padx=10, pady=(2, 10))

    NOsButton = BButton(NOsScreen, text="Salvar", command=None)
    NOsButton.grid(row=6, column=1, padx=10, pady=2)


def AbrirOSScreen():
    AbrirOSScreen = tk.Toplevel()
    AbrirOSScreen.title("AT9000 Abrir OS")
    AbrirOSScreen.config(bg="#333", padx=50, pady=50)

    AOSLabel = Label(AbrirOSScreen, text="Cliente", fg="#F5F5F5", bg="#333")
    AOSLabel.grid(row=0, column=0, padx=10, pady=2)

    AOSLabel = Label(AbrirOSScreen, text="N/S", fg="#F5F5F5", bg="#333")
    AOSLabel.grid(row=1, column=0, padx=10, pady=2)

    AOSLabel = Label(AbrirOSScreen, text="Descrição", fg="#F5F5F5", bg="#333")
    AOSLabel.grid(row=2, column=0, padx=10, pady=2)

    AOSClientecombobox = ttk.Combobox(AbrirOSScreen)
    AOSClientecombobox.grid(row=0, column=1, padx=10, pady=2)

    AOSNS = Entry(AbrirOSScreen, state="readonly")
    AOSNS.grid(row=1, column=1, padx=10, pady=2)

    AOSDesc = Text(AbrirOSScreen, height=10, width=20)
    AOSDesc.grid(row=2, column=1, padx=10, pady=2)

    AOSButton = BButton(AbrirOSScreen, text="Salvar", command=None)
    AOSButton.grid(row=3, column=1, padx=10, pady=2)


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
