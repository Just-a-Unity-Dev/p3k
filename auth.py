import requests
import config
from datetime import datetime

auth_url = config.bot_config['auth']['url']


class NotRealUserException(Exception):
    pass


class User():
    username: str = "BobbyTables"
    user_id: str = "01234567-89ab-cdef-0123-456789abcdef"
    patron_tier: str = None
    created_time: datetime = "2050-01-01T00:00:00.000000+00:00"

    def __init__(
        self,
        username,
        user_id,
        patron_tier,
        created_time
    ) -> None:
        self.username = username
        self.user_id = user_id
        self.patron_tier = patron_tier
        self.created_time = created_time

    @classmethod
    def from_username(self, username: str = "BobbyTables"):
        x = requests.get(f"{auth_url}/api/query/name?name={username}")
        data: dict = x.json()
        if ("status" in data):
            raise NotRealUserException("Did not supply a real username.")

        return User(
            data['userName'],
            data['userId'],
            data['patronTier'], 
            datetime.fromisoformat(data['createdTime']
            ))
