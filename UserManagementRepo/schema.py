
from pydantic import BaseModel,EmailStr


class User(BaseModel):
    organization_name: str
    tenant_name : str
    company_logo : str

    username:str
    firstname:str
    lastname:str
    email:str

class userRole(BaseModel):

    name:str