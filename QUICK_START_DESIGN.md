# 🎨 Guia de Uso Rápido - Design System TruK

## 📌 Exemplos Práticos

### 1. Card Básico
```html
<div class="card fade-in">
    <h3>Título do Card</h3>
    <p>Conteúdo do card com informações relevantes.</p>
    <button class="btn-primary">Ação</button>
</div>
```

### 2. Card de Estatística Completo
```html
<div class="stat-card success">
    <div class="stat-icon">✅</div>
    <div class="stat-label">Entregas Concluídas</div>
    <div class="stat-value">1,234</div>
    <div class="stat-change positive">
        ↑ 12.5% vs. mês anterior
    </div>
    <div class="progress-bar" style="margin-top: var(--spacing-3);">
        <div class="progress-fill success" style="width: 85%;"></div>
    </div>
</div>
```

### 3. Formulário Moderno com Floating Labels
```html
<form class="card">
    <h2>Registrar Nova Carga</h2>
    
    <div class="form-floating">
        <input type="text" class="form-input" id="origem" placeholder=" " required>
        <label class="form-label" for="origem">Cidade de Origem</label>
    </div>
    
    <div class="form-floating">
        <input type="text" class="form-input" id="destino" placeholder=" " required>
        <label class="form-label" for="destino">Cidade de Destino</label>
    </div>
    
    <div class="form-group">
        <label class="form-label" for="tipo">Tipo de Carga</label>
        <select class="form-select" id="tipo" required>
            <option value="">Selecione...</option>
            <option value="madeira">Madeira</option>
            <option value="metal">Metal</option>
            <option value="alimentos">Alimentos</option>
        </select>
    </div>
    
    <div class="grid grid-2">
        <div class="form-group">
            <label class="form-label" for="distancia">Distância (km)</label>
            <input type="number" class="form-input" id="distancia" min="0" required>
        </div>
        
        <div class="form-group">
            <label class="form-label" for="pagamento">Pagamento (€)</label>
            <input type="number" class="form-input" id="pagamento" min="0" step="0.01" required>
        </div>
    </div>
    
    <button type="submit" class="btn-primary ripple">
        Registrar Carga
    </button>
</form>
```

### 4. Tabela Responsiva com Ações
```html
<div class="card">
    <h2>Minhas Cargas Recentes</h2>
    
    <table class="table">
        <thead>
            <tr>
                <th>Rota</th>
                <th>Tipo</th>
                <th>Status</th>
                <th>Pagamento</th>
                <th>Ações</th>
            </tr>
        </thead>
        <tbody>
            <tr data-href="/cargas/1/">
                <td>
                    <strong>Lisboa → Paris</strong>
                    <br>
                    <small style="color: var(--text-secondary);">1,850 km</small>
                </td>
                <td>Madeira</td>
                <td>
                    <span class="badge badge-success">Concluída</span>
                </td>
                <td>
                    <strong style="color: var(--color-success);">€2,400</strong>
                </td>
                <td>
                    <button class="btn-secondary" style="padding: var(--spacing-1) var(--spacing-3);">
                        Ver
                    </button>
                </td>
            </tr>
            
            <tr data-href="/cargas/2/">
                <td>
                    <strong>Madrid → Berlin</strong>
                    <br>
                    <small style="color: var(--text-secondary);">2,300 km</small>
                </td>
                <td>Metal</td>
                <td>
                    <span class="badge badge-warning">Em Andamento</span>
                </td>
                <td>
                    <strong style="color: var(--color-success);">€3,200</strong>
                </td>
                <td>
                    <button class="btn-secondary" style="padding: var(--spacing-1) var(--spacing-3);">
                        Ver
                    </button>
                </td>
            </tr>
        </tbody>
    </table>
</div>
```

### 5. Dashboard com Grid Responsivo
```html
<!-- Stats Grid -->
<div class="stats-grid">
    <div class="stat-card">
        <div class="stat-icon">📦</div>
        <div class="stat-label">Total de Cargas</div>
        <div class="stat-value">1,234</div>
    </div>
    
    <div class="stat-card success">
        <div class="stat-icon">✅</div>
        <div class="stat-label">Concluídas</div>
        <div class="stat-value">890</div>
    </div>
    
    <div class="stat-card warning">
        <div class="stat-icon">🚛</div>
        <div class="stat-label">Em Andamento</div>
        <div class="stat-value">45</div>
    </div>
    
    <div class="stat-card error">
        <div class="stat-icon">❌</div>
        <div class="stat-label">Falhadas</div>
        <div class="stat-value">12</div>
    </div>
</div>

<!-- 2-Column Layout -->
<div class="dashboard-grid">
    <!-- Main Content (2/3) -->
    <div style="grid-column: span 2;">
        <div class="chart-container">
            <div class="chart-header">
                <h2 class="chart-title">Evolução Mensal</h2>
            </div>
            <!-- Chart here -->
        </div>
    </div>
    
    <!-- Sidebar (1/3) -->
    <div>
        <div class="chart-container">
            <h3 class="chart-title">Atividades</h3>
            <ul class="activity-list">
                <li class="activity-item">
                    <div class="activity-icon">✅</div>
                    <div class="activity-content">
                        <div class="activity-title">Carga Entregue</div>
                        <div class="activity-meta">
                            <span>Lisboa → Paris</span>
                            <span class="activity-time">há 2h</span>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>
```

### 6. Alerts e Notificações
```html
<!-- Alert Success -->
<div class="alert alert-success">
    ✅ Carga registrada com sucesso!
</div>

<!-- Alert Error -->
<div class="alert alert-error">
    ❌ Erro ao processar requisição. Tente novamente.
</div>

<!-- Alert Warning -->
<div class="alert alert-warning">
    ⚠️ Atenção: Esta carga possui multas pendentes.
</div>

<!-- Alert Info -->
<div class="alert alert-info">
    ℹ️ Dica: Você pode adicionar screenshots das entregas.
</div>
```

### 7. Loading States
```html
<!-- Skeleton Loading -->
<div class="skeleton-card">
    <div class="skeleton-text large"></div>
    <div class="skeleton-text"></div>
    <div class="skeleton-text small"></div>
</div>

<!-- Spinner -->
<div style="display: flex; justify-content: center; padding: var(--spacing-8);">
    <div class="spinner"></div>
</div>

<!-- Dots Loading -->
<div style="display: flex; justify-content: center; padding: var(--spacing-8);">
    <div class="dots-loading">
        <span></span>
        <span></span>
        <span></span>
    </div>
</div>
```

### 8. Efeitos Especiais
```html
<!-- Glassmorphism Card -->
<div class="card glass">
    <h3>Card com Efeito Vidro</h3>
    <p>Backdrop blur e transparência</p>
</div>

<!-- Gradient Text -->
<h1 class="gradient-text">
    Texto com Gradiente Colorido
</h1>

<!-- Card com Brilho -->
<div class="card shine-effect">
    <h3>Card com Shine Effect</h3>
    <p>Passa o mouse para ver o brilho</p>
</div>

<!-- Card 3D -->
<div class="card card-3d">
    <h3>Card com Efeito 3D</h3>
    <p>Rotação ao passar o mouse</p>
</div>

<!-- Gradient Border Animado -->
<div class="gradient-border" style="padding: var(--spacing-6);">
    <h3>Borda com Gradiente Animado</h3>
    <p>Cores em movimento</p>
</div>
```

### 9. Animações de Entrada
```html
<!-- Fade In -->
<div class="fade-in">
    Aparece suavemente
</div>

<!-- Slide In -->
<div class="slide-in-left">Entra pela esquerda</div>
<div class="slide-in-right">Entra pela direita</div>
<div class="slide-in-up">Entra de baixo</div>
<div class="slide-in-down">Entra de cima</div>

<!-- Scale In -->
<div class="scale-in">
    Cresce do centro
</div>

<!-- Bounce -->
<button class="btn-primary bounce">
    Botão com Bounce
</button>

<!-- Floating -->
<div class="floating">
    🚚 Elemento Flutuante
</div>
```

### 10. Tooltip
```html
<span class="tooltip" data-tooltip="Esta é uma dica útil!">
    Passe o mouse aqui
</span>
```

### 11. Progress Circle
```html
<div class="progress-circle" style="--progress: 75;">
    <div class="progress-circle-value">75%</div>
</div>
```

### 12. Empty State
```html
<div class="empty-state">
    <div class="empty-state-icon">📭</div>
    <div class="empty-state-title">Nenhuma carga encontrada</div>
    <div class="empty-state-text">
        Você ainda não registrou nenhuma carga. Comece agora!
    </div>
    <a href="/cargas/nova/" class="btn-primary">
        + Nova Carga
    </a>
</div>
```

## 🎭 JavaScript Interativo

### Toast Notification
```javascript
// Sucesso
showToast('Operação concluída com sucesso!', 'success');

// Erro
showToast('Erro ao processar requisição', 'error');

// Info
showToast('Informação importante', 'info');

// Warning
showToast('Atenção necessária', 'warning');
```

### Copy to Clipboard
```javascript
copyToClipboard('Texto para copiar');
```

### Validação Manual
```javascript
const input = document.getElementById('meuInput');
const isValid = validateField(input);

if (!isValid) {
    showFieldError(input, 'Mensagem de erro customizada');
} else {
    removeFieldError(input);
}
```

## 🎨 Customização de Cores

### Via CSS Variables
```css
/* No seu CSS customizado */
:root {
    --color-primary: #1e40af;  /* Seu azul */
    --color-accent: #d97706;   /* Seu laranja */
}
```

### Via Inline Style
```html
<div class="stat-card" style="--color-primary: #8b5cf6;">
    Card com cor customizada
</div>
```

## 📱 Classes Utilitárias

### Espaçamento
```html
<div style="margin-bottom: var(--spacing-4);">
<div style="padding: var(--spacing-6);">
<div style="gap: var(--spacing-3);">
```

### Tipografia
```html
<h1 style="font-size: var(--font-size-4xl); font-weight: var(--font-weight-bold);">
<p style="font-size: var(--font-size-sm); color: var(--text-secondary);">
```

### Cores
```html
<div style="background: var(--bg-surface); color: var(--text-primary);">
<span style="color: var(--color-success);">Texto verde</span>
<span style="color: var(--color-error);">Texto vermelho</span>
```

## ⚡ Dicas de Performance

1. **Use animações com transform/opacity**: São renderizadas na GPU
2. **Prefira CSS animations a JavaScript**: Melhor performance
3. **Use Intersection Observer**: Para animar apenas quando visível
4. **Debounce inputs**: Evite validação em cada tecla

## 🎯 Boas Práticas

1. **Sempre use variáveis CSS**: Mantém consistência
2. **Adicione animações sutis**: Não exagere
3. **Teste em diferentes telas**: Use DevTools responsive
4. **Respeite prefers-reduced-motion**: Já implementado
5. **Mantenha acessibilidade**: Use ARIA labels

---

**Para mais detalhes, consulte DESIGN_IMPROVEMENTS.md**
