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
        method = f'metrics/meetings/{meeting_id}/participants'
        return self.base_get_request(method)
