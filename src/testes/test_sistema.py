import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sistema_vendas import SistemaVendas

def test_cadastro_produto():
    s = SistemaVendas()
    s.cadastrar_produto("Camiseta", 50, 10)
    assert len(s.produtos) == 1

def test_venda_sucesso():
    s = SistemaVendas()
    s.cadastrar_cliente("João", 30, "111")
    s.cadastrar_produto("Tênis", 200, 5)
    msg = s.vender("111", "Tênis", 1)
    assert "Venda concluída" in msg

def test_venda_falha():
    s = SistemaVendas()
    s.cadastrar_cliente("João", 30, "111")
    s.cadastrar_produto("Tênis", 200, 5)
    msg = s.vender("111", "Tênis", -1)
    assert "Venda concluída" not in msg
