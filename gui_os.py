from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from cliente import Cliente
from tecnico import Tecnico
from ordemServico import OrdemServico
from especialidade import Especialidade
from status import Status

OS_EXEMPLO = {
        'os_id'         : 2,
        'cliente'       : "Fulano",
        'tecnico'       : "Cicrano",
        'status'        : Status.ABERTO,
        'equipamento'   : "S/N - 00122999120. Computador i5 8gb ram rtx 3200. Problemas no boot.",
        'comentario'    : ["01/06/2023 - OS aberta", "02/06/2023 - Testes de boot"]       
        }

def BButton(master, text, command):
    style = ttk.Style()
    style.configure("RoundedButton.TButton", relief=RIDGE, background="#333", foreground="#333")
    button = ttk.Button(master, text=text, style="RoundedButton.TButton", command=command)
    return button

def ViewOS():
    def NewComentScreen():
        NewComentScreen = tk.Toplevel()
        NewComentScreen.title("AT9000 Novo Comentario")
        NewComentScreen.config(bg="#333", padx=25, pady=25)

        NCLabel = Label(NewComentScreen, text="Comentário", fg="#F5F5F5", bg="#333")
        NCLabel.grid(row=0, column=0, padx=10, pady=2, sticky=N)

        NCEntry = Text(NewComentScreen, height=10 ,width=30)
        NCEntry.grid(row=0, column=1, padx=10, pady=2, sticky=S)

        NCButton = BButton(NewComentScreen, text=("Adicionar Comentário"), command=None)
        NCButton.grid(row=1, column=1, padx=10, pady=2, sticky=W)

    def AttScreen():
        AttScreen = tk.Toplevel()
        AttScreen.title("AT9000 Atualizar Status")
        AttScreen.config(bg="#333", padx=25, pady=25)

        StatusLabel = Label(AttScreen, text="Status", fg="#F5F5F5", bg="#333")
        StatusLabel.grid(row=0, column=0, padx=10, pady=2)

        StatusComboBox = ttk.Combobox(AttScreen)
        # Joia
        StatusComboBox.grid(row=0, column=1, padx=10, pady=2)

        StatusButton = BButton(AttScreen, text="Atualizar", command=None)
        StatusButton.grid(row=1, column=1, padx=10, pady=2)

    ViewOSScreen = Tk()
    ViewOSScreen.title("AT9000 Visualizar OS")
    ViewOSScreen.config(bg="#333", padx=50, pady=50)
    
    CodigoLabel = Label(ViewOSScreen, text="Código :", fg="#F5F5F5", bg="#333")
    CodigoText = Label(ViewOSScreen, text=OS_EXEMPLO["os_id"], fg="#F5F5F5", bg="#333")
    CodigoLabel.grid(row=0, column=0, padx=10, pady=2, sticky=W)
    CodigoText.grid(row=0, column=1, padx=10, pady=2, sticky=W)

    TecnicoLabel = Label(ViewOSScreen, text="Técnico :", fg="#F5F5F5", bg="#333")
    TecnicoText = Label(ViewOSScreen, text=OS_EXEMPLO["tecnico"], fg="#F5F5F5", bg="#333")
    TecnicoLabel.grid(row=0, column=3, padx=10, pady=2, sticky=E)
    TecnicoText.grid(row=0, column=4, padx=10, pady=2, sticky=W)

    ClienteLabel = Label(ViewOSScreen, text="Cliente :", fg="#F5F5F5", bg="#333")
    ClienteText = Label(ViewOSScreen, text=OS_EXEMPLO["cliente"], fg="#F5F5F5", bg="#333")
    ClienteLabel.grid(row=1, column=0, padx=10, pady=2, sticky=W)
    ClienteText.grid(row=1, column=1, padx=10, pady=2, sticky=W)

    StatusLabel = Label(ViewOSScreen, text="Status :", fg="#F5F5F5", bg="#333")
    StatusText = Label(ViewOSScreen, text=OS_EXEMPLO["status"], fg="#F5F5F5", bg="#333")
    StatusLabel.grid(row=1, column=3, padx=10, pady=2, sticky=E)
    StatusText.grid(row=1, column=4, padx=10, pady=2, sticky=W)

    Divisiao = Label(ViewOSScreen, text="     ", fg="#F5F5F5", bg="#333")
    Divisiao.grid(row=2, column=3, padx=10, pady=10)

    EquipamentoLabel = Label(ViewOSScreen, text="Equipamento :", fg="#F5F5F5", bg="#333")
    EquipamentoText = Label(ViewOSScreen, text=OS_EXEMPLO["equipamento"], fg="#F5F5F5", bg="#333")
    EquipamentoLabel.grid(row=3, column=0, padx=10, pady=2, sticky=W)
    EquipamentoText.grid(row=3, column=1, padx=10, pady=2, sticky=W)

    ComentariosLabel = Label(ViewOSScreen, text="Comentários :", fg="#F5F5F5", bg="#333")
    ComentariosLabel.grid(row=4, column=0, padx=10, pady=2, sticky=W)
    comentarios = OS_EXEMPLO["comentario"]
    ComentariosText = Text(ViewOSScreen, fg="#F5F5F5", bg="#333")
    ComentariosText.grid(row=5, column=1, padx=10, pady=2, sticky=W)
    for comentario in comentarios:
        ComentariosText.insert(END, comentario + "\n")

    NewComentButton = BButton(ViewOSScreen, text=("Adicionar Comentário"), command=NewComentScreen)
    NewComentButton.grid(row=6, column=1, padx=10, pady=2, sticky=W)

    AttButton = BButton(ViewOSScreen, text=("Atualizar Status"), command=AttScreen)
    AttButton.grid(row=6, column=1, padx=10, pady=2, sticky=E)

    ViewOSScreen.mainloop()

if __name__ == "__main__":
    ViewOS()
