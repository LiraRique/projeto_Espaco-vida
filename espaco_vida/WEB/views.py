#################################### APLICAÇÃO FLASK #####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import hashlib
import pyodbc
from datetime import date, datetime
from models import Usuario, Contato_Pessoa,Endereco_Pessoa,Quadro_Clinico,Pessoa

from metodos import  metodo_login,metodo_cadastrar, metodo_buscar_cliente


app = Flask(__name__)
app.secret_key = 'alura'
#################################### ^^^^^^^^^^^^^^^^^^ ####################################


#################################### CONEXÃO SQL SERVER ####################################

parametro=pyodbc.connect('Driver={SQL Server};'
                    'Server=LIRA-PC\SQLEXPRESS;'
                    'Database=Espaco_Terapia;'
                    'Trusted_Connection=yes;')
    
db = parametro.cursor()
login_usuario = metodo_login.UsuarioDao(db)

met_cadastrar = metodo_cadastrar.cadastrar_cliente(db)
buscar_id_usuario = metodo_buscar_cliente.busca_usuario(db)


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
     lista = buscar_id_usuario.listar()
     return render_template('ficha_cliente.html',lista_usuario = lista)


#################################### ^^^^^^^^^^^^^^^^^^ ####################################

#################################### AUTENTICAÇÃO ##########################################

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

#################################### CRUD ##################################################

@app.route('/cadastrar_cliente', methods= ['POST',])
def cadastrar_cliente():
    id_pessoa = met_cadastrar.ultima_posicao_id() + 1
    nome = request.form['nome_usuario']

    datanascimento = request.form['data_nascimento']
    cpf_usu = request.form['cpf']
    sexo = request.form['sexo']

    celular = request.form['celular']
    telefone = request.form['telefone']
    email = request.form['email']
    nome_contato = request.form['nome_usuario']

    endereco = request.form['endereco']
    numero_end= request.form['numero_endereco']
    cidade= request.form['cidade']
    uf= request.form['uf']
    cep= request.form['cep']

    artrose = request.form['artrose']
    protusao_ernia = request.form['protusao']
    cirurgia = request.form['cirurgia']
    medicacao = request.form['medicacao']
    queixas = request.form['descricao']

    p = Pessoa(id_pessoa, nome, datanascimento, cpf_usu, sexo)
    c= Contato_Pessoa(id_pessoa, celular,telefone,email,nome_contato)
    e = Endereco_Pessoa(id_pessoa, endereco, numero_end, cidade,uf, cep)
    q = Quadro_Clinico(id_pessoa, artrose, protusao_ernia,cirurgia,medicacao,queixas)
    att_cadastro = met_cadastrar.cadastrar_cliente_sistema(p, c , e, q)

    flash('Cliente cadastrado com sucesso!')
    return redirect(url_for('deash_usuario'))



app.run(debug=True)

