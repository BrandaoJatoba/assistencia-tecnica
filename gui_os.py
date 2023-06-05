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

