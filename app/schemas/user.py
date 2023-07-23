from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    user_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_superuser: bool = False


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    pwd: str

# Properties to receive via API on update
class UserUpdate(UserCreate):
    wish_list: Optional[str]