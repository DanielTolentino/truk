# 🎯 TruK - Funcionalidades Detalhadas

## 📋 Índice
1. [Dashboard](#dashboard)
2. [Gestão de Cargas](#gestão-de-cargas)
3. [Analytics](#analytics)
4. [Autenticação](#autenticação)
5. [Admin Panel](#admin-panel)

---

## 🏠 Dashboard

### Visão Geral
O dashboard principal mostra uma visão consolidada de toda a operação:

**Cards de Estatísticas:**
- 📦 Total de Cargas
- ✅ Cargas Concluídas
- 🚚 Cargas em Andamento
- 🛣️ Distância Total (km)
- 💰 Receita Total (€)
- ⚠️ Total de Multas (€)
- 📊 Lucro Líquido (€)
- ⛽ Combustível Consumido (L)

**Gráficos Interativos:**
- Gráfico de barras: Cargas por mês (últimos 6 meses)
- Lista de cargas recentes (últimas 5)
- Top 5 rotas mais utilizadas com receita

**Funcionalidades:**
- Atualização em tempo real
- Dados filtrados por usuário (motorista vê apenas suas cargas)
- Admins vêem dados consolidados de todos

---

## 🚛 Gestão de Cargas

### 1. Criar Nova Carga

**Campos Obrigatórios:**
- Cidade de Origem
- País de Origem
- Cidade de Destino
- País de Destino
- Tipo de Carga
- Distância (km)
- Pagamento (€)

**Campos Opcionais:**
- Tipo de Trailer (9 opções: Curtain, Box, Reefer, Flatbed, etc.)
- Peso (toneladas)
- Combustível consumido (litros)
- Tempo de viagem (HH:MM:SS)
- Dano recebido (%)
- Multas (€)
- Status
- Screenshot da entrega
- Notas adicionais

### 2. Listar Cargas

**Visualização:**
- Tabela com todas as cargas
- Status badge colorido
- Informações principais visíveis
- Botões de ação (Ver, Editar)

**Filtros Disponíveis:**
- Por status (pendente, em andamento, concluída, falhada)
- Busca por origem, destino, tipo de carga, motorista

**Paginação:**
- 20 cargas por página
- Navegação entre páginas

### 3. Detalhes da Carga

**Informações Exibidas:**
- Rota completa (origem → destino)
- Informações da carga (tipo, trailer, peso)
- Financeiro (pagamento, multas, lucro líquido)
- Detalhes técnicos (dano, eficiência, combustível)
- Datas (criação, início, conclusão)
- Informações do motorista
- Screenshot (se disponível)
- Notas

**Ações Disponíveis:**
- Editar carga
- Deletar carga
- Alterar status:
  - Pendente → Iniciar
  - Em Andamento → Concluir ou Falhar

### 4. Editar Carga

- Formulário pré-preenchido
- Todos os campos editáveis
- Validação de dados
- Mensagem de sucesso/erro

### 5. Deletar Carga

- Soft delete (não apaga do banco)
- Confirmação antes de deletar
- Mensagem de sucesso

---

## 📊 Analytics

### Página de Analytics Avançado

**Gráficos:**

1. **Evolução da Receita (12 meses)**
   - Gráfico de linha interativo
   - Mostra tendência de crescimento
   - Valores mensais

2. **Análise por Tipo de Trailer**
   - Quantidade de cargas por trailer
   - Receita total por tipo
   - Dano médio por tipo

3. **Top 10 Países de Origem**
   - Quantidade de cargas
   - Receita total

4. **Top 10 Países de Destino**
   - Quantidade de cargas
   - Receita total

5. **Performance por Motorista** (Admin Only)
   - Quantidade de cargas por motorista
   - Receita total
   - Dano médio

**Interatividade:**
- Gráficos com zoom
- Tooltips informativos
- Dados atualizados em tempo real

---

## 🔐 Autenticação

### 1. Login
- Formulário simples (username + password)
- Validação de credenciais
- Redirecionamento para dashboard
- Mensagens de erro claras

### 2. Registro
- Campos: username, email, nome, sobrenome, senha
- Validação de senha forte
- Confirmação de senha
- Criação automática como "motorista"
- Login automático após registro

### 3. Perfil de Usuário
**Visualização:**
- Avatar (ou placeholder)
- Nome completo
- Role (motorista/admin)
- Email
- Data de entrada
- Bio

**Edição:**
- Atualizar nome
- Alterar email
- Upload de avatar
- Editar bio

### 4. Sistema de Roles

**Motorista:**
- Ver apenas suas cargas
- Criar novas cargas
- Editar suas cargas
- Ver seu próprio dashboard

**Admin:**
- Ver todas as cargas
- Editar qualquer carga
- Ver dashboard consolidado
- Acessar analytics com performance de motoristas
- Acessar admin panel

---

## ⚙️ Admin Panel

### Acesso: `/admin/`

**Funcionalidades:**

1. **Gestão de Usuários**
   - Criar/editar/deletar usuários
   - Alterar roles
   - Resetar senhas
   - Ver informações completas

2. **Gestão de Cargas**
   - CRUD completo
   - Filtros avançados
   - Busca por múltiplos campos
   - Ordenação customizada
   - Ações em lote

3. **Painel de Controle**
   - Estatísticas gerais
   - Logs de atividade
   - Informações do sistema

---

## 🎨 Design e UX

### Interface

**Navbar:**
- Logo clicável
- Links principais (Dashboard, Cargas, Analytics)
- Botão "Nova Carga" destacado
- Menu de usuário com dropdown

**Cards:**
- Design moderno com sombras
- Ícones grandes e claros
- Cores temáticas por tipo
- Hover effects

**Tabelas:**
- Responsivas
- Hover em linhas
- Status badges coloridos
- Ações inline

**Formulários:**
- Campos organizados em fieldsets
- Labels claras
- Placeholders informativos
- Validação visual
- Mensagens de erro contextuais

**Gráficos:**
- Plotly.js para interatividade
- Cores consistentes com tema
- Responsivos
- Tooltips informativos

### Responsividade

- ✅ Desktop (1200px+)
- ✅ Tablet (768px - 1199px)
- ✅ Mobile (< 768px)

**Adaptações Mobile:**
- Navbar colapsável
- Cards em coluna única
- Tabelas com scroll horizontal
- Formulários adaptados
- Botões full-width

---

## 🔒 Segurança

### Implementado:

1. **Autenticação Django**
   - Hash de senhas (PBKDF2)
   - Session-based authentication
   - CSRF protection

2. **Permissões**
   - LoginRequiredMixin em todas as views
   - Verificação de ownership (motorista vê apenas suas cargas)
   - Admin checks

3. **Validação**
   - Forms com validação server-side
   - Sanitização de inputs
   - Prevenção de SQL injection (ORM)

4. **Soft Delete**
   - Dados não são apagados fisicamente
   - Possibilidade de recuperação
   - Auditoria completa

---

## 📱 Tecnologias Utilizadas

**Backend:**
- Django 5.0
- Python 3.10+
- PostgreSQL / SQLite

**Frontend:**
- HTML5
- CSS3 (Custom)
- JavaScript (Plotly.js)
- HTMX (básico)

**Bibliotecas:**
- django-widget-tweaks (formulários)
- python-decouple (config)
- Pillow (imagens)
- Plotly (gráficos)
- Pandas (análises)

---

## 🚀 Performance

### Otimizações Implementadas:

1. **Database:**
   - Índices automáticos em ForeignKeys
   - Select_related para queries otimizadas
   - Aggregate queries para estatísticas

2. **Static Files:**
   - WhiteNoise para servir arquivos
   - Compressão automática
   - Cache headers

3. **Queries:**
   - Apenas dados necessários
   - Paginação para listas grandes
   - Soft delete queries filtradas

---

## 📈 Métricas Calculadas

### Automáticas:

1. **Lucro Líquido**
   - Fórmula: Pagamento - Multas
   - Calculado em tempo real

2. **Eficiência**
   - Fórmula: 100 - Dano%
   - Quanto menos dano, maior eficiência

3. **Estatísticas Agregadas**
   - Total de km rodados
   - Receita total
   - Média de dano
   - Total de combustível

---

## 🎯 Casos de Uso

### Exemplo 1: Motorista Registrando Carga

1. Login no sistema
2. Clica em "+ Nova Carga"
3. Preenche origem: Lisboa, Portugal
4. Preenche destino: Paris, França
5. Tipo: Madeira, Trailer: Flatbed
6. Distância: 1850 km, Pagamento: €2400
7. Após entrega, adiciona dano: 2%, Combustível: 450L
8. Upload screenshot
9. Salva como "Concluída"

### Exemplo 2: Admin Analisando Performance

1. Login como admin
2. Acessa "Analytics"
3. Vê evolução de receita mensal
4. Identifica melhor motorista
5. Analisa rotas mais rentáveis
6. Toma decisões baseadas em dados

### Exemplo 3: Acompanhamento de Carga

1. Motorista cria carga "Pendente"
2. Ao iniciar viagem, muda para "Em Andamento"
3. Durante viagem, pode editar notas
4. Ao finalizar, muda para "Concluída"
5. Adiciona dados finais (dano, combustível)
6. Upload screenshot da entrega

---

## 💡 Dicas de Uso

1. **Organização:**
   - Use notas para informações extras
   - Upload screenshots para documentar
   - Mantenha status atualizados

2. **Análise:**
   - Verifique dashboard regularmente
   - Compare rotas no analytics
   - Identifique padrões de dano

3. **Eficiência:**
   - Use filtros para encontrar cargas
   - Paginação para navegar histórico
   - Busca por cidade/tipo

---

Desenvolvido com ❤️ para a comunidade ETS2
