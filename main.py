from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/olamundo")
def read_root():
    return {"ola": "mundo"}

@app.get("/numerorandom")
def funcaoteste():
    return {"teste": True, "num_aleatorio":random.randint(1,1000)}
