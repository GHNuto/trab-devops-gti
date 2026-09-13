from fastapi import FastAPI

app = FastAPI()


@app.get("/olamundo")
def read_root():
    return {"ola": "mundo"}

@app.get("/numerorandom")
def funcaoteste():
    return {"teste": "deucerto"}
