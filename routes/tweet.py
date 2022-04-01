#Python
import json
from models.Tweet import Tweet
from typing import List
from uuid import UUID

#FastApi
from fastapi import APIRouter
from fastapi import status
from fastapi import Body
from fastapi import HTTPException


TweetRouter = APIRouter()

def seach_tweet(tweet_id):
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        seach_tweet = list(filter(lambda tweet: tweet['tweet_id'] == str(tweet_id), results))
        return seach_tweet

def save_in_json(tweets):
	data = json.dumps(tweets)
	f = open('tweets.json','w')
	f.write(data)
	f.close()  

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
def show_a_tweet(tweet_id:UUID):
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        seach_tweet = filter(lambda tweet: tweet['tweet_id'] == str(tweet_id), results)
        list_seach_tweet = list(seach_tweet)
        if not list_seach_tweet:
            raise HTTPException(status_code=404, detail="Tweet not found")
        tweet_found = list_seach_tweet[0]
        return tweet_found
    
@TweetRouter.delete(
    path='/tweets/{tweet_id}/delete',
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="Delete a Tweet",
    tags=["Tweets"]
)
def delete_a_tweet(tweet_id:UUID):
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        results = list(filter(lambda tweet: tweet['tweet_id'] != str(tweet_id), results))
        list_seach_tweet = seach_tweet(tweet_id)
        if not list_seach_tweet:
            raise HTTPException(status_code=404, detail="Tweet not found")
        seach_tweet_found = list_seach_tweet[0]
        save_in_json(results)
        return seach_tweet_found

@TweetRouter.put(
    path='/tweets/{tweet_id}/update',
    response_model=Tweet,
    status_code = status.HTTP_200_OK,
    summary="Update a Tweet",
    tags=["Tweets"]
)
def update_a_tweet(tweet_id:UUID,tweet: Tweet = Body(...)):
    with open("tweets.json", "r+", encoding="utf-8") as f:
        tweet_dict = tweet.dict()
        tweet_dict["tweet_id"] = str(tweet_dict["tweet_id"])
        tweet_dict["created_at"] = str(tweet_dict["created_at"])
        tweet_dict["update_at"] = str(tweet_dict["update_at"])
        tweet_dict['by']['user_id'] = str(tweet_dict['by']['user_id'])
        tweet_dict['by']['birth_date'] = str(tweet_dict['by']['birth_date'])

        results = json.loads(f.read())
        results = list(filter(lambda tweet_dict: tweet_dict['tweet_id'] != str(tweet_id), results))
        results.append(tweet_dict)

        list_seach_tweet = seach_tweet(tweet_id)

        if not list_seach_tweet:
            raise HTTPException(status_code=404, detail="Tweet not found")

        seach_tweet_found = list_seach_tweet[0]
        save_in_json(results)
        return seach_tweet_found