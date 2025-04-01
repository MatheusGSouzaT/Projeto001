import customtkinter
from tkinter import ttk
import sqlite3

def abrir_frame02():
    frame03.grid_forget()
    frame04.grid_forget()
    frame05.grid_forget()
    frame06.grid_forget()
    frame07.grid_forget()
    frame08.grid_forget()
    frame02.grid_propagate(False)
    frame02.grid(row=0, column=1, padx=10)


def abrir_frame03():
    frame04.grid_forget()
    frame02.grid_forget()
    frame05.grid_forget()
    frame06.grid_forget()
    frame07.grid_forget()
    frame08.grid_forget()
    frame03.grid_propagate(False)
    frame03.grid(row=0, column=1, padx=10)
    ler_dados_edicao()

def abrir_frame04():
    frame02.grid_forget()
    frame03.grid_forget()
    frame05.grid_forget()
    frame06.grid_forget()
    frame07.grid_forget()
    frame08.grid_forget()
    frame04.grid_propagate(False)
    frame04.grid(row=0, column=1, padx=10)
    ler_dados_saida()

def adicionar_item():
        global item_vet
        item_vet = str(nome_quantidade_saida.get())
        if item_vet in items:
            item_texto = nome_quantidade_saida.get()
            if item_texto:
                frame_item = customtkinter.CTkFrame(lista_frame)
                frame_item.pack(fill="x", pady=2, padx=5)
                label = customtkinter.CTkLabel(frame_item, text=item_texto, anchor="w")
                label.pack(side="left", fill="x", expand=True, padx=5)
                botao_remover = customtkinter.CTkButton(frame_item, text="🗑", width=30,
                                                        command=lambda: frame_item.destroy())
                botao_remover.pack(side="right", padx=5)
                nome_quantidade_saida.delete(0, "end")


def abrir_frame05():
    frame02.grid_forget()
    frame03.grid_forget()
    frame04.grid_forget()
    frame06.grid_forget()
    frame07.grid_forget()
    frame08.grid_forget()
    frame05.grid_propagate(False)
    frame05.grid(row=0, column=1, padx=10)
    ler_dados_entrada()

def abrir_frame06():
    frame02.grid_forget()
    frame03.grid_forget()
    frame04.grid_forget()
    frame07.grid_forget()
    frame08.grid_forget()
    frame06.grid_propagate(False)
    frame06.grid(row=0, column=1, padx=10)
    ler_dados()

def abrir_frame07():
    frame02.grid_forget()
    frame03.grid_forget()
    frame04.grid_forget()
    frame05.grid_forget()
    frame06.grid_forget()
    frame08.grid_forget()
    frame07.grid_propagate(False)
    frame07.grid(row=0, column=1, padx=10)

def abrir_frame08():
    frame02.grid_forget()
    frame03.grid_forget()
    frame04.grid_forget()
    frame05.grid_forget()
    frame06.grid_forget()
    frame07.grid_forget()
    frame08.grid_propagate(False)
    frame08.grid(row=0, column=1, padx=10)

def open_window():
    pop_up = customtkinter.CTk()
    pop_up.title("Pop-Up")
    pop_up.geometry("500x400")
    escolher_relatorio = customtkinter.CTkLabel(pop_up, text="Escolher relatório(s):", font=("Arial", 20))
    escolher_relatorio.grid(row=0, column=0, padx=30, pady=30)
    escolher_extensao = customtkinter.CTkLabel(pop_up, text="Escolher extensão:", font=("Arial", 20))
    escolher_extensao.grid(row=0, column=1, padx=30, pady=30)

    exportar_estoque = customtkinter.CTkCheckBox(pop_up, text="exportar estoque")
    exportar_estoque.grid(row=1, column=0, pady=20, padx=20, sticky="w")

    exportar_saida = customtkinter.CTkCheckBox(pop_up, text="exportar saida")
    exportar_saida.grid(row=2, column=0, pady=20, padx=20, sticky="w")

    exportar_entrada = customtkinter.CTkCheckBox(pop_up, text="exportar entrada")
    exportar_entrada.grid(row=3, column=0, pady=20, padx=20, sticky="w")

    exportar_word = customtkinter.CTkCheckBox(pop_up, text="Word")
    exportar_word.grid(row=1, column=1, pady=20, padx=20, sticky="w")

    exportar_pdf = customtkinter.CTkCheckBox(pop_up, text="PDF")
    exportar_pdf.grid(row=2, column=1, pady=20, padx=20, sticky="w")

    exportar_EXcel = customtkinter.CTkCheckBox(pop_up, text="Excel")
    exportar_EXcel.grid(row=3, column=1, pady=20, padx=20, sticky="w")

    botao_cancelar_exportar = customtkinter.CTkButton(pop_up, text="Cancelar", fg_color="red", width=80)
    botao_cancelar_exportar.grid(row=4, column=1, sticky="w")

    botao_salvar_exportar = customtkinter.CTkButton(pop_up, text="Salvar", width=80)
    botao_salvar_exportar.grid(row=4, column=1, sticky="e")

    pop_up.mainloop()

def criar_banco():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("CREATE TABLE IF NOT EXISTS produtos (nome text, preco decimal, descricao text, quantidade integer)")
    conexao.commit()
    conexao.close()


def salvar_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    nome_cadastro = entrada_nome.get()
    preco_cadastro = entrada_preco.get()
    quant_cadastro = "0"
    desc_cadastro = entrada_descricao.get("1.0", "end")
    terminal_sql.execute("INSERT INTO produtos VALUES ('"+nome_cadastro+"', '"+quant_cadastro+"', '"+preco_cadastro+"', '"+desc_cadastro+"')")
    conexao.commit()
    conexao.close()


def ler_dados():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT * FROM produtos")
    recebe_dados = terminal_sql.fetchall()



    for item in tree_estoque.get_children():
        tree_estoque.delete(item)

    for i in recebe_dados:
        nome = str(i[0])
        quantidade = str(i[1])
        precos = str(i[2])
        desc = str(i[3])
        tree_estoque.insert("", "end", values=(nome, quantidade, precos, desc))

    conexao.close()

def ler_dados_edicao():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM produtos")
    items_editar = terminal_sql.fetchall()

    def selecionar_item(arq_item):
       conexao = sqlite3.connect("dados.db")
       terminal_sql = conexao.cursor()
       terminal_sql.execute(f"SELECT * FROM produtos WHERE nome= '{arq_item}'")
       receber_dados_produto= terminal_sql.fetchall()
       print(receber_dados_produto)

       nome_produto_editar.insert(0, receber_dados_produto[0][0])
       preco_produto_editar.insert(0, receber_dados_produto[0][2])
       Textbox_editar.insert(0.0, receber_dados_produto[0][3])

    def desmarcar_item():
        nome_produto_editar.delete(0, "end")
        preco_produto_editar.delete(0, "end")
        Textbox_editar.delete(0.0, "end")

    for item in scrollable_frame.winfo_children():
        item.destroy()

    for item in items_editar:
        box = customtkinter.CTkCheckBox(scrollable_frame, text=item)
        box.grid(pady=5, padx=10)
        box.configure(command=lambda nome=item[0], cb=box: (selecionar_item(nome) if cb.get() == 1 else desmarcar_item()))

def ler_dados_saida():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM produtos")
    items = terminal_sql.fetchall()

    def selecionar_item(arq_item):
        conexao = sqlite3.connect("dados.db")
        terminal_sql = conexao.cursor()
        terminal_sql.execute(f"SELECT * FROM produtos WHERE nome= '{arq_item}'")
        receber_dados_produto = terminal_sql.fetchall()
        print(receber_dados_produto)

        nome_quantidade_saida.insert(0, receber_dados_produto[0][0])

    def desmarcar_item():
        nome_quantidade_saida.delete(0, "end")

    for item in lista_frame_saida.winfo_children():
        item.destroy()

    for item in items:
        box_frame_saida = customtkinter.CTkCheckBox(lista_frame_saida, text=item, border_color="blue", border_width=2)
        box_frame_saida.grid(pady=5, padx=10)
        box_frame_saida.configure(command=lambda nome=item[0], cb=box_frame_saida: (selecionar_item(nome) if cb.get() == 1 else desmarcar_item()))


def ler_dados_entrada():
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute("SELECT nome FROM produtos")
    items = terminal_sql.fetchall()

    def selecionar_item(arg_item):
     conexao = sqlite3.connect("dados.db")
     terminal_sql = conexao.cursor()
     terminal_sql.execute(f"SELECT * FROM produtos WHERE nome ='{arg_item}'")
     receber_dados_produto = terminal_sql.fetchall()
     print(receber_dados_produto)

     Nome_produto_entrada.insert(0, receber_dados_produto[0][0])

    def desmarcar_item_saida():
      Nome_produto_entrada.delete(0, "end")

    for item in lista_frame_entrada.winfo_children():
        item.destroy()

    for item in items:
        box_frame_entrada = customtkinter.CTkCheckBox(lista_frame_entrada, text=item, border_color="blue", border_width=2)
        box_frame_entrada.grid(pady=5, padx=10)
        box_frame_entrada.configure(command=lambda nome=item[0], cb=box_frame_entrada: (selecionar_item(nome) if cb.get() == 1 else desmarcar_item_saida()))


def deletar_produto(nome_produto):
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"DELETE FROM produtos WHERE nome = '{nome_produto}'")
    conexao.commit()
    conexao.close()
    nome_produto_editar.delete(0, "end")
    preco_produto_editar.delete(0, "end")
    Textbox_editar.delete(0.0, "end")
    ler_dados_edicao()


def salvar_produto(nome_produto, preco_produto, descricao_produto):
    conexao = sqlite3.connect("dados.db")
    terminal_sql = conexao.cursor()
    terminal_sql.execute(f"UPDATE produtos SET nome = '{nome_produto}', preco = '{preco_produto}', descricao = '{descricao_produto}' WHERE nome = '{nome_produto}'")
    conexao.commit()
    conexao.close()

    nome_produto_editar.delete(0, "end")
    preco_produto_editar.delete(0, "end")
    Textbox_editar.delete(0.0, "end")
    ler_dados_edicao()





criar_banco()


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.title("Nome do Sistema")
janela.geometry("800x400")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview",
                background="#2a2d2e",
                foreground="white",
                rowheight=25,
                fieldbackground="#343638",
                bordercolor="#343638",
                borderwidth=0)
style.map('Treeview', background=[('selected', '#22559b')])

style.configure("Treeview.Heading",
                background="#565b5e",
                foreground="white",
                relief="flat")
style.map("Treeview.Heading",
          background=[('active', '#3484F0')])



frame01 = customtkinter.CTkFrame(janela, width=190, height=400, border_color="#5826EA", border_width=2)
frame01.pack_propagate(False)
frame01.grid(row=0, column=0)

label01_ola = customtkinter.CTkLabel(frame01, text="Nome do Sistema", font=("Arial", 20), text_color="white")
label01_ola.pack(pady=10)


botao01 = customtkinter.CTkButton(frame01, text="Cadastrar", command=abrir_frame02)
botao01.pack(pady=5)

botao02 = customtkinter.CTkButton(frame01, text="Editar", command=abrir_frame03)
botao02.pack(pady=5)

botao03 = customtkinter.CTkButton(frame01, text="Saida", command=abrir_frame04)
botao03.pack(pady=5)

botao04 = customtkinter.CTkButton(frame01, text="Entrada", command=abrir_frame05)
botao04.pack(pady=5)

botao05 = customtkinter.CTkButton(frame01, text="Relatorio", command=abrir_frame06)
botao05.pack(pady=5)


frame02 = customtkinter.CTkFrame(janela, width=590, height=400, border_color="#5826EA", border_width=2)
frame02.grid_propagate(False)
frame02.grid(row=0, column=1, padx=10)

frame03 = customtkinter.CTkFrame(janela, width=590, height=400, border_color="#5826EA", border_width=2)
frame03.grid_propagate(False)


frame04 = customtkinter.CTkFrame(janela, width=590, height=400, border_color="#5826EA", border_width=2)
frame04.grid_propagate(False)

frame05 = customtkinter.CTkFrame(janela, width=590, height=400, border_color="#5826EA", border_width=2)
frame05.grid_propagate(False)

frame06 = customtkinter.CTkFrame(janela, width=590, height=400, border_color="#5826EA", border_width=2)
frame06.grid_propagate(False)

frame07 = customtkinter.CTkFrame(janela, width=590, height=400, border_color="#5826EA", border_width=2)
frame07.grid_propagate(False)

frame08 = customtkinter.CTkFrame(janela, width=590, height=400, border_color="#5826EA", border_width=2)
frame08.grid_propagate(False)

# Frame02 (CADASTRAR)




label02_ola = customtkinter.CTkLabel(frame02, text="Cadastro de Produto", font=("Arial", 20), text_color="white")
label02_ola.grid(row=0, column=1, padx=70,pady=10)

label_nome_produto = customtkinter.CTkLabel(frame02, text="Nome do Produto:")
label_nome_produto.grid(row=1, column=0, stick="w", padx=20)

label_preco = customtkinter.CTkLabel(frame02, text="Preço(R$):")
label_preco.grid(row=2, column=0, stick="e", padx=20)

label_descricao = customtkinter.CTkLabel(frame02, text="Descrição:")
label_descricao.grid(row=3, column=0, stick="ne", padx=20)

entrada_nome = customtkinter.CTkEntry(frame02, placeholder_text="Digite o nome do produto", width=220)
entrada_nome.grid(row=1, column=1, stick="w")

entrada_preco = customtkinter.CTkEntry(frame02, placeholder_text="0,00", width=70)
entrada_preco.grid(row=2, column=1, stick="w")

entrada_descricao = customtkinter.CTkTextbox(frame02, width=220, height=70)
entrada_descricao.grid(row=3, column=1, pady=5, stick="w")

botao_salvar = customtkinter.CTkButton(frame02, text="Salvar", width=100, command=salvar_dados)
botao_salvar.grid(row=5, column=1, pady=5, stick="s")

# Frame 03 (EDITAR)

scrollable_frame = customtkinter.CTkScrollableFrame(frame03)
scrollable_frame.grid(pady=5, padx=20, row=2, column=0, rowspan=5)

label_editar = customtkinter.CTkLabel(frame03, text="\nEditar\n", font=("Arial", 20))
label_editar.grid(row=0, column=1, padx=5)

Buscar_Produto = customtkinter.CTkEntry(frame03, placeholder_text="Buscar Produto:", width=300)
Buscar_Produto.grid(row=1, column=0, padx=50, sticky="w", pady=5, columnspan=3)

nome_produto_editar= customtkinter.CTkEntry(frame03, placeholder_text="nome do produto", width=220)
nome_produto_editar.grid(row=2, column=1, pady=5, sticky="w", columnspan=3)

preco_produto_editar = customtkinter.CTkEntry(frame03, placeholder_text="0,00", width=70)
preco_produto_editar.grid(row=3, column=1,pady=5, sticky="w", columnspan=3)

Textbox_editar = customtkinter.CTkTextbox(frame03, width=300, height=100)
Textbox_editar.grid(row=4, column=1, pady=5, sticky="w", columnspan=3)

botao_excluir = customtkinter.CTkButton(frame03, text="Excluir", width=80,
                                        command=lambda: deletar_produto(nome_produto_editar.get()))
botao_excluir.grid(row=5, column=1, pady=5)

botao_cancelar_editar = customtkinter.CTkButton(frame03, text="Cancelar", width=80)
botao_cancelar_editar.grid(row=5, column=2, pady=5)

botao_salvar_editar = customtkinter.CTkButton(frame03, text="Salvar", width=80, fg_color="#013ADF",
                                              command=lambda: salvar_produto(nome_produto_editar.get(), preco_produto_editar.get(), Textbox_editar.get(0.0, "end")))
botao_salvar_editar.grid(row=5, column=3, pady=5)

# Frame04(SAIDA)

label_saida = customtkinter.CTkLabel(frame04, text="Saida de Produto", font=("Arial", 20))
label_saida.grid(row=0, column=1, padx=20, pady=20)

root = customtkinter.CTk()
root.geometry("580x380")

lista_frame_saida = customtkinter.CTkScrollableFrame(frame04, border_width=2, border_color="#6447E6")
lista_frame_saida.grid(row=2, column=0, pady=5, padx=5, stick="w", rowspan=6)

items = ["item 1", "item 2",  "item 3",  "item 4",  "item 5",  "item 6",  "item 7",  "item 8"]

for item in items:
    box_frame_saida = customtkinter.CTkCheckBox(lista_frame_saida, text=item, border_color="blue", border_width=2)
    box_frame_saida.grid(pady=5, padx=10, stick="se")

campo_busca_saida= customtkinter.CTkEntry(frame04, placeholder_text="Campo de Busca:", width=220, border_color="#6447E6")
campo_busca_saida.grid(row=1, column=0, stick="w", padx=5)

nome_quantidade_saida = customtkinter.CTkEntry(frame04, placeholder_text="Nome e quantidade:", width=220, border_color="#6447E6")
nome_quantidade_saida.grid(row=1, column=1)

valor_saida = customtkinter.CTkEntry(frame04, placeholder_text="", border_color="#6447E6", width=105, height=30)
valor_saida.grid(padx=5, row=2, column=1, columnspan=3, stick="w")

botao_adicionar = customtkinter.CTkButton(frame04, text="Adicionar Item", width=105, height=30,
                                          command=adicionar_item)
botao_adicionar.grid(pady=5, row=2, column=1, sticky="e", padx=5)

botao_cancelar_saida = customtkinter.CTkButton(frame04, text="Cancelar", width=80, height=30)
botao_cancelar_saida.grid(row=4, column=1, sticky="w")

botao_salvar_saida = customtkinter.CTkButton(frame04, text="Salvar", width=80, height=30, fg_color="blue")
botao_salvar_saida.grid(row=4, column=1, sticky="e")

lista_frame = customtkinter.CTkFrame(frame04, width=220, height=180)
lista_frame.grid(padx=5, pady=5, row=3, column=1, stick="snwe")

# Frame05 (Entrada)


label_entrada = customtkinter.CTkLabel(frame05, text="Entrada do Produto", font=("Arial", 20))
label_entrada.grid(row=0, column=1, padx=20, pady=20)

root = customtkinter.CTk()
root.geometry("580x380")

lista_frame_entrada = customtkinter.CTkScrollableFrame(frame05, border_width=2, border_color="#6447E6")
lista_frame_entrada.grid(row=2, column=0, pady=5, padx=5, stick="w", rowspan=2)


campo_busca_entrada = customtkinter.CTkEntry(frame05, placeholder_text="Campo de Busca:", width=220, border_color="#6447E6")
campo_busca_entrada.grid(row=1, column=0, stick="w", padx=5)

Nome_produto_entrada = customtkinter.CTkEntry(frame05, placeholder_text="Nome e quantidade:", width=220, border_color="#6447E6")
Nome_produto_entrada.grid(row=1, column=1)

valor_saida_entrada = customtkinter.CTkEntry(frame05, placeholder_text="", border_color="#6447E6", width=105, height=30)
valor_saida_entrada.grid(padx=5, row=2, column=1, columnspan=3, stick="w")

botao_adicionar_entrada = customtkinter.CTkButton(frame05, text="Adicionar Item", width=105, height=30,
                                          command=adicionar_item)
botao_adicionar_entrada.grid(pady=5, row=2, column=1, sticky="e", padx=5)

botao_cancelar_entrada = customtkinter.CTkButton(frame05, text="Cancelar", width=80, height=30)
botao_cancelar_entrada.grid(row=4, column=1, sticky="w")

botao_salvar_entrada = customtkinter.CTkButton(frame05, text="Salvar", width=80, height=30, fg_color="blue")
botao_salvar_entrada.grid(row=4, column=1, sticky="e")

lista_frame = customtkinter.CTkFrame(frame05, width=220, height=180)
lista_frame.grid(padx=5, pady=5, row=3, column=1, stick="nw")



# Frame06 (Relatorio)

label_relatorio = customtkinter.CTkLabel(frame06, text="Relatorio Estoque", font=("Arial", 20))
label_relatorio.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

pesquisar_estoque = customtkinter.CTkEntry(frame06, placeholder_text="Pesquisar:", width=200, border_color="#6447E6", border_width=2)
pesquisar_estoque.grid(row=1, column=0, pady=0, padx=30)

colunas=["produtos", "quantidade", "preço", "descrição"]

tree_estoque = ttk.Treeview(frame06, columns=colunas, show="headings", height=10)
tree_estoque.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

tree_estoque.heading("produtos", text="produtos")
tree_estoque.heading("quantidade", text="quantidade")
tree_estoque.heading("preço", text="preço")
tree_estoque.heading("descrição", text="Descrição")
tree_estoque.column("produtos", width=120, anchor="center")
tree_estoque.column("quantidade", width=120, anchor="center")
tree_estoque.column("preço", width=120, anchor="center")



botao_exportar = customtkinter.CTkButton(frame06, text="Exportar", width=80, command=open_window)
botao_exportar.grid(row=1, column=3, pady=0,)

botao_estoque = customtkinter.CTkButton(frame06, text="Estoque", width=80, command=abrir_frame06)
botao_estoque.grid(row=3, column=1, padx=10)

botao_saida = customtkinter.CTkButton(frame06, text="Saida", width=80, command=abrir_frame07)
botao_saida.grid(row=3, column=2, padx=10)

botao_entrada = customtkinter.CTkButton(frame06, text="Entrada", width=80, command=abrir_frame08)
botao_entrada.grid(row=3, column=3, padx=10)

# Frame07 (Saida)

label_estoque3 = customtkinter.CTkLabel(frame07, text="Saida Estoque", font=("Arial", 20))
label_estoque3.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

entrada_estoque = customtkinter.CTkEntry(frame07, placeholder_text="Pesquisar:", width=200, border_color="#6447E6", border_width=2)
entrada_estoque.grid(row=1, column=0, pady=0, padx=30)



colunas=["nome", "quantidade", "data/hora"]

tree_saida = ttk.Treeview(frame07, columns=colunas, show="headings", height=10)
tree_saida.grid(row=2, column=0, columnspan=4, padx=50, pady=5)

for coluna in colunas:
    tree_saida.heading(coluna, text=coluna)
    tree_saida.column(coluna, width=160)


botao13 = customtkinter.CTkButton(frame07, text="Exportar", width=80, command=open_window)
botao13.grid(row=1, column=3, pady=0,)

botao14 = customtkinter.CTkButton(frame07, text="Estoque", width=80, command=abrir_frame06)
botao14.grid(row=3, column=1)

botao15 = customtkinter.CTkButton(frame07, text="Saida", width=80, command=abrir_frame07)
botao15.grid(row=3, column=2)

botao16 = customtkinter.CTkButton(frame07, text="Entrada", width=80, command=abrir_frame08)
botao16.grid(row=3, column=3)

# Frame08 (Entrada)

label_estoque6 = customtkinter.CTkLabel(frame08, text="Entrada Estoque", font=("Arial", 20))
label_estoque6.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

entrada_estoque7 = customtkinter.CTkEntry(frame08, placeholder_text="Pesquisar:", width=200, border_color="#6447E6", border_width=2)
entrada_estoque7.grid(row=1, column=0, pady=0, padx=30)


colunas=["nome", "quantidade", "data/hora"]

tree_entrada = ttk.Treeview(frame08, columns=colunas, show="headings", height=10)
tree_entrada.grid(row=2, column=0, columnspan=4, padx=50, pady=5)

for coluna in colunas:
    tree_entrada.heading(coluna, text=coluna)
    tree_entrada.column(coluna, width=160)


botao17 = customtkinter.CTkButton(frame08, text="Exportar", width=80, command=open_window)
botao17.grid(row=1, column=3, pady=0,)

botao18 = customtkinter.CTkButton(frame08, text="Estoque", width=80, command=abrir_frame06)
botao18.grid(row=3, column=1)

botao19 = customtkinter.CTkButton(frame08, text="Saida", width=80, command=abrir_frame07)
botao19.grid(row=3, column=2)

botao20 = customtkinter.CTkButton(frame08, text="Entrada", width=80, command=abrir_frame08)
botao20.grid(row=3, column=3)






janela.mainloop()