from fastapi import FastAPI

app = FastAPI()


@app.get("/helloworld")
def read_root():
    return {"Hello": "World"}

@app.get("/numerorandom")
def funcaoteste():
    return {"teste": "deucerto"}
