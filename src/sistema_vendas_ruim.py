# Sistema de vendas bagunçado, maior e com mais funcionalidades

produtos = []
vendas = []
clientes = []
fornecedores = []
promocoes = []

# Cadastro de produtos
def cad_prod(n, p, q):
    prod = {}
    prod['n'] = n           # ❌ chave abreviada, pouco legível
    prod['p'] = p           # ❌ chave abreviada
    prod['q'] = q           # ❌ chave abreviada
    produtos.append(prod)    # ❌ lista global, sem encapsulamento
    print(f"Produto '{n}' cadastrado!")  # ❌ print dentro da lógica

# Cadastro de clientes
def cad_cli(n, i, c):
    cli = {}
    cli['n'] = n
    cli['i'] = i
    cli['c'] = c
    clientes.append(cli)    # ❌ lista global
    print(f"Cliente '{n}' cadastrado!")  # ❌ print dentro da função

# Cadastro de fornecedores
def cad_fornecedor(nome, cnpj):
    f = {}
    f['nome'] = nome
    f['cnpj'] = cnpj
    fornecedores.append(f)  # ❌ lista global, sem validação
    print(f"Fornecedor '{nome}' cadastrado!")

# Cadastro de promoções
def cad_promocao(produto_nome, desconto):
    promo = {'produto': produto_nome, 'desconto': desconto}
    promocoes.append(promo)  # ❌ lista global, sem verificação de duplicidade
    print(f"Promoção adicionada: {produto_nome} com {desconto}% de desconto")

# Buscar cliente
def acha_cli(cpf):
    for c in clientes:
        if c['c'] == cpf:
            return c
    print("Cliente não encontrado")  # ❌ mistura lógica com print
    return None

# Buscar produto
def acha_prod(nome):
    for p in produtos:
        if p['n'] == nome:
            return p
    print("Produto não encontrado")  # ❌ mistura lógica com print
    return None

# Obter desconto de produto
def obter_desconto(nome_prod):
    for promo in promocoes:
        if promo['produto'] == nome_prod:
            return promo['desconto']
    return 0  # ❌ sem tratamento de casos inválidos

# Venda
def vende(cpf, nome_prod, qtd):
    c = acha_cli(cpf)
    if not c:
        print("Cliente não existe")
        return

    p = acha_prod(nome_prod)
    if not p:
        print("Produto não existe")
        return

    if qtd <= 0:
        print("Quantidade inválida")
        return

    if p['q'] < qtd:
        print("Sem estoque suficiente")
        return

    desconto = obter_desconto(nome_prod)
    total = p['p'] * qtd * (1 - desconto/100)

    v = {}
    v['cli'] = c['n']          # ❌ chave abreviada
    v['prod'] = p['n']         # ❌ chave abreviada
    v['q'] = qtd
    v['total'] = total
    v['desconto'] = desconto
    vendas.append(v)           # ❌ mistura lógica com persistência

    p['q'] -= qtd               # ❌ altera estoque direto, sem controle
    print(f"Venda realizada: {c['n']} comprou {qtd} {p['n']} com {desconto}% de desconto - Total: R${total:.2f}")

# Relatório gigante
def relatorio():
    print("----- PRODUTOS -----")
    for p in produtos:
        print(f"{p['n']} - {p['q']} unidades - R$ {p['p']:.2f}")  # ❌ f-strings ajudam mas listas globais tornam frágil
    print("----- CLIENTES -----")
    for c in clientes:
        print(f"{c['n']} - CPF: {c['c']} - Idade: {c['i']}")
    print("----- FORNECEDORES -----")
    for f in fornecedores:
        print(f"{f['nome']} - CNPJ: {f['cnpj']}")
    print("----- PROMOÇÕES -----")
    for promo in promocoes:
        print(f"{promo['produto']} com {promo['desconto']}% de desconto")
    print("----- VENDAS -----")
    for v in vendas:
        print(f"{v['cli']} comprou {v['q']} {v['prod']} - Desconto: {v['desconto']}% - Total: R${v['total']:.2f}")
    print("----- TOTAL DE ESTOQUE -----")
    total_estoque = sum([p['q'] for p in produtos])  # ❌ cálculo manual, poderia ser função
    print("Total em estoque:", total_estoque)

# Relatório de vendas por cliente
def vendas_por_cliente(cpf):
    c = acha_cli(cpf)
    if not c:
        print("Cliente não existe")
        return
    print(f"--- Vendas de {c['n']} ---")
    for v in vendas:
        if v['cli'] == c['n']:
            print(f"{v['q']} {v['prod']} - Total: R${v['total']:.2f} - Desconto: {v['desconto']}%")  # ❌ repetição de lógica

# Atualizar preço
def atualizar_preco(nome_prod, novo_preco):
    p = acha_prod(nome_prod)
    if not p:
        print("Produto não encontrado")
        return
    p['p'] = novo_preco
    print(f"Preço de {nome_prod} atualizado para R${novo_preco:.2f}")  # ❌ print dentro da função

# Funções inúteis
def clientes_adultos():
    for c in clientes:
        if c['i'] >= 18:
            print(c['n'], "é maior de idade")  # ❌ função inútil e repetitiva

def produtos_em_promocao():
    for promo in promocoes:
        print(f"{promo['produto']} está em promoção com {promo['desconto']}% de desconto")  # ❌ repetição

# Exemplo de uso bagunçado
cad_prod("Camiseta", 50, 10)
cad_prod("Tênis", 200, 5)
cad_prod("Boné", 30, 8)

cad_cli("João", 30, "111")
cad_cli("Maria", 25, "222")
cad_cli("Pedro", 17, "333")

cad_fornecedor("Fornecedor A", "12345678000199")
cad_fornecedor("Fornecedor B", "98765432000188")

cad_promocao("Camiseta", 10)
cad_promocao("Boné", 20)

vende("111", "Camiseta", 2)
vende("222", "Tênis", 1)
vende("111", "Tênis", 10)  # ❌ sem tratamento adequado
vende("333", "Boné", 1)

relatorio()
clientes_adultos()
produtos_em_promocao()
vendas_por_cliente("111")
atualizar_preco("Tênis", 180)
relatorio()
