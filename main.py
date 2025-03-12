from fastapi import FastAPI, Query

app = FastAPI()

# Carregar o conteúdo do arquivo de texto
with open("base_de_conhecimento.txt", "r", encoding="utf-8") as f:
    knowledge_base = f.read()

@app.get("/consultar")
def consultar(pergunta: str):
    """
    Simples mecanismo de busca no texto: retorna frases que contêm a palavra-chave da pergunta.
    """
    resposta = [linha for linha in knowledge_base.split("\n") if pergunta.lower() in linha.lower()]
    return {"resposta": resposta[:5] if resposta else "Não encontrei informações relevantes."}
