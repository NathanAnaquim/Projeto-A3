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
        preco = float(request.form['preco'])
        quantidade = int(request.form['quantidade'])
        sistema.cadastrar_produto(nome, preco, quantidade)
        return redirect('/produtos')
    return render_template('produtos.html', produtos=sistema.produtos)

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = int(request.form['idade'])
        cpf = request.form['cpf']
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