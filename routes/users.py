#Python
from models.User import User
from typing import Optional, List

#FastApi
from fastapi import APIRouter
from fastapi import status


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
def signup():
    pass

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
    pass

@UserRouter.get(
    path='/users/{user_id}',
    response_model=User,
    status_code = status.HTTP_200_OK,
    summary="Show a user",
    tags=["Users"]
)
def show_a_user():
    pass

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