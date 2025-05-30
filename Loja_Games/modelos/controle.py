from .produto import Produto

class Controle(Produto):
    def __init__(self, nome, preco, compatibilidade):
        super().__init__(nome, preco)
        self.compatibilidade = compatibilidade

    def mostrar_produto(self):
        print(f"{self.nome} compativel com {self.compatibilidade} custa ${self.preco}")