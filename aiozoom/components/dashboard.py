from aiozoom.components.base import Base


class Dashboard(Base):
    """
    Class describing `Dashboard` logic of Zoom API
    learn more:
    https://marketplace.zoom.us/docs/api-reference/zoom-api/dashboards/
    """
    async def get_meeting_participants(self, meeting_id: str) -> dict:
        """
        Get list of participants with detail information

        Params:
            meeting_id - unique id of meeting
        """
        method = f'metrics/meetings/{meeting_id}/participants?type=past&page_size=100'
        return await self.base_get_request(method)

    async def get_meeting_info(self, meeting_id: str) -> dict:
        """
        Get information about past meeting

        Params:
            meeting_id - unique id of meeting
        """
        method = f'metrics/meetings/{meeting_id}?type=past'
        return await self.base_get_request(method)
