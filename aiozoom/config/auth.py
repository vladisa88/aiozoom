# pylint:disable=(missing-function-docstring)
class ConfigurationError(Exception):
    """
    Specify own exception
    """
    pass


class Configuration:
    """
    Describe auth logic. Now available
    only JWT_TOKEN authentication
    """

    auth_token: str = ''

    def __init__(self):
        self.assert_has_api_key()

    @staticmethod
    def configure(token: str) -> None:
        Configuration.auth_token = token

    def assert_has_api_key(self):
        if not self.auth_token:
            raise ConfigurationError('Token is required!')
