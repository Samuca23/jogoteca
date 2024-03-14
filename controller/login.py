from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app
from model.usuarios import Usuarios
from helpers import FormularioUsuario

@app.route('/login')
def login() :
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST', ])
def autenticar() :
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    if usuario:
        if form.password.data == usuario.senha :
            session['usuario_logado'] = usuario.nickname
            flash('Login efetuado com sucesso!')
            proxima_pagina = request.form['proxima']

            if  proxima_pagina == 'None' :
                return redirect(url_for('index'))

            return redirect(proxima_pagina)
    else :
        flash('Login incorreto!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout() :
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))