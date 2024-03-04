from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app
from model.usuarios import Usuarios

@app.route('/login')
def login() :
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST', ])
def autenticar() :
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
        if request.form['senha'] == usuario.senha :
            session['usuario_logado'] = usuario.nickname
            flash('Login efetuado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else :
        flash('Login incorreto!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout() :
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))