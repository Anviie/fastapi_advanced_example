from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import text
import asyncio

from config import settings

engine = create_async_engine(settings.db_url)

async def finc():
    async with engine.begin() as conn:
        res = await conn.execute(text('select version()'))
        print(res.fetchone())
        
asyncio.run(finc())

