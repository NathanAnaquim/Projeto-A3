from flask import Flask, render_template, request, redirect
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