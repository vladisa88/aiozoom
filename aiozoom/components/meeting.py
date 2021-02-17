import typing as tp

from aiozoom.components.base import Base, ZoomException


class Meeting(Base):
    """
    Class describing `Meeting` logic of Zoom API
    learn more:
    https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/
    """

    async def create_meeting(self, email: str, body: dict) -> dict:
        """
        Create meeting for the given account email

        Params:
            email - address of account
            body - dict with parameters
        See docs for `body` sample
        https://marketplace.zoom.us/docs/api-reference/zoom-api/meetings/meetingcreate
        """
        if not self.check_body(body):
            raise ZoomException('Body has to be a valid python dictionary')

        method = f'users/{email}/meetings'
        return await self.base_post_request(method, json=body)

    async def get_meeting(self, meeting_id: str) -> dict:
        """
        Get meeting information for given `meeting_id`

        Params:
            meeting_id - unique id of meeting
        """
        method = f'meetings/{meeting_id}'
        return await self.base_get_request(method)

    async def stop_meeting(self, meeting_id: str) -> None:
        """
        Force stop the meeting.

        Params:
            meeting_id - unique id of meeting
        """
        method = f'meetings/{meeting_id}/status'
        body = {'action': 'end'}
        return await self.base_put_request(method, json=body)

    async def list_meetings(self, email: str) -> dict:
        """
        List all meetings for account

        Params:
            email - address of account
        """
        method = f'users/{email}/meetings'
        return await self.base_get_request(method)

    async def update_meeting(self, meeting_id: str, body: dict) -> dict:
        """
        Update the details of a meeting

        Params:
            meeting_id - unique id of meeting
            body - dict with parameters (see docs for more)
        """
        if not self.check_body(body):
            raise ZoomException('Body has to be a valid python dictionary')

        method = f'meetings/{meeting_id}'
        return await self.base_patch_request(method, json=body)

    @staticmethod
    def check_body(body: tp.Any) -> bool:
        """
        Check if body is valid for request
        """
        return isinstance(body, dict)
