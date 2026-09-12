from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/testet1")
def funcaoteste():
    return {"teste": "deucerto"}
