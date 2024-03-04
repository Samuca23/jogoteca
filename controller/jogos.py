from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app
from model.jogos import Jogos
from db import db

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=Jogos.query.order_by(Jogos.id))

@app.route('/novo')
def novo() :
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo'))) 
    
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',]) 
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogos.query.filter_by(nome=nome).first()

    if jogo:
        flash("Jogo já existente!")
    else:
        novo_jogo = Jogos(nome=nome, categoria=categoria, console=console)
        db.session.add(novo_jogo)
        db.session.commit()

    return redirect(url_for('index'))