from .bancoSqlite import BancoDeDados
from modelos.console import Console
from modelos.controle import Controle
from modelos.jogo import Jogo
from modelos.produto import Produto


class Loja:

    def __init__(self,nome_banco):
        self.banco_de_dados = BancoDeDados(nome_banco)


    def adicionar_produto(self):
        tipos_validos = ['console', 'controle', 'jogo']
        
        while True:
            print("Que tipo de produto deseja adicionar? (Console / Controle / Jogo)")
            tipo = input("Tipo: ").strip().lower()

            if tipo not in tipos_validos:
                print("Tipo inválido. Tente novamente.\n")
                continue  # volta ao início do loop

            nome = input("Qual o nome do produto? ").strip()
            if not nome:
                print("Nome não pode estar em branco.\n")
                continue

            try:
                preco = float(input("Qual o preço do produto? ").strip())
            except ValueError:
                print("Preço inválido. Digite um número (ex: 299.99).\n")
                continue

            # Pegando atributos específicos por tipo
            if tipo == 'console':
                armazenamento = input("Armazenamento (ex: 1TB): ").strip()
                if not armazenamento:
                    print("Armazenamento não pode estar vazio.\n")
                    continue
                produto = Console(nome, preco, armazenamento)

            elif tipo == 'controle':
                compatibilidade = input("Compatível com qual console? ").strip()
                if not compatibilidade:
                    print("Compatibilidade não pode estar vazia.\n")
                    continue
                produto = Controle(nome, preco, compatibilidade)

            elif tipo == 'jogo':
                plataforma = input("Plataforma (ex: PS5, Xbox): ").strip()
                if not plataforma:
                    print("Plataforma não pode estar vazia.\n")
                    continue
                produto = Jogo(nome, preco, plataforma)

            self.banco_de_dados.inserir_produto(produto)
            print(f"Produto '{nome}' adicionado com sucesso!\n")
            break  # sai do loop após sucesso

    def excluir_produto(self):
        while True:
            nome = input("Qual o nome do produto que deseja excluir? ").strip()
            
            if not nome:
                print("Nome não pode estar em branco.\n")
                continue
            
            # Tenta excluir o produto no banco de dados
            sucesso = self.banco_de_dados.excluir_por_nome(nome)
            
            if sucesso:
                print(f"Produto '{nome}' excluído com sucesso!\n")
                break
            else:
                print(f"Nenhum produto encontrado com o nome '{nome}'. Tente novamente.\n")

    def visualizar_produtos(self):
        tipos_validos = ['Console', 'Controle', 'Jogo']
        
        while True:
            print("Qual tipo de produto deseja visualizar? (Console / Controle / Jogo)")
            tipo = input("Tipo: ").strip().capitalize()

            if tipo not in tipos_validos:
                print("Tipo inválido. Tente novamente.\n")
                continue

            produtos = self.banco_de_dados.listar_formatado_por_tipo(tipo)

            if not produtos:
                print(f"Não há produtos do tipo '{tipo}'.\n")
            else:
                print(f"\nProdutos do tipo '{tipo}':")
                for produto in produtos:
                    print(produto)
                print()  # linha em branco após a lista

            break
