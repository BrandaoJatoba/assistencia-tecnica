from tkinter import *
from tkinter import ttk

#PlaceHolder
ListaDeProduto = [1, 2, 3, 4, 5]
ListaDeClientes = ["João", "Maria", "José", "Ana", "Carlos"]
ListaDeTecnicos = ["Jorge", "Marcelo", "Josepha", "Carla"]
#PlaceHolder

def ProdAppend():
    novo_produto = addProd.get()
    ListaDeProduto.append(novo_produto)
    listaProduto.delete(0, END)
    for n in ListaDeProduto:
        listaProduto.insert(END, str(n))
    addProd.delete(0, END)
def ProdRemove():
    listaProduto.delete(ANCHOR)
    ListaDeProduto.clear()
    for n in range(listaProduto.size()):
        item = listaProduto.get(n)
        ListaDeProduto.append(item)
def ClieteAppend():
    novo_cliente = addCliente.get()
    ListaDeClientes.append(novo_cliente)
    listaClientes.delete(0, END)
    for n in  ListaDeClientes:
        listaClientes.insert(END, str(n))
    addCliente.delete(0, END)
def ClienteRemove():
    listaClientes.delete(ANCHOR)
    ListaDeClientes.clear()
    for n in range(listaClientes.size()):
        item = listaClientes.get(n)
        ListaDeClientes.append(item)
def TecnicoAppend():
    novo_tecnico = addTecnico.get()
    ListaDeTecnicos.append(novo_tecnico)
    listaTecnico.delete(0, END)
    for t in ListaDeTecnicos:
        listaTecnico.insert(END, str(t))
    addTecnico.delete(0, END)
def TecnicoRemove():
    listaTecnico.delete(ANCHOR)
    ListaDeTecnicos.clear()
    for n in range(listaTecnico.size()):
        item = listaTecnico.get(n)
        ListaDeTecnicos.append(item)


if __name__ == "__main__":
    janela = Tk()
    janela.title("Assistencia Tecnica")
    janela.config(bg="#F5F5F5", padx=20, pady=20)

    # Produto
    addProd = Entry(width=20, font=("Arial", 14))
    addProd.grid(row=1, column=1, pady=10)
    bttProduto = ttk.Button(janela, text="Adicionar", command=ProdAppend)
    bttProduto.grid(row=1, column=2, pady=10)
    bttRemoverProduto = ttk.Button(janela, text="Remover", command=ProdRemove)
    bttRemoverProduto.grid(row=3, column=1, pady=10)
    nomeProduto = Label(text="Adicionar Produto", font=("Arial", 20), fg="#333", bg="#F5F5F5")
    nomeProduto.grid(row=0, column=1, pady=20)
    listaProduto = Listbox(janela, height=5, font=("Arial", 14))
    for n in ListaDeProduto:
        listaProduto.insert(END, str(n))
    listaProduto.grid(row=2, column=0, columnspan=2, pady=10)

    # Cliente
    addCliente = Entry(width=20, font=("Arial", 14))
    addCliente.grid(row=1, column=10, pady=10)
    bttCliente = ttk.Button(janela, text="Adicionar", command=ClieteAppend)
    bttCliente.grid(row=1, column=11, pady=10)
    bttRemoverCliente = ttk.Button(janela, text="Remover", command=ClienteRemove)
    bttRemoverCliente.grid(row=3, column=10, pady=10)
    nomeCliente = Label(text="Adicionar Cliente", font=("Arial", 20), fg="#333", bg="#F5F5F5")
    nomeCliente.grid(row=0, column=10, pady=20)
    listaClientes = Listbox(janela, height=5, font=("Arial", 14))
    for n in ListaDeClientes:
        listaClientes.insert(END, str(n))
    listaClientes.grid(row=2, column=9, columnspan=2, pady=10)

    #Tecnico
    addTecnico = Entry(width=20, font=("Arial", 14))
    addTecnico.grid(row=1, column=18, pady=10)
    bttTecnico = ttk.Button(janela, text="Adicionar", command=TecnicoAppend)
    bttTecnico.grid(row=1, column=19, pady=10)
    bttRemoverTecnico = ttk.Button(janela, text="Remover", command=TecnicoRemove)
    bttRemoverTecnico.grid(row=3, column=18, pady=10)
    nomeTecnico = Label(text="Adicionar Técnico", font=("Arial", 20), fg="#333", bg="#F5F5F5")
    nomeTecnico.grid(row=0, column=18, pady=20)
    listaTecnico = Listbox(janela, height=5, font=("Arial", 14))
    for t in ListaDeTecnicos:
        listaTecnico.insert(END, str(t))
    listaTecnico.grid(row=2, column=17, columnspan=2, pady=10)




    janela.mainloop()
