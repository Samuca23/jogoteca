from jogoteca import app
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class FormularioJogo(FlaskForm) :
    nome = StringField('Nome do jogo', [validators.DataRequired(), validators.Length(min=1, max=50)])
    categoria = StringField('Categoria do Jogo', [validators.DataRequired(), validators.Length(min=1, max=40)])
    console = StringField('Console do Jogo', [validators.DataRequired(), validators.Length(min=1, max=20)])
    salvar = SubmitField('Salvar')

class FormularioUsuario(FlaskForm) :
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    password = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')

def recupera_imagem(id) :
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']) :
        if f'capa{id}' in nome_arquivo :
            print(nome_arquivo)
            return nome_arquivo
        
    return 'capa_padrao.jpg'

def deleta_arquivo(id) :
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_padrao.jpg' :
        print('Removendo')
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))