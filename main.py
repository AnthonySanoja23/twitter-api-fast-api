#Python
from routes.users import UserRouter
from routes.tweet import TweetRouter

#FastApi
from fastapi import FastAPI


app = FastAPI()

app.include_router(UserRouter)
app.include_router(TweetRouter)


