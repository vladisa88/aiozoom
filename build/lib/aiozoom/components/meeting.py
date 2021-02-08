import asyncio
import sys

from aiozoom.components.base import Base
from aiozoom.config import client


class Meeting(Base):

    async def create_meeting(self, email: str, body: dict) -> dict:
        """
        Create meeting for the given account email
        See docs for `body` sample
        """
        method = f'users/{email}/meetings'
        return await self.base_post_request(method, json=body)

    async def get_meeting(self, meeting_id: str) -> dict:
        method = f'meetings/{meeting_id}'
        return await self.base_get_request(method)

    async def stop_meeting(self, meeting_id: str) -> None:
        method = f'meetings/{meeting_id}'
        body = {'action': 'end'}
        res = await self.base_put_request(method, json=body)
        print(res)

    async def list_meetings(self, email: str) -> dict:
        method = f'users/{email}/meetings'
        return await self.base_get_request(method)
