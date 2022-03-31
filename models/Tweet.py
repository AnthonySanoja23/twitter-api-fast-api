#Imports
from User import User

#Python
from uuid import UUID
from datetime import datetime
from typing import Optional

#Pydantic
from pydantic import BaseModel
from pydantic import Field


class Tweet(BaseModel):
    tweet_id: UUID
    content: str = Field(
        ...,
        min_length=1,
        max_length=256
    )
    created_at: datetime = Field(default=datetime.now)
    update_at: Optional[datetime] = Field(default=None)
    by: User = Field(...)