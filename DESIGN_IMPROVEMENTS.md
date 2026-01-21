# 🎨 Design System Improvements - TruK

Este documento descreve as melhorias de design implementadas na branch `feature/design-improvements`.

## 📋 Índice
- [Sistema de Design](#sistema-de-design)
- [Novos Componentes](#novos-componentes)
- [Animações e Efeitos](#animações-e-efeitos)
- [Melhorias de UX](#melhorias-de-ux)
- [Acessibilidade](#acessibilidade)
- [Como Usar](#como-usar)

---

## 🎨 Sistema de Design

### Variáveis CSS (`variables.css`)
Sistema completo de design tokens incluindo:

#### Cores
- **Paleta Primária**: Azul (#2563eb) com variações
- **Cores de Acento**: Laranja (#f59e0b)
- **Estados**: Success, Error, Warning, Info
- **Neutrals**: Escala de cinzas de 50 a 900

#### Tipografia
- **Fonte Base**: System fonts (San Francisco, Segoe UI, etc.)
- **Escalas**: De xs (12px) a 4xl (36px)
- **Pesos**: Normal, Medium, Semibold, Bold
- **Line Heights**: Tight, Normal, Relaxed

#### Espaçamento
- Sistema baseado em múltiplos de 4px
- De spacing-1 (4px) a spacing-16 (64px)

#### Border Radius
- De sm (4px) a 2xl (24px)
- Plus: full (9999px) para círculos

#### Sombras
- 5 níveis: sm, md, lg, xl, 2xl
- Ajustadas para modo escuro

#### Transições
- Fast (150ms), Base (250ms), Slow (350ms)

### Modo Escuro
Sistema completo de tema escuro com:
- Cores invertidas automaticamente
- Contraste otimizado
- Sombras ajustadas
- Ativação via botão flutuante

---

## 🧩 Novos Componentes

### Cards
```html
<div class="card">
    <div class="card-header">
        <div class="card-icon">🚚</div>
        <div>
            <div class="card-title">Total de Cargas</div>
            <div class="card-value">1,234</div>
        </div>
    </div>
</div>
```

**Variações**:
- `.card` - Card básico com hover effect
- `.stat-card` - Card de estatística com barra colorida
- `.metric-card` - Card de métrica com ícone grande
- `.glass` - Card com efeito glassmorphism

### Botões
```html
<button class="btn-primary">Botão Primário</button>
<button class="btn-secondary">Botão Secundário</button>
```

**Features**:
- Gradientes animados
- Hover effects (elevação)
- Ripple effect ao clicar
- Loading state automático em forms

### Forms com Floating Labels
```html
<div class="form-floating">
    <input type="text" class="form-input" placeholder=" " id="name">
    <label for="name" class="form-label">Nome</label>
</div>
```

**Features**:
- Label anima ao focar/preencher
- Validação inline com feedback visual
- Estados de erro com mensagens
- Suporte a todos os tipos de input

### Badges
```html
<span class="badge badge-success">Concluída</span>
<span class="badge badge-warning">Pendente</span>
<span class="badge badge-error">Falhada</span>
```

### Alerts
```html
<div class="alert alert-success">
    Operação realizada com sucesso!
</div>
```

**Features**:
- Auto-dismiss após 5 segundos
- Animação de entrada/saída
- Ícones contextuais

### Tabelas
```html
<table class="table">
    <thead>
        <tr>
            <th>Coluna 1</th>
            <th>Coluna 2</th>
        </tr>
    </thead>
    <tbody>
        <tr data-href="/detalhes/1">
            <td>Dados</td>
            <td>Dados</td>
        </tr>
    </tbody>
</table>
```

**Features**:
- Hover effects em linhas
- Clique em linhas para navegar (via data-href)
- Design moderno com gradientes
- Responsivas com scroll horizontal

---

## ✨ Animações e Efeitos

### Animações Disponíveis

#### Entrada
- `.fade-in` - Fade in suave
- `.slide-in-left/right/up/down` - Desliza de diferentes direções
- `.scale-in` - Cresce do centro
- `.flip-in` - Gira em 3D

#### Loops
- `.pulse` - Pulsa suavemente
- `.bounce` - Salta
- `.rotate` - Rotaciona continuamente
- `.floating` - Flutua para cima e baixo

#### Interação
- `.shake` - Tremor (útil para erros)
- `.ripple` - Efeito ripple ao clicar
- `.shine-effect` - Brilho ao passar mouse

#### Especiais
- `.gradient-bg` - Background com gradiente animado
- `.gradient-border` - Borda com gradiente animado
- `.glow` - Efeito de brilho/neon
- `.neon` - Texto neon

### Micro-interações

#### Cards
- Elevam ao passar mouse
- Animam ao entrar na viewport
- Stagger animation em listas

#### Botões
- Elevam ao hover
- Ripple effect ao clicar
- Loading state automático em submits

#### Forms
- Labels flutuantes animadas
- Validação inline com animações
- Feedback visual em tempo real

---

## 🎯 Melhorias de UX

### 1. Dashboard Aprimorado
- **Stats Grid**: Cards de estatísticas com gradientes e ícones
- **Gráficos Modernos**: Containers estilizados com filtros
- **Activity Feed**: Lista de atividades recentes com ícones
- **Progress Bars**: Barras de progresso animadas

### 2. Navegação
- **Dropdown Menu**: Menu dropdown animado
- **Skip Links**: Links de pulo para acessibilidade
- **Sticky Navbar**: Navbar que fica fixo ao rolar

### 3. Feedback Visual
- **Toast Notifications**: Notificações temporárias no canto
- **Loading States**: Spinners e skeleton screens
- **Empty States**: Estados vazios bonitos e informativos
- **Error Messages**: Mensagens de erro contextuais

### 4. Interações
- **Smooth Scroll**: Rolagem suave para âncoras
- **Keyboard Navigation**: Navegação completa via teclado
- **Focus Visible**: Estados de foco claros
- **Hover Effects**: Efeitos em todos elementos interativos

---

## ♿ Acessibilidade

### Implementações

1. **Contraste de Cores**
   - Todas as combinações atendem WCAG AAA
   - Modo escuro otimizado

2. **Navegação por Teclado**
   - Tab order lógico
   - Focus indicators visíveis
   - Escape para fechar modals/dropdowns

3. **Screen Readers**
   - ARIA labels em todos componentes
   - Roles semânticos corretos
   - Live regions para atualizações dinâmicas

4. **Reduced Motion**
   - Respeita `prefers-reduced-motion`
   - Animações desabilitadas quando necessário

5. **Skip Links**
   - Link de pulo para conteúdo principal
   - Visível ao focar

---

## 🚀 Como Usar

### 1. Arquivos Criados

```
static/
├── css/
│   ├── variables.css      # Design tokens
│   ├── style.css          # Estilos base e componentes
│   ├── dashboard.css      # Estilos específicos do dashboard
│   └── animations.css     # Animações e efeitos
└── js/
    └── main.js            # Interações e funcionalidades
```

### 2. Já Incluído no Base Template

Os arquivos já estão linkados em `templates/base/base.html`:

```html
<link rel="stylesheet" href="{% static 'css/variables.css' %}">
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<link rel="stylesheet" href="{% static 'css/dashboard.css' %}">
<script src="{% static 'js/main.js' %}"></script>
```

### 3. Usando Componentes

#### Card Simples
```html
<div class="card">
    <h3>Título</h3>
    <p>Conteúdo do card</p>
</div>
```

#### Card de Estatística
```html
<div class="stat-card success">
    <div class="stat-icon">✅</div>
    <div class="stat-label">Entregas Completas</div>
    <div class="stat-value">1,234</div>
    <div class="stat-change positive">
        ↑ 12.5% vs. mês anterior
    </div>
</div>
```

#### Form com Validação
```html
<form>
    <div class="form-group">
        <label class="form-label" for="email">Email</label>
        <input type="email" class="form-input" id="email" required>
    </div>
    <button type="submit" class="btn-primary">Enviar</button>
</form>
```

#### Grid Responsivo
```html
<div class="grid grid-3">
    <div class="card">Card 1</div>
    <div class="card">Card 2</div>
    <div class="card">Card 3</div>
</div>
```

### 4. JavaScript Features

#### Dark Mode Toggle
Automaticamente criado e funcional. Toggle salvo em localStorage.

#### Form Validation
Automática em todos os forms. Validação inline com feedback visual.

#### Toast Notification
```javascript
showToast('Mensagem de sucesso!', 'success');
showToast('Erro ao processar', 'error');
```

#### Copy to Clipboard
```javascript
copyToClipboard('Texto para copiar');
```

---

## 📱 Responsividade

### Breakpoints
- **Mobile**: < 768px
- **Tablet**: 768px - 1199px
- **Desktop**: ≥ 1200px

### Adaptações Mobile
- Navbar colapsável
- Cards em coluna única
- Tabelas com scroll horizontal
- Formulários full-width
- Grids adaptados

---

## 🎨 Temas

### Tema Claro (Padrão)
- Background: Cinza claro (#f9fafb)
- Surface: Branco
- Texto: Cinza escuro

### Tema Escuro
- Background: Cinza escuro (#111827)
- Surface: Cinza médio (#1f2937)
- Texto: Branco/Cinza claro

**Toggle**: Botão flutuante no canto inferior direito

---

## 🔧 Customização

### Modificar Cores
Edite `static/css/variables.css`:

```css
:root {
    --color-primary: #seu-azul;
    --color-accent: #seu-laranja;
}
```

### Adicionar Nova Animação
Em `static/css/animations.css`:

```css
@keyframes minhaAnimacao {
    from { /* estado inicial */ }
    to { /* estado final */ }
}

.minha-classe {
    animation: minhaAnimacao 1s ease-out;
}
```

---

## 📊 Performance

### Otimizações Implementadas
- CSS moderno (custom properties)
- Animations com GPU (transform, opacity)
- Lazy loading de cards (Intersection Observer)
- Debouncing em inputs
- Transition apenas em propriedades necessárias

---

## 🐛 Compatibilidade

### Navegadores Suportados
- ✅ Chrome/Edge 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Opera 76+

### Features Modernas Usadas
- CSS Custom Properties
- CSS Grid & Flexbox
- Intersection Observer API
- LocalStorage API
- CSS Animations

---

## 📚 Referências

- [Design System](https://www.designsystems.com/)
- [Material Design](https://material.io/design)
- [Tailwind CSS](https://tailwindcss.com/)
- [Animate.css](https://animate.style/)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

---

## 🤝 Contribuindo

Para adicionar novos componentes ou melhorias:

1. Siga o sistema de design tokens em `variables.css`
2. Mantenha consistência com componentes existentes
3. Teste em diferentes tamanhos de tela
4. Garanta acessibilidade (WCAG AA mínimo)
5. Adicione animações com `prefers-reduced-motion`
6. Documente no README

---

**Desenvolvido com ❤️ para TruK - Virtual Trucking Company**
