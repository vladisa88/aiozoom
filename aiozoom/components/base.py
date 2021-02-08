import os
import sys
import asyncio

from aiozoom.config import client
from aiozoom.config.auth import Configuration


class Base(Configuration):

    async def base_get_request(self, method: str, *args, **kwargs) -> dict:
        data = await client.get(method, headers=self._headers())
        return data

    async def base_post_request(self, method: str, *args, **kwargs) -> dict:
        data = await client.post(
            method, headers=self._headers(), *args, **kwargs)
        return data

    async def base_put_request(self, method: str, *args, **kwargs) -> dict:
        data = await client.put(
            method, headers=self._headers(), *args, **kwargs)
        return data

    def _headers(self) -> dict:
        return {
            'Authorization': f'Bearer {Configuration.auth_token}'
        }


# async def func():
#     ZOOM_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.' \
#              'eyJhdWQiOm51bGwsImlzcyI6IlFJUEFQR2U1UWl1RWo3dnRxNHN' \
#              '3dmciLCJleHAiOjE3MzgyNjcyMDAsImlhdCI6MTU5ODAyMTA4OX0.' \
#              'a5QcuGot2zKW3jjv0Io40a6kSK4hSPhcQR6micdXxV0'
#     b = Base(ZOOM_TOKEN)
#     res = await b.base_get_request('meetings/123')
#     print(res)
#     await client.close()

# loop = asyncio.get_event_loop()
# loop.run_until_complete(func())
