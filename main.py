from fastapi import FastAPI
from routes.home import home
from routes.users import UserRouter
from routes.tweet import TweetRouter

app = FastAPI()
app.include_router(home)
app.include_router(UserRouter)
app.include_router(TweetRouter)


