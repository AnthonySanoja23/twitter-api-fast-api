from fastapi import FastAPI

app = FastAPI()

@app.get(path='/')
def Home():
    return {"Twitter Api":"Ready"}