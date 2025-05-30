from .produto import Produto


class Console(Produto):
    def __init__(self, nome, preco, armazenamento):
        super().__init__(nome, preco)
        self.armazenamento = armazenamento

    def mostrar_produto(self):
        print(f"{self.nome} custa ${self.preco} e possui {self.armazenamento} de armazenamento")