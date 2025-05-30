class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco =  preco
    
    def mostrar_produto(self):
        print(f"{self.nome} custa ${self.preco}")

    def aplicar_desconto(self, desconto: str):
        desconto = float(desconto.strip('%')) / 100
        self.preco *= 1 - desconto
