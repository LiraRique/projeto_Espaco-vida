#################################### APLICAÇÃO FLASK #####################################

from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import hashlib
import pyodbc
from datetime import date, datetime
from models import Usuario, Contato_Pessoa,Endereco_Pessoa,Quadro_Clinico,Pessoa

from metodos import  metodo_login,metodo_cadastrar, metodo_buscar_cliente, metodo_exibe_cliente


app = Flask(__name__)
app.secret_key = 'alura'
#################################### ^^^^^^^^^^^^^^^^^^ ####################################


#################################### CONEXÃO SQL SERVER ####################################

parametro=pyodbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-DHA43PM\BD_EXPRESS_L;'
                    'Database=Espaco_Terapia;'
                    'Trusted_Connection=yes;')
    
db = parametro.cursor()
login_usuario = metodo_login.UsuarioDao(db)

met_cadastrar = metodo_cadastrar.cadastrar_cliente(db)
buscar_id_usuario = metodo_buscar_cliente.busca_usuario(db)
exibe_tb_usuario = metodo_exibe_cliente.busca_cliente_por_id(db)

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


@app.route('/relatorio_cliente')
def relatorio_cliente():
     if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('relatorio_cliente')))        
     return render_template('relatorio_cliente.html')


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


#################################### EXIBE DADOS TABELA ##################################################

@app.route('/editar', methods=['POST'])
def editar():
    id_pessoa_tb = int(request.form['id_produto'])
    print(id_pessoa_tb)
    dados_td =exibe_tb_usuario.listar(id_pessoa_tb)

    print(dados_td[1][1])

    return jsonify({
			'nome': dados_produto[0][1],
            'cpf': dados_produto[0][2],
           
        
            'cep': dados_produto[0][5],
            'cidade': dados_produto[0][6],
            'uf': dados_produto[0][7],
            'endereco': dados_produto[0][8],
            'numero_endereco': dados_produto[0][9],
            'telefone': dados_produto[0][10],
            'celular': dados_produto[0][11],
            'artrose': dados_produto[0][12],
            'protusao_ernia_disco': dados_produto[0][13],
            'cirurgia': dados_produto[0][14],
            'medicacao': dados_produto[0][15],
            'email': dados_produto[0][16],
            'queixas_atuais': dados_produto[0][17],
    })

#################################### ^^^^^^^^^^^^^^^^^^ ####################################

app.run(debug=True)

