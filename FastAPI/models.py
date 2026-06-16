#this is pydantic implementation for type checking and validation of data.
from pydantic import BaseModel

class Product(BaseModel):

    id: int 
    name: str
    description: str 
    price : float 
    quantity : int 