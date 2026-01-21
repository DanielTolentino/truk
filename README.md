# 🚚 TruK - Virtual Trucking Company Manager (ETS2)

Sistema web completo para gerenciar, registrar, analisar e acompanhar cargas de uma empresa de transporte virtual no Euro Truck Simulator 2.

## 🎯 Funcionalidades

- ✅ Sistema de autenticação (Motoristas e Admin)
- ✅ Registro detalhado de cargas/fretes
- ✅ Dashboard com análises e estatísticas
- ✅ Gráficos interativos de performance
- ✅ Upload de screenshots das entregas
- ✅ Acompanhamento de status em tempo real
- ✅ Interface moderna com HTMX

## 🛠️ Stack Tecnológico

- **Backend**: Django 5.0
- **Frontend**: Django Templates + HTMX
- **Database**: PostgreSQL
- **Charts**: Plotly
- **Styles**: CSS customizado

## 📋 Pré-requisitos

- Python 3.10+
- PostgreSQL 14+
- pip

## 🚀 Instalação

### 1. Clone o repositório
```bash
git clone <repository-url>
cd truk
```

### 2. Crie e ative o ambiente virtual
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o PostgreSQL

Crie o banco de dados:
```bash
sudo -u postgres psql
```

No psql:
```sql
CREATE DATABASE truk_db;
CREATE USER truk_user WITH PASSWORD 'your-password';
ALTER ROLE truk_user SET client_encoding TO 'utf8';
ALTER ROLE truk_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE truk_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE truk_db TO truk_user;
\q
```

### 5. Configure as variáveis de ambiente

Copie o arquivo de exemplo:
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações.

### 6. Execute as migrações
```bash
python manage.py migrate
```

### 7. Crie um superusuário
```bash
python manage.py createsuperuser
```

### 8. Colete os arquivos estáticos
```bash
python manage.py collectstatic --noinput
```

### 9. Execute o servidor
```bash
python manage.py runserver
```

Acesse: http://localhost:8000

## 📁 Estrutura do Projeto

```
truk/
├── manage.py
├── requirements.txt
├── .env.example
├── README.md
├── config/                 # Configurações Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── accounts/          # Autenticação e usuários
│   ├── loads/             # Gestão de cargas
│   └── dashboard/         # Analytics e dashboards
├── static/                # CSS, JS, imagens
├── templates/             # Templates HTML
└── media/                 # Uploads (screenshots)
```

## 🎮 Como Usar

1. **Login**: Acesse com suas credenciais
2. **Registrar Carga**: Clique em "Nova Carga" e preencha os dados do frete
3. **Dashboard**: Visualize estatísticas e gráficos
4. **Minhas Cargas**: Veja histórico completo de entregas

## 📊 Campos de Registro

### Informações Básicas
- Origem (cidade/país)
- Destino (cidade/país)
- Tipo de carga
- Distância (km)
- Pagamento (€)

### Informações Avançadas
- Tipo de trailer
- Peso da carga (toneladas)
- Dano recebido (%)
- Combustível consumido (litros)
- Tempo de viagem
- Multas recebidas
- Status da entrega
- Screenshots
- Notas adicionais

## 🔐 Segurança

- Nunca commite o arquivo `.env`
- Altere o `SECRET_KEY` em produção
- Use senhas fortes para o banco de dados
- Configure `DEBUG=False` em produção

## 📝 Licença

MIT License

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 📧 Contato

Para dúvidas ou sugestões, abra uma issue no GitHub.

---

**Desenvolvido com ❤️ para a comunidade ETS2**
