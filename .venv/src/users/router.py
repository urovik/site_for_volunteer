from  fastapi import APIRouter
from src.users.schemas import UserAddSchema,VolunteerAddSchema
from src.users.service import UserService

user_router = APIRouter(prefix="/api/users",tags=['пользователи'])

@user_router.post("")
async def insert_user(user: UserAddSchema):
    await UserService.insert_user_from_db(user)
    return {'msg': f"пользователь {user.name} добавлен в базу "}

@user_router.post("/volunteers")
async def register_volunteer(volunteer: VolunteerAddSchema):
    await UserService.insert_volunteer_from_db(volunteer)
    return {"msg": f"волонтер с именем {volunteer.name} добавлен"}