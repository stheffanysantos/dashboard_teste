#!/bin/bash

# Atualiza o ambiente e instala o Python
apt-get update && apt-get install -y python3-pip

# Instala as dependências
pip install -r requirements.txt

# Inicia o servidor FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000
