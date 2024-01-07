from pydantic import BaseModel

from ..loader import collection
from datetime import datetime
from .user_model import User

class Art(BaseModel):
    _id: int
    image: str
    tag: str
    creator: str
   


arts_collection = collection.art