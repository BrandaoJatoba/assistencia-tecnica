from tkinter import *
from tkinter import ttk
import tkinter as tk
from cliente import Cliente
from equipamento import Equipamento
from tecnico import Tecnico
from ordemServico import OrdemServico

#PlaceHolder
ListaDeProduto = [1, 2, 3, 4, 5]
ListaDeClientes = ["João", "Maria", "José", "Ana", "Carlos"]
ListaDeTecnicos = ["Jorge", "Marcelo", "Josepha", "Carla"]
#PlaceHolder

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

    menuButt = BButton(Menu, text="Tecnico", command=None)
    menuButt.grid(row=3, column=1, padx=10, pady=10)

    menuButt = BButton(Menu, text="Ordem de Serviço", command=Os2)
    menuButt.grid(row=4, column=1, padx=10, pady=10)
    
    Menu.mainloop()

def ClientScreen():  
    ClienteScreen = tk.Toplevel()
    ClienteScreen.title("AT9000 Clientes")
    ClienteScreen.config(bg="#333", padx=50, pady=50)

    clienText = Label(ClienteScreen, text="Nome", fg="#F5F5F5", bg="#333")
    clienText.grid(row=0, column=1, padx=10, pady=2)

    clienText = Label(ClienteScreen, text="CPF", fg="#F5F5F5", bg="#333")
    clienText.grid(row=1, column=1, padx=10, pady=2)

    clienText = Label(ClienteScreen, text="Telefone", fg="#F5F5F5", bg="#333")
    clienText.grid(row=2, column=1, padx=10, pady=2)

    clienWrite = Entry(ClienteScreen, width=20)
    clienWrite.grid(row=0, column=2)

    clienWrite = Entry(ClienteScreen, width=20)
    clienWrite.grid(row=1, column=2)

    clienWrite = Entry(ClienteScreen, width=20)
    clienWrite.grid(row=2, column=2)

    clienButt = BButton(ClienteScreen, text="Adicionar Cliente", command=None)
    clienButt.grid(row=4, column=1, padx=15, pady=20)

    clienButt = BButton(ClienteScreen, text="Atualizar Cliente", command=None)
    clienButt.grid(row=4, column=2, padx=15, pady=20)

def Os2():
    Os2Screen = tk.Toplevel()
    Os2Screen.title("AT9000 OS")
    Os2Screen.config(bg="#333", padx=50, pady=50)

    Os2Butt1 = BButton(Os2Screen, text="Nova Ordem de Serviço", command=NovaOSScreen)
    Os2Butt1.grid(row=1, column=1, pady=5)

    Os2Butt2 = BButton(Os2Screen, text="Abrir Ordem de Serviço", command=AbrirOSScreen)
    Os2Butt2.grid(row=2, column=1, pady=5)

def NovaOSScreen():
    NOsScreen = tk.Toplevel()
    NOsScreen.title("AT9000 Nova OS")
    NOsScreen.config(bg="#333", padx=50, pady=50)

    clientelabel = Label(NOsScreen, text="Selecionar Cliente", fg="#F5F5F5", bg="#333")
    clientelabel.grid(row=0, column=0, padx=10, pady=(2, 10))
    
    clientecombobox = ttk.Combobox(NOsScreen)
    clientecombobox['values'] = [cliente[0] for cliente in Cliente.listaCliente]
    clientecombobox.grid(row=1, column=0, padx=10, pady=2)
    
    tecnicolabel = Label(NOsScreen, text="Selecionar Técnico", fg="#F5F5F5", bg="#333")
    tecnicolabel.grid(row=2, column=0, padx=10, pady=2)

    tecnicocombobox = ttk.Combobox(NOsScreen, state = "readonly")
    tecnicocombobox['values'] = [tec[0] for tec in Tecnico.listaTecnico]
    tecnicocombobox.grid(row=3, column=0, padx=10, pady=2)
    
    descricaolabel = Label(NOsScreen, text="Descrição", fg="#F5F5F5", bg="#333")
    descricaolabel.grid(row=0, column=1, padx=10, pady=(2, 10))
    descricaoentry = Text(NOsScreen, height=10, width=30)
    descricaoentry.grid(row=1, column=1, padx=10, pady=2, rowspan=5)
    
    equipamentolabel = Label(NOsScreen, text="Equipamento", fg="#F5F5F5", bg="#333")
    equipamentolabel.grid(row=6, column=0, padx=10, pady=2)
    equipamentoentry = Entry(NOsScreen)
    equipamentoentry.grid(row=7, column=0, padx=10, pady=2)
    
    def adicionar_equipamento(): # TO DO: mudar funcionamento
        equipamento = equipamentoentry.get()
        equipamentolistbox.insert(END, equipamento)
        equipamentoentry.delete(0, END)
        
    adicionarbutton = BButton(NOsScreen, text="Adicionar", command=adicionar_equipamento)
    adicionarbutton.grid(row=8, column=0, padx=10, pady=2)
    equipamentolistbox = Listbox(NOsScreen)
    equipamentolistbox.grid(row=9, column=0, padx=10, pady=(2, 10))

    #
    # Botão para salvar OS?
    #

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