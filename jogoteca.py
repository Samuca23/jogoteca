from flask import Flask, render_template
from jogo import Jogo

app = Flask(__name__)

@app.route('/jogoteca')
def hello():
    jogo_1 = Jogo('Tetris', 'Puzzle', 'Atari')
    jogo_2 = Jogo('God od War', 'Rack n Slash', 'PS2')

    jogo = [jogo_1, jogo_2]
    return render_template('lista.html', titulo='Jogos', jogos=jogo)

if __name__ == '__main__':
    app.run(debug=True)