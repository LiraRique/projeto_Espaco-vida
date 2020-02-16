#################################### APLICAÇÃO FLASK ####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import hashlib
import pyodbc
from datetime import date, datetime


app = Flask(__name__)
app.secret_key = 'alura'

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

@app.route('/')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/deash_usuario')
def deash_usuario():
    return render_template('deash_usuario.html')


@app.route('/formulario_cadastro')
def formulario_cadastro():
    return render_template('formulario_cadastro.html')


@app.route('/ficha_cliente')
def ficha_cliente():
    return render_template('ficha_cliente.html')







#################################### ^^^^^^^^^^^^^^^^^^ ####################################


app.run(debug=True)

