import os

import asyncpg
from async_db_polars.pgdb import PGDB

db = PGDB()

DATABASE_URL = os.environ["DATABASE_URL"]


async def init_pg_pool():
    pool = await asyncpg.create_pool(DATABASE_URL)
    if pool is None:
        return
    db.init(pool)
