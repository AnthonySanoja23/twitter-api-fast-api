#Python
import json
from models.Tweet import Tweet
from typing import List

#FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Body


TweetRouter = APIRouter()

# Path Operations

@TweetRouter.get(
    path='/',
    response_model=List[Tweet],
    status_code = status.HTTP_200_OK,
    summary="Show all Tweets",
    tags=["Tweets"]
)
def home():
    """
    This path operation shows all tweet in the app 

    Parameters: 
        -
    
    Returns a json list with all tweet in the app, with the followin keys :
        - tweet_id : UUID
        - content: str 
        - created_at: datetime 
        - update_at: Optional[datetime] 
        - by: User
    """
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

@TweetRouter.post(
    path='/post',
    response_model=Tweet,
    status_code = status.HTTP_201_CREATED,
    summary="Post a Tweet",
    tags=["Tweets"]
)
def post(tweet: Tweet = Body(...)):
    """
    Post Tweet 

    This path operation register a tweet in the app

    Parameteres:
        -Request body parameter
            -tweet: Tweet
    
    Returns a json with the basic tweet information:
        tweet_id: UUID
        content: str 
        created_at: datetime 
        update_at: Optional[datetime] 
        by: User
    """
    with open("tweets.json","r+", encoding="utf-8") as f :
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["update_at"] = str(tweet_dict["update_at"])
        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

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