from aiozoom.components.base import Base


class Recording(Base):
    """
    Class describing `Recording` logic of Zoom API
    learn more:
    https://marketplace.zoom.us/docs/api-reference/zoom-api/cloud-recording/
    """

    async def get_recording(self, meeting_id: str) -> dict:
        """
        Get meeting's recording information.
        """
        method = f'/meetings/{meeting_id}/recordings'
        return await self.base_get_request(method)

    async def list_recordings(self, email: str) -> dict:
        """
        List all cloud recordings related to user
        """
        method = f'/users/{email}/recordings'
        return await self.base_get_request(method)

    async def delete_all_recording_files(self, meeting_id: str) -> dict:
        """
        Delete all recording files of meeting
        """
        method = f'/meetings/{meeting_id}/recordings'
        return await self.base_delete_request(method)

    async def delete_recording_file(
        self, meeting_id: str, recording_id: str) -> dict:
        """
        Delete a sprecific recording file from a meeting
        """
        method = f'/meetings/{meeting_id}/recordings/{recording_id}'
        return await self.base_delete_request(method)
