from sqlalchemy import insert
from src.auth.utils import hash_password
from src.database.config import async_session
from src.users.models import UserOrm

from  .schemas import UserAddSchema


async def insert_user_from_db(user: UserAddSchema):
    async with async_session() as session:
        query = insert(UserOrm).values(
            name= user.name,
            surname= user.surname,
            age= user.age,
            sex= user.sex,
            login= user.login,
            password_hash= hash_password(user.password_hash),
            role=user.role ,
            email=user.email ,
            phonenumber=user.phonenumber,
        )
        await session.execute(query)
        await session.commit()