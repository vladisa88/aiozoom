# pylint:disable=(missing-function-docstring)
import typing as tp

from aiohttp import ClientSession


BASE_URL = 'https://api.zoom.us/v2/'

class Client:
    """
    Async client for making requests
    """

    def __init__(self, base_url: str = BASE_URL) -> None:
        self.base_url = base_url
        self.session = ClientSession()

    async def get(self, method: str, *args: tp.Any, **kwargs: tp.Any) -> tp.Any:
        async with self.session.get(f'{self.base_url}/{method}', *args, **kwargs) as response:
            data = await response.json()
            return data

    async def post(self, method: str, *args: tp.Any, **kwargs: tp.Any) -> tp.Any:
        async with self.session.post(f"{self.base_url}/{method}", *args, **kwargs) as response:
            data = await response.json()
            return data

    async def put(self, method: str, *args: tp.Any, **kwargs: tp.Any) -> tp.Any:
        async with self.session.put(f"{self.base_url}/{method}", *args, **kwargs) as response:
            data = await response.json()
            return data

    async def patch(self, method: str, *args: tp.Any, **kwargs: tp.Any) -> tp.Any:
        async with self.session.patch(f"{self.base_url}/{method}", *args, **kwargs) as response:
            data = await response.json()
            return data

    async def delete(self, method: str, *args: tp.Any, **kwargs: tp.Any) -> tp.Any:
        async with self.session.delete(f"{self.base_url}/{method}", *args, **kwargs) as response:
            data = await response.json()
            return data

    async def close(self):
        await self.session.close()


client = Client()
