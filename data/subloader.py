import os

import aiofiles
from ujson import loads

DATA = 'data'

async def get_json(filename: str) -> list:
    path = os.path.join(DATA, filename)
    if os.path.exists(path):
        async with aiofiles.open(path, "r", encoding="utf-8") as f:
            return loads(await f.read())
    return []
