#!/bin/bash

# 🚚 TruK - Virtual Trucking Company Manager
# Quick Start Script

echo "🚚 Iniciando TruK Virtual Trucking Company Manager..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não encontrado. Por favor, instale Python 3."
    exit 1
fi

echo "✅ Python 3 encontrado: $(python3 --version)"
echo ""

# Install dependencies
echo "📦 Instalando dependências..."
pip3 install --user -r requirements.txt

if [ $? -ne 0 ]; then
    echo "⚠️  Erro ao instalar dependências. Tentando continuar..."
fi

echo ""
echo "🔧 Executando migrações do banco de dados..."
python3 manage.py migrate

if [ $? -ne 0 ]; then
    echo "❌ Erro ao executar migrações. Verifique a configuração."
    exit 1
fi

echo ""
echo "📁 Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

echo ""
echo "✅ Setup concluído!"
echo ""
echo "📝 Próximos passos:"
echo "1. Crie um superusuário: python3 manage.py createsuperuser"
echo "2. Inicie o servidor: python3 manage.py runserver"
echo "3. Acesse: http://localhost:8000"
echo ""
echo "🚀 Boa viagem! 🚛"
