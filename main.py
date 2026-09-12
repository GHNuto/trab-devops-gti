from fastapi import FastAPI
import random

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/testet1")
def funcaoteste():
    return {"teste": True, "num_aleatorio":random.randint(1,1000)}
