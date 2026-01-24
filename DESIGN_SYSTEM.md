# TruK Design System

Sistema de design moderno para o TruK - Virtual Trucking Company Manager.

## Tema: Road & Fire 🔥

Inspirado nas estradas e na energia do transporte rodoviário.

## Cores

### Cores Primárias
| Nome | Hex | Uso |
|------|-----|-----|
| Primary | `#FF6B35` | Botões principais, links, destaques |
| Primary Dark | `#E55A2B` | Hover states |
| Primary Light | `#FF8A5C` | Backgrounds sutis |

### Cores Secundárias
| Nome | Hex | Uso |
|------|-----|-----|
| Secondary | `#C73E1D` | Acentos, bordas |
| Accent | `#FFB627` | Alertas, ícones |

### Cores Semânticas
| Nome | Hex | Uso |
|------|-----|-----|
| Success | `#34C759` | Confirmações, status positivo |
| Danger | `#FF3B30` | Erros, exclusões |
| Warning | `#FFB627` | Avisos |
| Info | `#007AFF` | Informações |

### Neutros
```
--neutral-900: #1A1A1A  (texto principal)
--neutral-700: #404040  (texto secundário)
--neutral-500: #999999  (texto terciário)
--neutral-300: #E5E5E5  (bordas)
--neutral-100: #F9F9F9  (backgrounds)
```

## Tipografia

- **Font Family:** System UI stack
- **Base Size:** 16px (1rem)

### Escalas
```css
--text-xs: 0.75rem;    /* 12px */
--text-sm: 0.875rem;   /* 14px */
--text-base: 1rem;     /* 16px */
--text-lg: 1.125rem;   /* 18px */
--text-xl: 1.25rem;    /* 20px */
--text-2xl: 1.5rem;    /* 24px */
--text-3xl: 2rem;      /* 32px */
```

## Espaçamento

```css
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
```

## Componentes

### Botões

```html
<!-- Primário -->
<button class="btn btn-primary">Ação Principal</button>

<!-- Secundário -->
<button class="btn btn-secondary">Ação Secundária</button>

<!-- Ghost -->
<button class="btn btn-ghost">Link Style</button>

<!-- Danger -->
<button class="btn btn-danger">Excluir</button>

<!-- Tamanhos -->
<button class="btn btn-primary btn-sm">Pequeno</button>
<button class="btn btn-primary btn-lg">Grande</button>
```

### Cards

```html
<div class="card">
  <div class="card-header">
    <h2 class="card-title">Título</h2>
  </div>
  <div class="card-body">
    Conteúdo do card
  </div>
  <div class="card-footer">
    <button class="btn btn-primary">Ação</button>
  </div>
</div>

<!-- Stat Card -->
<div class="card stat-card">
  <div class="stat-icon">📊</div>
  <div class="stat-content">
    <h3>1,234</h3>
    <p>Total de Cargas</p>
  </div>
</div>
```

### Badges

```html
<span class="badge badge-success">Concluída</span>
<span class="badge badge-warning">Pendente</span>
<span class="badge badge-danger">Falhada</span>
<span class="badge badge-info">Em Andamento</span>
```

### Formulários

```html
<div class="form-group">
  <label class="form-label">Nome</label>
  <input type="text" class="form-input" placeholder="Digite...">
</div>

<div class="form-group">
  <label class="form-label">Opção</label>
  <select class="form-select">
    <option>Selecione...</option>
  </select>
</div>

<div class="form-group">
  <label class="form-label">Descrição</label>
  <textarea class="form-textarea"></textarea>
</div>
```

### Tabelas

```html
<div class="card">
  <div class="card-body" style="padding: 0;">
    <div class="table-container">
      <table class="table">
        <thead>
          <tr>
            <th>Coluna 1</th>
            <th>Coluna 2</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Dado 1</td>
            <td>Dado 2</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
```

### Alertas/Toasts

```html
<div class="alert alert-success">Operação concluída!</div>
<div class="alert alert-error">Erro ao processar.</div>
<div class="alert alert-warning">Atenção!</div>
<div class="alert alert-info">Informação.</div>
```

### Skeletons (Loading)

```html
<div class="skeleton skeleton-text"></div>
<div class="skeleton skeleton-title"></div>
<div class="skeleton skeleton-avatar"></div>
<div class="skeleton skeleton-button"></div>
```

## Layout

### Estrutura Base

```html
<body>
  <div class="app-container">
    <aside class="sidebar">...</aside>
    <div class="main-wrapper">
      <header class="topbar">...</header>
      <main class="content">
        <!-- Page content -->
      </main>
    </div>
  </div>
</body>
```

### Page Header

```html
<div class="page-header">
  <div>
    <h1 class="page-title">Título da Página</h1>
    <p class="text-secondary">Descrição opcional</p>
  </div>
  <div class="page-actions">
    <a href="#" class="btn btn-primary">Ação</a>
  </div>
</div>
```

### Grids

```html
<!-- Stats Grid -->
<div class="stats-grid">
  <div class="card stat-card">...</div>
  <div class="card stat-card">...</div>
</div>

<!-- Dashboard Grid -->
<div class="dashboard-grid">
  <div class="card">...</div>
  <div class="card">...</div>
</div>
```

## Efeitos

### Glassmorphism

```html
<div class="glass">
  Elemento com efeito glass
</div>
```

### Hover Effects

```html
<div class="hover-lift">Sobe no hover</div>
<div class="hover-grow">Cresce no hover</div>
<div class="hover-glow">Brilha no hover</div>
```

### Animações

```html
<div class="fade-in">Aparece suavemente</div>
<div class="slide-in-right">Entra da direita</div>
<div class="stagger-item">Item com delay (usar em listas)</div>
```

## Dark Mode

O tema escuro é ativado automaticamente baseado na preferência do sistema, ou pode ser alternado manualmente via botão no topbar.

```css
/* Variáveis mudam automaticamente */
[data-theme="dark"] {
  --bg-primary: #1A1A1A;
  --neutral-900: #F9F9F9;
  /* etc */
}
```

## Acessibilidade

- **Skip Link:** Navegação rápida para conteúdo principal
- **Focus States:** Indicadores visuais claros
- **Reduced Motion:** Respeita preferência do usuário
- **Touch Targets:** Mínimo 44x44px em dispositivos touch
- **ARIA Labels:** Em elementos interativos

```css
/* Exemplo de uso */
@media (prefers-reduced-motion: reduce) {
  /* Animações desabilitadas */
}
```

## Arquivos CSS

```
static/css/
├── base/
│   ├── reset.css        # Reset CSS
│   ├── variables.css    # Variáveis CSS
│   └── typography.css   # Tipografia
├── components/
│   ├── sidebar.css      # Sidebar navigation
│   ├── topbar.css       # Top bar
│   ├── cards.css        # Cards
│   ├── buttons.css      # Botões
│   ├── forms.css        # Formulários
│   ├── tables.css       # Tabelas
│   ├── badges.css       # Badges
│   ├── toasts.css       # Notificações
│   └── skeletons.css    # Loading states
├── layouts/
│   ├── dashboard.css    # Layout dashboard
│   └── auth.css         # Layout autenticação
├── utils/
│   ├── animations.css   # Animações
│   ├── glassmorphism.css # Efeitos glass
│   ├── utilities.css    # Classes utilitárias
│   └── accessibility.css # Acessibilidade
└── main.css             # Entry point
```

## Breakpoints

```css
/* Mobile First */
@media (min-width: 768px)  { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1280px) { /* Wide */ }
```

## Utilitários

### Display
```html
<div class="hidden">Escondido</div>
<div class="flex">Flexbox</div>
<div class="grid">Grid</div>
```

### Espaçamento
```html
<div class="p-4">Padding</div>
<div class="m-4">Margin</div>
<div class="gap-4">Gap</div>
```

### Texto
```html
<p class="text-center">Centralizado</p>
<p class="text-primary">Cor primária</p>
<p class="text-secondary">Cor secundária</p>
```

---

**Versão:** 1.0  
**Última atualização:** Janeiro 2026
