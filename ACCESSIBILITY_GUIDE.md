# 📚 Guia de Acessibilidade - TruK

## 🎯 Objetivo

Este guia documenta os padrões de acessibilidade implementados na aplicação TruK e fornece diretrizes para manter e melhorar a acessibilidade em desenvolvimentos futuros.

---

## 🌟 Padrões WCAG Adotados

A aplicação segue as **Web Content Accessibility Guidelines (WCAG) 2.1 Nível AA**.

### Princípios POUR

1. **Perceptível** - Informação deve ser apresentada de forma que usuários possam perceber
2. **Operável** - Componentes de interface devem ser operáveis
3. **Compreensível** - Informação e operação da interface devem ser compreensíveis
4. **Robusto** - Conteúdo deve ser robusto o suficiente para ser interpretado por diversos user agents

---

## ✅ Implementações Realizadas

### 1. Estrutura Semântica HTML

#### Landmarks ARIA
```html
<nav role="navigation" aria-label="Navegação principal">
<main id="main-content" role="main">
<footer role="contentinfo">
```

**Por que:** Landmarks ajudam screen readers a navegar rapidamente entre seções da página.

#### Headings Hierárquicos
```html
<h1>Título Principal</h1>
  <h2>Subtítulo</h2>
    <h3>Sub-subtítulo</h3>
```

**Regras:**
- Sempre começar com `<h1>`
- Não pular níveis (não vá de h1 para h3)
- Use apenas um `<h1>` por página

---

### 2. Formulários Acessíveis

#### Labels Explícitos
```html
<!-- ✅ CORRETO -->
<div class="form-group">
    <label for="id_username">Username</label>
    <input type="text" id="id_username" name="username">
</div>

<!-- ❌ ERRADO -->
<div class="form-group">
    <label>Username</label>
    <input type="text" name="username">
</div>
```

#### Mensagens de Erro
```html
<span class="error" role="alert" aria-live="polite">
    {{ form.field.errors }}
</span>
```

**Atributos importantes:**
- `role="alert"` - Indica que é uma mensagem importante
- `aria-live="polite"` - Screen reader anuncia quando conveniente

#### Fieldsets e Legends
```html
<fieldset>
    <legend>Origem e Destino</legend>
    <!-- Campos relacionados -->
</fieldset>
```

---

### 3. Navegação por Teclado

#### Skip Navigation
```html
<a href="#main-content" class="skip-link">
    Pular para o conteúdo principal
</a>
```

**CSS:**
```css
.skip-link {
    position: absolute;
    top: -40px;
    left: 0;
}

.skip-link:focus {
    top: 0;
}
```

#### Estados de Foco Visíveis
```css
*:focus-visible {
    outline: 3px solid var(--primary);
    outline-offset: 2px;
}
```

**Por que:** Usuários de teclado precisam ver onde o foco está.

#### Ordem de Tabulação
- Siga a ordem natural do DOM
- Use `tabindex="0"` para elementos customizados interativos
- Nunca use `tabindex` positivo (ex: tabindex="1")

---

### 4. Componentes Interativos

#### Dropdown Menu Acessível
```html
<button 
    class="user-menu" 
    aria-expanded="false" 
    aria-haspopup="true"
    id="user-menu-button">
    {{ user.username }}
    <span aria-hidden="true"> ▼</span>
</button>
<ul class="dropdown-menu" 
    role="menu" 
    aria-labelledby="user-menu-button">
    <li role="none">
        <a href="/profile" role="menuitem">Perfil</a>
    </li>
</ul>
```

**Comportamento de Teclado:**
- `Enter/Space` - Abre/fecha menu
- `ArrowDown/Up` - Navega entre itens
- `Escape` - Fecha menu e retorna foco ao botão

**JavaScript:** Ver `/static/js/accessibility.js`

---

### 5. Conteúdo Não-Textual

#### Emojis e Ícones
```html
<!-- ✅ CORRETO -->
<div class="stat-icon" aria-label="Pacotes">📦</div>

<!-- ❌ ERRADO -->
<div class="stat-icon">📦</div>
```

#### Ícones Decorativos
```html
<span aria-hidden="true">▼</span>
```

**Quando usar `aria-hidden="true"`:**
- Ícones puramente decorativos
- Conteúdo redundante
- Caracteres especiais usados para estilo

---

### 6. Tabelas Acessíveis

#### Estrutura Completa
```html
<table class="table">
    <caption class="sr-only">
        Descrição da tabela para screen readers
    </caption>
    <thead>
        <tr>
            <th scope="col">Coluna 1</th>
            <th scope="col">Coluna 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Dado 1</td>
            <td>Dado 2</td>
        </tr>
    </tbody>
</table>
```

**Elementos essenciais:**
- `<caption>` - Título/descrição da tabela
- `scope="col"` - Para headers de coluna
- `scope="row"` - Para headers de linha

---

### 7. ARIA Live Regions

#### Mensagens do Sistema
```html
<div 
    class="messages-container" 
    role="region" 
    aria-live="polite" 
    aria-atomic="true"
    aria-label="Mensagens do sistema">
    {% for message in messages %}
    <div class="alert alert-{{ message.tags }}" role="alert">
        {{ message }}
    </div>
    {% endfor %}
</div>
```

**Níveis de `aria-live`:**
- `polite` - Anuncia quando screen reader estiver ocioso
- `assertive` - Interrompe para anunciar imediatamente
- `off` - Não anuncia

---

### 8. Classes Utilitárias

#### Screen Reader Only
```css
.sr-only {
    position: absolute;
    width: 1px;
    height: 1px;
    padding: 0;
    margin: -1px;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border-width: 0;
}
```

**Uso:**
```html
<caption class="sr-only">
    Informação visível apenas para screen readers
</caption>
```

---

## 🎨 Contraste de Cores

### Requisitos WCAG AA

- **Texto normal** (< 18pt): Ratio mínimo **4.5:1**
- **Texto grande** (≥ 18pt ou ≥ 14pt bold): Ratio mínimo **3:1**
- **Componentes UI**: Ratio mínimo **3:1**

### Cores da Aplicação

```css
:root {
    --primary: #3498db;    /* Azul */
    --secondary: #95a5a6;  /* Cinza */
    --success: #27ae60;    /* Verde */
    --danger: #e74c3c;     /* Vermelho */
    --warning: #f39c12;    /* Laranja */
    --info: #16a085;       /* Turquesa */
    --dark: #2c3e50;       /* Azul escuro */
    --light: #ecf0f1;      /* Cinza claro */
}
```

**Ferramentas para verificar:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Colour Contrast Analyser](https://www.tpgi.com/color-contrast-checker/)

---

## 📋 Checklist para Novos Componentes

### Antes de Criar
- [ ] Existe um componente HTML semântico apropriado?
- [ ] Precisa ser interativo via teclado?
- [ ] Precisa de ARIA attributes?

### Formulários
- [ ] Todos os inputs têm labels com `for` correto?
- [ ] Erros têm `role="alert"` e `aria-live="polite"`?
- [ ] Campos relacionados estão em `<fieldset>` com `<legend>`?
- [ ] Campos obrigatórios indicados (não apenas com cor)?

### Interatividade
- [ ] Funciona apenas com teclado?
- [ ] Estados de foco são visíveis?
- [ ] Estados são anunciados (aria-expanded, aria-pressed, etc)?
- [ ] Escape fecha componentes modais/dropdowns?

### Conteúdo
- [ ] Imagens têm `alt` text descritivo?
- [ ] Ícones decorativos têm `aria-hidden="true"`?
- [ ] Ícones informativos têm `aria-label`?
- [ ] Vídeos têm legendas/transcrições?

### Tabelas
- [ ] Tem `<caption>` descritivo?
- [ ] Headers usam `<th>` com `scope`?
- [ ] Dados complexos têm `headers` attribute?

---

## 🧪 Testes de Acessibilidade

### Testes Automatizados

#### Script Python
```bash
python3 accessibility_audit.py
```

#### Browser DevTools
- Chrome/Edge: Lighthouse (Accessibility audit)
- Firefox: Accessibility Inspector

#### Extensões Recomendadas
- **axe DevTools** (Chrome/Firefox)
- **WAVE** (Chrome/Firefox/Edge)

### Testes Manuais

#### 1. Navegação por Teclado
```
Tab       - Próximo elemento
Shift+Tab - Elemento anterior
Enter     - Ativar link/botão
Space     - Ativar botão/checkbox
Arrows    - Navegar em menus/sliders
Escape    - Fechar modais/menus
```

**Checklist:**
- [ ] Todos elementos interativos são alcançáveis?
- [ ] Ordem de tabulação faz sentido?
- [ ] Foco está sempre visível?
- [ ] Nenhum "keyboard trap"?

#### 2. Screen Readers

**Windows:**
- **NVDA** (gratuito) - [Download](https://www.nvaccess.org/)
- **JAWS** (pago) - [Download](https://www.freedomscientific.com/products/software/jaws/)

**macOS:**
- **VoiceOver** (nativo) - Cmd+F5

**Mobile:**
- **TalkBack** (Android)
- **VoiceOver** (iOS)

**Teste:**
- [ ] Navegação por landmarks funciona?
- [ ] Headings são anunciados corretamente?
- [ ] Labels de formulário são lidos?
- [ ] Estados são anunciados?
- [ ] Mensagens dinâmicas são anunciadas?

#### 3. Zoom e Responsividade
- [ ] Testar zoom 200% (Ctrl/Cmd + +)
- [ ] Nenhum overflow horizontal?
- [ ] Texto permanece legível?
- [ ] Funcionalidade mantida?

---

## 📚 Recursos e Referências

### Documentação Oficial
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/)
- [MDN Web Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)

### Ferramentas
- [WebAIM](https://webaim.org/)
- [A11y Project](https://www.a11yproject.com/)
- [Inclusive Components](https://inclusive-components.design/)

### Comunidade
- [A11y Weekly Newsletter](https://a11yweekly.com/)
- [WebAIM Mailing List](https://webaim.org/discussion/)

---

## 🚀 Próximos Passos

### Curto Prazo
1. Testar com usuários reais que usam tecnologias assistivas
2. Implementar testes automatizados no CI/CD
3. Documentar padrões específicos do projeto

### Médio Prazo
1. Adicionar modo alto contraste
2. Implementar preferências de usuário (reduzir animações)
3. Melhorar suporte a internacionalização

### Longo Prazo
1. Certificação WCAG 2.1 AA formal
2. Implementar WCAG 2.2 quando finalizado
3. Treinamento regular da equipe

---

## 🤝 Contribuindo

### Para Desenvolvedores

Ao adicionar novos componentes:

1. Consulte este guia
2. Use checklist apropriado
3. Execute testes automatizados
4. Teste manualmente com teclado
5. Documente padrões novos

### Reportando Problemas

Template para issues de acessibilidade:

```markdown
## Descrição
[Descrição clara do problema]

## Critério WCAG Afetado
[Ex: 2.4.7 Focus Visible]

## Passos para Reproduzir
1. [Passo 1]
2. [Passo 2]

## Tecnologia Assistiva Usada
[Ex: NVDA 2023.1, Chrome 120]

## Comportamento Esperado
[O que deveria acontecer]

## Comportamento Atual
[O que acontece atualmente]
```

---

## 📞 Suporte

Para dúvidas sobre acessibilidade:
- Consulte a documentação no repositório
- Revise exemplos em `/templates`
- Execute audit script: `python3 accessibility_audit.py`

---

**Última atualização:** 21 de Janeiro de 2026  
**Versão:** 1.0  
**Mantido por:** Equipe TruK
