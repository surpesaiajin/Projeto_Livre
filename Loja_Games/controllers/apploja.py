from .bancoSqlite import BancoDeDados
from modelos.console import Console
from modelos.controle import Controle
from modelos.jogo import Jogo
from modelos.produto import Produto
from .loja import Loja


import tkinter as tk
from tkinter import messagebox, simpledialog, ttk

class LojaGUI:
    def __init__(self, loja):
        self.loja = loja
        self.root = tk.Tk()
        self.root.title("Loja de Produtos")

        # Botões principais
        tk.Button(self.root, text="Adicionar Produto", width=20, command=self.adicionar_produto).pack(pady=5)
        tk.Button(self.root, text="Visualizar Produtos", width=20, command=self.visualizar_produtos).pack(pady=5)
        tk.Button(self.root, text="Excluir Produto", width=20, command=self.excluir_produto).pack(pady=5)

    def adicionar_produto(self):
        tipos = ['Console', 'Controle', 'Jogo']
        tipo = simpledialog.askstring("Adicionar Produto", "Tipo (Console / Controle / Jogo):")
        if tipo is None:
            return
        tipo = tipo.capitalize()
        if tipo not in tipos:
            messagebox.showerror("Erro", "Tipo inválido.")
            return

        nome = simpledialog.askstring("Adicionar Produto", "Nome do produto:")
        if not nome:
            messagebox.showerror("Erro", "Nome não pode estar vazio.")
            return

        preco_str = simpledialog.askstring("Adicionar Produto", "Preço do produto:")
        try:
            preco = float(preco_str)
        except:
            messagebox.showerror("Erro", "Preço inválido.")
            return

        if tipo == 'Console':
            armazenamento = simpledialog.askstring("Adicionar Produto", "Armazenamento (ex: 1TB):")
            if not armazenamento:
                messagebox.showerror("Erro", "Armazenamento não pode estar vazio.")
                return
            produto = Console(nome, preco, armazenamento)
        elif tipo == 'Controle':
            compatibilidade = simpledialog.askstring("Adicionar Produto", "Compatibilidade (ex: PS5):")
            if not compatibilidade:
                messagebox.showerror("Erro", "Compatibilidade não pode estar vazia.")
                return
            produto = Controle(nome, preco, compatibilidade)
        else:  # Jogo
            plataforma = simpledialog.askstring("Adicionar Produto", "Plataforma (ex: PS5):")
            if not plataforma:
                messagebox.showerror("Erro", "Plataforma não pode estar vazia.")
                return
            produto = Jogo(nome, preco, plataforma)

        self.loja.banco_de_dados.inserir_produto(produto)
        messagebox.showinfo("Sucesso", f"Produto '{nome}' adicionado!")

    def visualizar_produtos(self):
        tipos = ['Console', 'Controle', 'Jogo']
        tipo = simpledialog.askstring("Visualizar Produtos", "Tipo (Console / Controle / Jogo):")
        if tipo is None:
            return
        tipo = tipo.capitalize()
        if tipo not in tipos:
            messagebox.showerror("Erro", "Tipo inválido.")
            return

        produtos = self.loja.banco_de_dados.listar_formatado_por_tipo(tipo)
        if not produtos:
            messagebox.showinfo("Produtos", f"Não há produtos do tipo '{tipo}'.")
            return

        janela = tk.Toplevel(self.root)
        janela.title(f"Produtos do tipo {tipo}")

        text = tk.Text(janela, width=80, height=20)
        text.pack(padx=10, pady=10)
        text.insert(tk.END, "\n".join(produtos))
        text.config(state=tk.DISABLED)

    def excluir_produto(self):
        nome = simpledialog.askstring("Excluir Produto", "Nome do produto para excluir:")
        if not nome:
            messagebox.showerror("Erro", "Nome não pode estar vazio.")
            return

        sucesso = self.loja.banco_de_dados.excluir_por_nome(nome)
        if sucesso:
            messagebox.showinfo("Sucesso", f"Produto '{nome}' excluído.")
        else:
            messagebox.showinfo("Falha", f"Nenhum produto encontrado com o nome '{nome}'.")

    def run(self):
        self.root.mainloop()
