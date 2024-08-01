import loguru
from pydantic import PostgresDsn
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncEngine as SQLAlchemyAsyncEngine,
    AsyncSession as SQLAlchemyAsyncSession,
    create_async_engine as create_sqlalchemy_async_engine,
)

class AsyncDatabase:
    def __init__(self):
        self.postgres_uri: PostgresDsn = PostgresDsn(
            url='postgresql://myuser:mypassword@postgres:5432/mydatabase',
        )
        self.async_engine: SQLAlchemyAsyncEngine = create_sqlalchemy_async_engine(
            url=self.set_async_db_uri,
            poolclass=NullPool,
        )
        self.async_session: SQLAlchemyAsyncSession = SQLAlchemyAsyncSession(bind=self.async_engine)
        self.pool = self.async_engine.pool
        loguru.logger.info("Database class Successfully Initialized!")

    @property
    def set_async_db_uri(self) -> str:

        uri_str = str(self.postgres_uri)
        return (
            uri_str.replace("postgresql://", "postgresql+asyncpg://")
            if uri_str else uri_str
        )


async_db: AsyncDatabase = AsyncDatabase()
