from sqlalchemy import insert,select
from src.auth.utils import hash_password
from src.database.config import async_session
from src.users.models import UserOrm

from  .schemas import UserAddSchema

class UserService():

    @classmethod
    async def insert_user_from_db(cls,user: UserAddSchema):
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
    
    @classmethod
    async def get_user_payload_by_login_from_db(cls,login: str):
        async with async_session() as session:
            query = select(UserOrm.login,UserOrm.password_hash,UserOrm.id,UserOrm.role).where(UserOrm.login == login)
            res = await session.execute(query)
            return res.first()
        
    @classmethod
    async def get_user_by_id_from_db(cls,id: int):
        async with async_session() as session:
            query = select(UserOrm).where(UserOrm.id == id)
            res = await session.execute(query)
            return res.scalar()
