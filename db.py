from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine

from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

aengine = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,
    echo=False,
)

