class Venda:
    def __init__(self, cliente, produto, quantidade):
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.total = produto.preco * quantidade