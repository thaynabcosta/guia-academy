from fastapi import FastAPI

app = FastAPI()

@app.get("/nome")
def ver_nome():
    return {"nome": "thayná beatriz"}

@app.get("/soma")
def soma(a: int, b: int):
    return {"soma": a + b}

