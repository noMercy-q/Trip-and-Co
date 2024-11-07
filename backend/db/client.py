from sqlalchemy import MetaData
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
import logging
import asyncio


from db.models import Base


log = logging.getLogger(__name__)


class PostgresClient:
    async_session: sessionmaker

    def __init__(self, database_url: str = "postgresql+asyncpg://postgres:hac_db@localhost:5432/hac_db"):
        self.engine = create_async_engine(database_url, echo=True)
        self.metadata = MetaData()
        self.async_session = sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def connect(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def select_all(self, table: Base):
        async with self.async_session() as session:
            async with session.begin():
                try:
                    result = await session.execute(select(table))
                    return result.scalars().all()
                except Exception as e:
                    log.error(f"Failed to execute query: {e}")
                    return []


    async def create_record(self, table_record: Base):
        async with self.async_session() as session:
            async with session.begin():
                session.add(table_record)
                try:
                    await session.commit()
                    return table_record
                except SQLAlchemyError as e:
                    await session.rollback()
                    log.error(f"Failed to create record for {table_record.__tablename__}: {e}")
                    raise


# for tests, TODO: delete
# async def main():
#     db_client = PostgresClient()
#     await db_client.connect()
#
#     cities = await db_client.select_all()
#     for city in cities:
#         print(city.city_id, city.city_name)
#
# if __name__ == "__main__":
#     asyncio.run(main())