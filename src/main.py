from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/olamundo")
async def read_root():
    return {"ola": "mundo"}

@app.get("/numerorandom")
async def funcaoteste():
    return {"teste": True, "num_aleatorio":random.randint(1,1000)}

@app.get("/dado")
async def jogar_dado():
    return {"resultado_dado": random.randint(1, 6)}

@app.get("/saudacao/{nome}")
async def saudacao_personalizada(nome: str):
    return {"mensagem": f"Olá, {nome}! Seja bem-vindo à API."}

@app.get("/status")
async def checar_status():
    return {"status": "online", "servidor": "funcionando perfeitamente"}
