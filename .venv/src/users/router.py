from  fastapi import APIRouter
from src.users.schemas import UserAddSchema
from src.users.service import insert_user_from_db

user_router = APIRouter(prefix="/users",tags=['пользователи'])

@user_router.post("")
async def insert_user(user: UserAddSchema):
    await insert_user_from_db(user)
    return {'msg': f"пользователь {user.name} добавлен в базу "}
