#################################### APLICAÇÃO FLASK #####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import hashlib
import pyodbc
from datetime import date, datetime
from models import Usuario
from metodos import metodo_login


app = Flask(__name__)
app.secret_key = 'alura'
#################################### ^^^^^^^^^^^^^^^^^^ ####################################


#################################### CONEXÃO SQL SERVER ####################################

parametro=pyodbc.connect('Driver={SQL Server};'
                    'Server=NOTE_CPV-EEE\SQLEXPRESS;'
                    'Database=Espaco_Terapia;'
                    'Trusted_Connection=yes;')
    
db = parametro.cursor()
login_usuario = metodo_login.UsuarioDao(db)


#################################### ^^^^^^^^^^^^^^^^^^ ####################################

####################################        VIEWS ADMINISTRADOR       ######################

@app.route('/')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/deash_usuario')
def deash_usuario():
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('deash_usuario')))
     return render_template('deash_usuario.html')


@app.route('/formulario_cadastro')
def formulario_cadastro():
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('formulario_cadastro')))
     return render_template('formulario_cadastro.html')


@app.route('/ficha_cliente')
def ficha_cliente():
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('ficha_cliente')))
     return render_template('ficha_cliente.html')


#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### AUTENTICAÇÃO E CRUD ###################################

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    usuario = login_usuario.buscar_por_id(request.form['email_usuario'])
    password = request.form['senha_usuario']
    password_app = hashlib.md5(password.encode())
    senha_aplicacao = password_app.hexdigest()
    if usuario:
        if usuario.senha_aplicacao == senha_aplicacao:
                session['usuario_logado'] = usuario.email_usuario
                flash('Administrador(a)  ' + usuario.nome_usuario + ' logado!')
                proxima_pagina = url_for('deash_usuario')
                return redirect(proxima_pagina)
        else:
            flash('Senha invalida, tente denovo!')
            return redirect(url_for('login'))
    else:
        flash('Usuario não encontrado!')
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Deslogado com sucesso!')
    return redirect(url_for('login'))




#################################### ^^^^^^^^^^^^^^^^^^ ####################################





app.run(debug=True)

