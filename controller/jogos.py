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


@app.route('/criar', methods=['POST']) 
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

        arquivo = request.files['arquivo']
        uploads_path = app.config['UPLOAD_PATH']
        arquivo.save(f'{uploads_path}/capa_{novo_jogo.id}_{arquivo.filename}')

    return redirect(url_for('index'))

@app.route('/editar/<int:id>')
def editar(id) :
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('editar'))) 
    
    jogo = Jogos.query.filter_by(id=id).first()
    return render_template('editar.html', titulo='Editando Jogo', jogo=jogo)

@app.route('/atualizar', methods=['POST']) 
def atualizar():
    jogo = Jogos.query.filter_by(id=request.form['id']).first()
    jogo.nome = request.form['nome']
    jogo.categoria = request.form['categoria']
    jogo.console = request.form['console']

    db.session.add(jogo)
    db.session.commit()

    return redirect( url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id) :
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login'))
    
    Jogos.query.filter_by(id=id).delete()
    db.session.commit()
    flash('Jogo deletado com sucesso!')
    
    return redirect(url_for('index'))
