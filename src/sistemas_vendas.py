from models.produto import Produto
from models.cliente import Cliente
from models.venda import Venda

class SistemaVendas:
    def _init_(self):
        self.produtos = []
        self.clientes = []
        self.vendas = []

    def cadastrar_produto(self, nome, preco, quantidade):
        self.produtos.append(Produto(nome, preco, quantidade))

    def cadastrar_cliente(self, nome, idade, cpf):
        self.clientes.append(Cliente(nome, idade, cpf))

    def vender(self, cpf, nome_produto, quantidade):
        cliente = next((c for c in self.clientes if c.cpf == cpf), None)
        produto = next((p for p in self.produtos if p.nome == nome_produto), None)

        if not cliente or not produto:
            return "Cliente ou produto não encontrado!"
        if produto.quantidade < quantidade:
            return "Estoque insuficiente!"

        produto.quantidade -= quantidade
        venda = Venda(cliente, produto, quantidade)
        self.vendas.append(venda)
        return f"Venda concluída! Total: R${venda.total}"

    def relatorio(self):
        texto = "=== RELATÓRIO ===\n"
        for v in self.vendas:
            texto += f"{v.cliente.nome} comprou {v.quantidade}x {v.produto.nome} - Total: R${v.total}\n"
        return texto
