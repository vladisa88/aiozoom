from aiozoom.components.base import Base


class Dashboard(Base):

    async def get_meeting_participants(self, meeting_id: str) -> dict:
        """
        Get list of participants with detail information
        """
        method = f'metrics/meetings/{meeting_id}/participants'
        return self.base_get_request(method)
