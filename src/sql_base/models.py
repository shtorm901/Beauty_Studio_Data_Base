from pydantic import Optional
from pydantic import BaseModel
from datetime import datetime

class Workers(BaseModel):
    post_id: Optional[int]
    name: str
    surname: str
    telephone_number: str

class Post(BaseModel):
    post: str

class Services(BaseModel):
    name: str
    price: str
    description: str

class Client(BaseModel):
    name: str
    address: str
    telephone_number: str

class Visits(BaseModel):
    visit_id: Optional[int]
    client_id: Optional[int]
    service_id: Optional[int]
    worker_id: Optional[int]
    datetime: datetime

class user(BaseModel):
    name: str
    password: str
    telephone_number: str
