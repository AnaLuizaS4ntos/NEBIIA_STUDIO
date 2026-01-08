document.addEventListener('DOMContentLoaded', function () {
  
  // Função principal que inicia o TinyMCE
  function initTiny() {
    // Verificações de segurança pra não dar erro se a net estiver lenta
    if (typeof tinymce === 'undefined') return;
    if (tinymce.get('roteiro_editor')) return;

    tinymce.init({
      selector: '#roteiro_editor', // Precisa bater com o ID do textarea no criar.html
      height: 600,
      menubar: false, // Remove menus desnecessários
      statusbar: false, // Remove barra de status inferior
      branding: false, // Remove logo do TinyMCE
      language: 'pt_BR', // Se tiver a tradução, senão usa inglês mesmo
      
      // Plugins essenciais
      plugins: [
        'lists', 'link', 'charmap', 'preview', 'searchreplace', 'visualblocks', 'code', 'wordcount', 'autoresize'
      ],
      
      // A BARRA DE FERRAMENTAS (Aqui definimos a ordem dos botões)
      toolbar: 'scene action character dialogue parenthetical transition | undo redo | removeformat',
      
      // Definição interna dos formatos (Mapeia o nome para a classe CSS)
      formats: {
        scene: { block: 'h3', classes: 'sc-scene', remove: 'all' },
        action: { block: 'p', classes: 'sc-action', remove: 'all' },
        character: { block: 'p', classes: 'sc-character', remove: 'all' },
        dialogue: { block: 'p', classes: 'sc-dialogue', remove: 'all' },
        parenthetical: { block: 'p', classes: 'sc-parenthetical', remove: 'all' },
        transition: { block: 'p', classes: 'sc-transition', remove: 'all' }
      },

      // CSS INJETADO (Para você ver a formatação enquanto escreve)
      // Nota: Esses valores batem com o seu style.css para ficar igual ao PDF
     /* No seu script.js, substitua o content_style por este com valores menores */

content_style: `
  body { 
    font-family: 'Courier Prime', 'Courier New', Courier, monospace;
    font-size: 12pt;
    line-height: 1.0;
    max-width: 8.5in;
    margin: 0 auto;
    padding: 1in; /* A folha já tem borda */
    color: black;
  }
  
  .sc-scene { font-weight: bold; text-transform: uppercase; margin-top: 1.5em; margin-bottom: 0.5em; width: 100%; }
  .sc-action { text-align: left; width: 100%; margin-bottom: 1em; }

  /* --- VALORES CORRIGIDOS (Diminuímos ~1 polegada de tudo) --- */
  
  /* PERSONAGEM: Era 3.7in -> Agora 2.0in (Fica mais no meio) */
  .sc-character { 
    text-align: left; 
    margin-left: 2.2in; 
    width: auto; 
    text-transform: uppercase; 
    margin-top: 1em; 
    margin-bottom: 0px; 
    font-weight: bold; 
  }

  /* FALA: Era 2.5in -> Agora 1.3in (Não fica tão na ponta) */
  .sc-dialogue { 
    text-align: left; 
    margin-left: 1.3in; 
    width: 3.8in;  /* Aumentei um pouquinho a largura pra caber mais texto */
    margin-bottom: 0px; 
  }

  /* PARÊNTESES: Era 3.1in -> Agora 1.9in */
  .sc-parenthetical { 
    text-align: left; 
    margin-left: 1.9in; 
    width: 2.5in; 
    margin-bottom: 0px; 
    font-style: italic; 
  }

  .sc-transition { text-align: right; width: 100%; margin-top: 1em; margin-bottom: 1em; }
`,

      // --- AQUI ESTÁ A LÓGICA DOS BOTÕES ---
      setup: function (editor) {
        
        // Função auxiliar: Aplica o formato e GARANTE que limpou o anterior
        const applyFormat = (formatName) => {
          const formatClasses = ['sc-scene', 'sc-action', 'sc-character', 'sc-dialogue', 'sc-parenthetical', 'sc-transition'];
          const node = editor.selection.getNode();
          
          // 1. Remove qualquer classe de roteiro que já esteja na linha
          formatClasses.forEach(cls => {
             editor.dom.removeClass(node, cls);
          });
          
          // 2. Remove negrito e itálico manuais para não sujar
          editor.formatter.remove('bold');
          editor.formatter.remove('italic');

          // 3. Aplica o novo formato desejado
          editor.formatter.apply(formatName);
        };

        // Função auxiliar para registrar botão na barra
        const registerBtn = (name, text, formatName) => {
          editor.ui.registry.addButton(name, {
            text: text,
            onAction: () => applyFormat(formatName)
          });
        };

        // Criação dos Botões Visuais
        registerBtn('scene', 'CENA', 'scene');
        registerBtn('action', 'AÇÃO', 'action');
        registerBtn('character', 'PERSONAGEM', 'character');
        registerBtn('dialogue', 'FALA', 'dialogue');
        registerBtn('parenthetical', '(parênteses)', 'parenthetical');
        registerBtn('transition', 'TRANSIÇÃO', 'transition');

        // --- LÓGICA DO "ENTER MÁGICO" ---
        editor.on('keydown', function (e) {
          // Se apertou ENTER (código 13) e NÃO está segurando Shift
          if (e.keyCode === 13 && !e.shiftKey) { 
            
            const node = editor.selection.getNode();
            
            // Regra 1: Estava em PERSONAGEM? -> Vai para FALA
            if (node.classList.contains('sc-character')) {
              e.preventDefault(); 
              editor.insertContent('<p class="sc-dialogue">&nbsp;</p>'); 
            }
            // Regra 2: Estava em FALA? -> Vai para PERSONAGEM (Bate-bola rápido)
            else if (node.classList.contains('sc-dialogue')) {
              e.preventDefault();
              editor.insertContent('<p class="sc-character">&nbsp;</p>');
            }
            // Regra 3: Estava em PARENTESES? -> Vai para FALA
            else if (node.classList.contains('sc-parenthetical')) {
              e.preventDefault();
              editor.insertContent('<p class="sc-dialogue">&nbsp;</p>');
            }
            // Regra 4: Estava em CENA? -> Vai para AÇÃO
            else if (node.classList.contains('sc-scene')) {
              e.preventDefault();
              editor.insertContent('<p class="sc-action">&nbsp;</p>');
            }
            // Se estava em AÇÃO, o comportamento padrão cria outro parágrafo de AÇÃO (normal)
          }
        });
      }
    });
  }

  // Sistema de Polling: Tenta carregar o editor até o script do TinyMCE estar pronto
  if (typeof tinymce !== 'undefined') {
    initTiny();
  } else {
    let tries = 0;
    const interval = setInterval(() => {
      if (typeof tinymce !== 'undefined') {
        clearInterval(interval);
        initTiny();
      } else if (++tries > 50) { // Desiste depois de 10 segundos pra não travar
        clearInterval(interval);
      }
    }, 200);
  }
});

function salvaConteudo() {
  if (typeof tinymce !== 'undefined' && tinymce.get('roteiro_editor')) {
      tinymce.triggerSave();
  }
}