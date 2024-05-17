from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import scoped_session, declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql+asyncpg://vlone:pass@localhost:5432/tasks_db'

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
)
new_session = async_sessionmaker(engine, expire_on_commit=False)

Base = declarative_base()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
