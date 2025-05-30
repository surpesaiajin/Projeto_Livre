from .produto import Produto

class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma

    def mostrar_produto(self):
        print(f"{self.nome} para {self.plataforma} custa ${self.preco}")
