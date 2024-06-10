import requests, config
from datetime import datetime

auth_url = config.bot_config['auth']['url']

class User():
    username: str = "BobbyTables"
    user_id: str = "01234567-89ab-cdef-0123-456789abcdef"
    patron_tier: str = None
    created_time: datetime = "2050-01-01T00:00:00.000000+00:00"

    def __init__(self, username = None, user_id = None, patron_tier = None, created_time = None) -> None:
        self.username = username
        self.user_id = user_id
        self.patron_tier = patron_tier
        self.created_time = created_time
    
    @classmethod
    def from_username(self, username: str = "BobbyTables"):
        inst = self()
        x = requests.get(f"{auth_url}/api/query/name?name={username}")
        data = x.json()

        inst.username = data['userName']
        inst.user_id = data['userId']
        inst.patron_tier = data['patronTier']
        inst.created_time = datetime.fromisoformat(data['createdTime'])

        return inst