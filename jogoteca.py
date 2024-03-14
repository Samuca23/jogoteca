from flask import Flask, render_template, request, redirect, session, flash, url_for
from db import db
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Inicialize o objeto db
db.init_app(app)
csrf = CSRFProtect(app)

from controller.jogos import *
from controller.login import *

if __name__ == '__main__':
    app.run(debug=True)