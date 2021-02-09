from aiozoom.components.meeting import Meeting
from aiozoom.components.dashboard import Dashboard
from aiozoom.components.recording import Recording


class Zoom(Meeting, Dashboard, Recording):
    """
    Main entrypoint for all components
    """
    pass
