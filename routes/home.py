from fastapi import APIRouter

home = APIRouter()

@home.get(path='/')
def Home():
    return {"Twitter Api":"Ready"}