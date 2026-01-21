# 🚀 Guia Rápido de Instalação - TruK

## Opção 1: Instalação Rápida (SQLite)

### 1. Instalar dependências do sistema
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Ou instalar apenas o necessário para Django
pip3 install --user django django-htmx python-decouple pillow django-widget-tweaks plotly pandas
```

### 2. Executar migrações
```bash
cd /home/daniel/dev/truk
python3 manage.py migrate
```

### 3. Criar superusuário
```bash
python3 manage.py createsuperuser
```

### 4. Coletar arquivos estáticos
```bash
python3 manage.py collectstatic --noinput
```

### 5. Rodar o servidor
```bash
python3 manage.py runserver
```

Acesse: http://localhost:8000

---

## Opção 2: Instalação Completa (com venv e PostgreSQL)

### 1. Criar ambiente virtual
```bash
# Instalar python3-venv se necessário
sudo apt install python3.12-venv

# Criar e ativar venv
cd /home/daniel/dev/truk
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Configurar PostgreSQL (opcional)
```bash
# Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# Criar banco
sudo -u postgres psql
```

No psql:
```sql
CREATE DATABASE truk_db;
CREATE USER truk_user WITH PASSWORD 'sua-senha';
GRANT ALL PRIVILEGES ON DATABASE truk_db TO truk_user;
\q
```

### 4. Configurar .env
Edite o arquivo `.env` e altere:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=truk_db
DB_USER=truk_user
DB_PASSWORD=sua-senha
DB_HOST=localhost
DB_PORT=5432
```

### 5. Executar migrações
```bash
python manage.py migrate
```

### 6. Criar superusuário
```bash
python manage.py createsuperuser
```

### 7. Coletar arquivos estáticos
```bash
python manage.py collectstatic --noinput
```

### 8. Rodar o servidor
```bash
python manage.py runserver
```

---

## Comandos Úteis

### Ver estrutura do projeto
```bash
tree -I '__pycache__|*.pyc|venv|staticfiles|media' -L 3
```

### Fazer backup do banco
```bash
python manage.py dumpdata > backup.json
```

### Carregar backup
```bash
python manage.py loaddata backup.json
```

### Criar nova migração
```bash
python manage.py makemigrations
python manage.py migrate
```

### Limpar sessões antigas
```bash
python manage.py clearsessions
```

---

## Troubleshooting

### Erro: No module named 'decouple'
```bash
pip3 install --user python-decouple
```

### Erro: No module named 'PIL'
```bash
pip3 install --user Pillow
```

### Erro: Cannot import HTMX
```bash
pip3 install --user django-htmx
```

### Porta 8000 já em uso
```bash
# Use outra porta
python manage.py runserver 8080

# Ou mate o processo
sudo lsof -t -i tcp:8000 | xargs kill -9
```

---

## Próximos Passos

1. ✅ Faça login com o superusuário
2. ✅ Acesse o admin em `/admin/`
3. ✅ Crie alguns usuários motoristas
4. ✅ Registre algumas cargas
5. ✅ Veja as estatísticas no dashboard

**Divirta-se! 🚚**
