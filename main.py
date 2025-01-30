import subprocess
from fastapi import FastAPI
from threading import Thread

app = FastAPI()

def run_streamlit():
    """Executa o Streamlit em uma thread separada"""
    subprocess.run(["streamlit", "run", "app.py", "--server.port=8501", "--server.headless=true"])

# Inicia o Streamlit quando o backend for iniciado
Thread(target=run_streamlit, daemon=True).start()

@app.get("/")
def read_root():
    return {"message": "Backend rodando! Acesse /streamlit para abrir a interface."}

