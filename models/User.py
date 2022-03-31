#Python
from datetime import date
from typing import Optional

#Pydantinc
from pydantic import BaseModel
from pydantic import EmailStr 
from pydantic import Field



#Models
class UserBase(BaseModel):
    user_id : UUID = Field(...)
    email : EmailStr = Field(...)

class UserLogin(UserBase):
    password : str = Field(
        ...,
        min_length=8
    )

class User(UserBase):
    user_id : UUID = Field(...)
    email : EmailStr = Field(...) 
    first_name : str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name : str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    birth_date : Optional[date] = Field(...)
