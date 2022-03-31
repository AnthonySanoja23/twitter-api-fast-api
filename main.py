from fastapi import FastAPI
from routes.home import home

app = FastAPI()
app.include_router(home)



