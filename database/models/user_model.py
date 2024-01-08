from pydantic import BaseModel


from ..loader import collection
from datetime import datetime


class User(BaseModel):
    name: str
    user_name: str
    photo: str
   


users_collection = collection.user