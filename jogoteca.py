from flask import Flask, render_template, request
from jogo import Jogo

app = Flask(__name__)

lista = []
jogo_1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo_2 = Jogo('God od War', 'Rack n Slash', 'PS2')
lista = [jogo_1, jogo_2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo() :
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',]) 
def criar() : 
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

if __name__ == '__main__':
    app.run(debug=True)