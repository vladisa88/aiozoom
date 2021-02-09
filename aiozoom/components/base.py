import os
import sys
import asyncio

from aiozoom.config import client
from aiozoom.config.auth import Configuration


class Base(Configuration):
    """
    Base class for processing requests
    """
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
