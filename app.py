from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import sqlite3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
# Onde os PDFs moram
app.config['UPLOAD_FOLDER'] = 'static/pdfs' 

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
app.config['SECRET_KEY'] = 'chave-secreta-nebbia'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

# ### Login ###
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# ### Função que carrega o usuário pelo ID ###
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

# 2. MODELO DO USUÁRIO 
class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# 3. INICIALIZAÇÃO DO BANCO 
def init_db():
    with app.app_context():
        db.create_all()
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS roteiros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            id_usuario INTEGER
        )""")
        conn.commit()
        conn.close()
        print("Banco Híbrido Iniciado!")

init_db()

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        print("--- PASSO 1: O botão foi clicado! ---")
        
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        print(f"--- PASSO 2: Recebi os dados: {nome}, {email} ---")

        usuario_existente = Usuario.query.filter_by(email=email).first()
        if usuario_existente:
            print("--- ERRO: Email já cadastrado! ---")
            return "<h1>Erro: Esse email já existe no banco! Tente outro.</h1>"

        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        
        try:
            db.session.add(novo_usuario)
            db.session.commit()
            print("--- PASSO 3: Salvo com sucesso! Redirecionando para Home... ---")
            
            return redirect(url_for('index')) 
            
        except Exception as e:
            print(f"--- ERRO CRÍTICO NO BANCO: {e} ---")
            return f"<h1>Deu erro no banco de dados: {e}</h1>"
            
    return render_template("registrar.html")

# ### NOVO: A ROTA DE LOGIN ###
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']
        
        # Busca o usuário no banco
        usuario = Usuario.query.filter_by(email=email).first()
        
        # Verifica se existe e se a senha bate
        if usuario and usuario.senha == senha:
            login_user(usuario)
            return redirect(url_for('index'))
        else:
            return "Email ou senha incorretos!"
            
    return render_template("login.html")

# ### NOVO: ROTA DE LOGOUT (SAIR) ###
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/")
def index():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM roteiros")
    roteiros = cursor.fetchall() 
    conn.close()
    
    return render_template("index.html", roteiros=roteiros, usuario=current_user)

@app.route('/criar', methods=['GET', 'POST'])
@login_required
def criar():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        conteudo = request.form.get('conteudo')
        
        # Tenta pegar o arquivo PDF (se a pessoa enviou)
        arquivo = request.files.get('arquivo_pdf')
        nome_pdf = None 

        # Se tiver arquivo e for PDF, salva
        if arquivo and arquivo.filename != '':
            filename = secure_filename(arquivo.filename)
            arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            nome_pdf = filename # Guarda o nome para o banco

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Salvamos Título, Conteúdo, ID do Usuário E O PDF
        cursor.execute("""
            INSERT INTO roteiros (titulo, conteudo, id_usuario, pdf)
            VALUES (?, ?, ?, ?)
        """, (titulo, conteudo, current_user.id, nome_pdf))
        
        conn.commit()
        conn.close()
        return redirect(url_for('meus_roteiros'))
        
    return render_template('criar.html')

@app.route("/roteiro/<int:id>")
def ler(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM roteiros WHERE id=?", (id,))
    roteiro = cursor.fetchone()
    conn.close()
    return render_template("ler.html", roteiro=roteiro)

# Adicione isso junto com as outras rotas
@app.route("/meus_roteiros")
@login_required
def meus_roteiros():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Filtra o usuario logado
    cursor.execute("SELECT * FROM roteiros WHERE id_usuario = ?", (current_user.id,))
    meus_roteiros = cursor.fetchall()
    
    conn.close()
    return render_template("meus_roteiros.html", roteiros=meus_roteiros)

# Rota para EXCLUIR um roteiro
@app.route('/deletar/<int:id>')
@login_required
def deletar(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT id_usuario FROM roteiros WHERE id = ?", (id,))
    roteiro = cursor.fetchone()
    
    if roteiro and roteiro[0] == current_user.id:
        cursor.execute("DELETE FROM roteiros WHERE id = ?", (id,))
        conn.commit()
    
    conn.close()
    return redirect(url_for('meus_roteiros'))

if __name__ == "__main__":
    app.run(debug=True)