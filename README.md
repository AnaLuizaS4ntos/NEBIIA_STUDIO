# Nebbia Studio

Bem-vindo ao repositório do **Nebbia Studio**! 
Este é um projeto **Full Stack** desenvolvido em **Python (Flask)**, focado em oferecer uma plataforma intuitiva para roteiristas gerenciarem, visualizarem e organizarem seus roteiros de forma gamificada e visual.

---

## Sobre o Projeto

O Nebbia Studio nasceu da necessidade de criar ferramentas melhores para escritores criativos. Diferente de editores de texto comuns, ele foca na experiência do usuário (UX), permitindo:
- **Upload e Leitura de PDFs:** Visualização integrada de roteiros no navegador.
- **Gestão de Conteúdo:** Sistema de Login, Cadastro e Dashboard personalizado.
- **Design Responsivo:** Interface moderna pensada para facilitar a leitura.

---

## Tecnologias Utilizadas

* **Back-end:** [Python](https://www.python.org/) e [Flask](https://flask.palletsprojects.com/) (Microframework robusto e ágil).
* **Banco de Dados:** SQLite (SQLAlchemy para ORM).
* **Front-end:** HTML5, CSS3, JavaScript (Vanilla).
* **Design:** Interface criada com foco em usabilidade (UI/UX).

---

## Como Rodar o Projeto na sua Máquina

Se você quiser testar o Nebbia Studio localmente, siga os passos abaixo.

### 1. Pré-requisitos
Você precisa ter o **Python** instalado. [Baixe aqui](https://www.python.org/downloads/).

### 2. Clonar o Repositório
Abra seu terminal (Git Bash ou CMD) e digite:

`bash
git clone [https://github.com/AnaLuizaS4ntos/NEBIIA_STUDIO.git](https://github.com/AnaLuizaS4ntos/NEBIIA_STUDIO.git)
cd NEBIIA_STUDIO `

### 3. Criar e Ativar o Ambiente Virtual (Recomendado)
**No windows**
` python -m venv venv `
` venv\Scripts\activate `

**No Mac/Linux**
` python3 -m venv venv `
` source venv/bin/activate `

### 4. Instalar as Dependências (Flask e outras)
O projeto utiliza o Flask. Para instalar todas as ferramentas necessárias de uma vez:

` pip install flask sqlalchemy `
(Se houver um arquivo requirements.txt, use: pip install -r requirements.txt)

### 5. Configurar o Banco de Dados
Para garantir que o banco de dados seja criado corretamente na primeira execução:

` python atualizar_banco.py `

### 6. Rodar o Servidor
Agora é só iniciar a aplicação:

` python app.py `

**Acesse no seu navegador: http://127.0.0.1:5000** (use tbm o ctrl + click)


### Funcionalidades Atuais
[x] Autenticação: Login e Registro de novos usuários com segurança.

[x] Dashboard: Painel exclusivo para ver seus projetos.

[x] Leitor de PDF: Visualizador embutido para não precisar baixar o arquivo.

[x] Upload: Envio de arquivos PDF para a nuvem/servidor local.

Contato
Projeto desenvolvido por Ana Luiza.
(88) 994165427 - whatsapp
analuizadossantos5@gmail.com
---

### Dica Extra:
Você viu que eu coloquei um passo ali **"4. Instalar as Dependências"**?
Para isso funcionar perfeitamente igual a um projeto profissional, você deve criar um arquivo `requirements.txt`.

**Como criar em 1 segundo:**
1.  No seu terminal do VS Code (com o `(venv)` ativado), digite:
    `pip freeze > requirements.txt`
2.  Vai aparecer um arquivo novo chamado `requirements.txt` na pasta.
3.  Dá um `git add requirements.txt`, `git commit` e `git push`.






