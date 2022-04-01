#Python
import json
from unittest import result
from uuid import UUID
from models.User import User, UserRegister
from typing import Optional, List

#FastApi
from fastapi import APIRouter, Body
from fastapi import status
from fastapi import HTTPException


UserRouter = APIRouter()

# Path Operations 

## Users
@UserRouter.post(
    path='/signup',
    response_model=User,
    status_code = status.HTTP_201_CREATED,
    summary="Register a User",
    tags=["Users"]
)
def signup(user: UserRegister = Body(...)):
    """
    Signup 

    This path operation register a user in the app

    Parameteres:
        -Request body parameter
            -user: UserRegister
    
    Returns a json with the basic user information:
        - user_id : UUID
        - email : Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime
    """
    with open("users.json","r+", encoding="utf-8") as f :
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["user_id"] = str(user_dict["user_id"])
        user_dict["birth_date"] = str(user_dict["birth_date"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


@UserRouter.post(
    path='/login',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="Login a User",
    tags=["Users"]
)
def login():
    pass

@UserRouter.get(
    path='/users',
    response_model=List[User],
    status_code = status.HTTP_200_OK,
    summary="Show all users",
    tags=["Users"]
)
def show_all_users():
    """
    This path operation shows all users in the app 

    Parameters: 
        -
    
    Returns a json list with all users in the app, with the followin keys :
        - user_id : UUID
        - email : Emailstr
        - first_name: str
        - last_name: str
        - birth_date: datetime  
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

@UserRouter.get(
    path='/users/{user_id}',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user(user_id:UUID):
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        seach_user = filter(lambda user: user['user_id'] == str(user_id), results)
        list_seach_user = list(seach_user)
        if not list_seach_user:
            raise HTTPException(status_code=404, detail="User not found")
        tweet_found = list_seach_user[0]
        return tweet_found

@UserRouter.delete(
    path='/users/{user_id}/delete',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="Delte a User",
    tags=["Users"]
)
def delete_user():
    pass

@UserRouter.put(
    path='/users/{user_id}/update',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="Update a User",
    tags=["Users"]
)
def update_user():
    pass