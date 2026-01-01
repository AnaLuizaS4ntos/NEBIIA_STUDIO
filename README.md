# Nebbia Studio
> *Platform for Animation Scriptwriting*

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-green?style=for-the-badge&logo=flask)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=for-the-badge&logo=javascript)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-orange?style=for-the-badge)

O **Nebbia Studio** é uma aplicação web Full Stack desenvolvida para auxiliar roteiristas e estúdios de animação. O foco do projeto é oferecer um editor de texto inteligente que formata automaticamente roteiros no padrão da indústria (Hollywood Standard), permitindo que o criativo foque apenas na história.

## Objetivo
Resolver a dor de roteiristas independentes que precisam de ferramentas ágeis para formatar Cenas, Ações e Diálogos sem depender de softwares caros e complexos.

## Tecnologias
* **Back-end:** Python, Flask (Rotas e Templating Jinja2)
* **Front-end:** HTML5, CSS3, JavaScript (Manipulação avançada de DOM)
* **Editor:** Integração com TinyMCE API customizada
* **Design:** Identidade visual própria ("Nebbia UI")

## Funcionalidades Principais
- [x] **Editor Rich-Text:** Interface limpa para escrita sem distrações.
- [x] **Formatação Automática:** Botões dedicados para *Cena*, *Ação*, *Personagem* e *Diálogo*.
- [x] **Lógica de Atalhos:** O sistema entende o contexto (ex: ao dar Enter após um personagem, o próximo bloco já é um diálogo).
- [ ] **Exportação em PDF:** (Em breve)
- [ ] **Login de Usuário:** (Em breve)

## Como rodar o projeto localmente

1. Instale o flask no seu notebook ou computador:  https://flask.palletsprojects.com/en/stable/installation/

2. Depois de aberto o código rode no terminal o: pip install flask

3. Depois rode no terminal: python app.py

4. Agora clique no link com o crtl+click: http://localhost:5000

-------------------------
1. Clone o repositório:
   ```bash
   git clone [https://github.com/AnaLuizaS4ntos/nebbia-studio.git](https://github.com/AnaLuizaS4ntos/nebbia-studio.git)
