from pydantic import BaseModel, EmailStr

from .models import Roles,Gender


class UserAddSchema(BaseModel):
    name: str
    surname: str
    age: int
    sex: Gender
    login: str
    password_hash: str
    role: Roles
    email: EmailStr
    phonenumber: str


class UserPayloadSchema(BaseModel):
    id: int
    login: str
    role: Roles