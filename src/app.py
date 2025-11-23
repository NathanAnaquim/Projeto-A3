import sys
import os
from flask import Flask, render_template, request, redirect

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sistema_vendas import SistemaVendas

app = Flask(__name__)
sistema = SistemaVendas()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos', methods=['GET', 'POST'])
def produtos():
    if request.method == 'POST':
        nome = request.form['nome']
        preco = request.form['preco']
        quantidade = request.form['quantidade']

        #Nome não pode ter números 
        if any(char.isdigit() for char in nome):
            return render_template('produtos.html', produtos=sistema.produtos,
                                   msg="O nome do produto não pode conter números.")

        #Preço deve ser número
        try:
            preco = float(preco)
            if preco <= 0:
                raise ValueError
        except ValueError:
            return render_template('produtos.html', produtos=sistema.produtos,
                                   msg="Preço inválido! Digite um número maior que zero.")

        #Quantidade deve ser inteira positiva 
        try:
            quantidade = int(quantidade)
            if quantidade <= 0:
                raise ValueError
        except ValueError:
            return render_template('produtos.html', produtos=sistema.produtos,
                                   msg="Quantidade inválida. Digite um número inteiro positivo.")

        # Cadastro OK
        sistema.cadastrar_produto(nome, preco, quantidade)
        return redirect('/produtos')

    return render_template('produtos.html', produtos=sistema.produtos)


@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        cpf = request.form['cpf']

        # Validação nome
        if not nome.replace(" ", "").isalpha():
            return render_template('clientes.html', clientes=sistema.clientes,
                                   msg="Nome inválido! Use apenas letras.")

        # Validação idade
        if idade <= 0:
            return render_template('clientes.html', clientes=sistema.clientes,
                                   msg="Idade deve ser maior que zero.")

        # Validação CPF
        if not cpf.isdigit() or len(cpf) != 11:
            return render_template('clientes.html', clientes=sistema.clientes,
                                   msg="CPF inválido! Digite apenas 11 números.")

        # Cadastro OK
        sistema.cadastrar_cliente(nome, idade, cpf)
        return redirect('/clientes')

    return render_template('clientes.html', clientes=sistema.clientes)



@app.route('/vendas', methods=['GET', 'POST'])
def vendas():
    if request.method == 'POST':
        cpf = request.form['cpf']
        produto = request.form['produto']
        quantidade = int(request.form['quantidade'])
        msg = sistema.vender(cpf, produto, quantidade)
        return render_template('vendas.html', vendas=sistema.vendas, msg=msg)
    return render_template('vendas.html', vendas=sistema.vendas)

@app.route('/relatorio')
def relatorio():
    return render_template(
        'relatorio.html',
        produtos=sistema.produtos,
        clientes=sistema.clientes,
        vendas=sistema.vendas
    )

if __name__ == "__main__":
    app.run(debug=True)