from sqlalchemy import MetaData
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from sqlalchemy.sql.expression import func, join
import logging
import asyncio


from db.models import Base, Comment, User

log = logging.getLogger(__name__)


class PostgresClient:
    async_session: sessionmaker

    def __init__(self, database_url: str = "postgresql+asyncpg://postgres:hac_db@localhost:5433/hac_db"):
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

    async def select_by_filter(self, table: Base, filters, count_only=False):
        async with self.async_session() as session:
            try:
                if count_only:
                    stmt = select(func.count()).select_from(table)
                else:
                    stmt = select(table)
                for attr, value in filters.items():
                    stmt = stmt.filter(getattr(table, attr) == value)
                result = await session.execute(stmt)
                if count_only:
                    return result.scalar()
                else:
                    return result.scalars().all()

            except SQLAlchemyError as e:
                log.error(f"Failed to select by filter: {e}")
                return None

    async def select_with_join(self, first_table: Base, first_field, second_table: Base, second_field: str, filters: dict):
        async with self.async_session() as session:
            try:
                join_condition = getattr(first_table, first_field) == getattr(second_table, second_field)

                stmt = select(first_table)
                stmt = select(first_table, second_table).select_from(join(first_table, second_table, join_condition))

                for attr, value in filters.items():
                    stmt = stmt.filter(getattr(first_table, attr) == value)

                result = await session.execute(stmt)
                return result.all()
            except SQLAlchemyError as e:
                log.error(f"Failed to execute join query: {e}")
                return None

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
#     from db.models import Vote
#     filters = {"trip_item_id": 1}
#     join_field = "user_id"
#     c = await db_client.select_with_join(Comment, "user_id", User, "id", filters)
#     print(c)
#
# if __name__ == "__main__":
#     asyncio.run(main())