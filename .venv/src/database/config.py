from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker

from src.users.models import UserOrm,VolunteerOrm,NeedyOrm
from .base import  Base



async_engine = create_async_engine(url= "postgresql+asyncpg://postgres:trava2016@localhost/volunteer_website")

async_session = async_sessionmaker(bind=async_engine)

async def init_db():
    async with async_engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


