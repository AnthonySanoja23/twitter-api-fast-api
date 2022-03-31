#Python
from models.Tweet import Tweet
from typing import List

#FastApi
from fastapi import APIRouter
from fastapi import status


TweetRouter = APIRouter()

# Path Operations

@TweetRouter.get(
    path='/',
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="Show all Tweets",
    tags=["Tweets"]
)
def home():
    return {"all":"tweets"}

@TweetRouter.post(
    path='/post',
    response_model=Tweet,
    status_code = status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweets"]
)
def post():
    pass

@TweetRouter.get(
    path='/tweets/{tweet_id}',
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="show a Tweet",
    tags=["Tweets"]
)
def show_a_tweet():
    pass

@TweetRouter.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"]
)
def delete_a_tweet():
    pass

@TweetRouter.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweets"]
)
def update_a_tweet():
    pass