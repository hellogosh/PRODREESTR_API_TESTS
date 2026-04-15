import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ApiClient:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL')
        self.token = os.getenv('TOKEN')
        self.session = requests.Session()

        self.session.headers.update({
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        })

    def get(self, path, params=None):
        return self.session.get(f'{self.base_url}{path}', params=params)

    def post(self, path, json=None, params=None):
        return self.session.post(f'{self.base_url}{path}', json=json, params=params)

    def put(self, path, json=None, params=None):
        return self.session.put(f'{self.base_url}{path}', json=json, params=params)

    def delete(self, path, params=None):
        return self.session.delete(f'{self.base_url}{path}', params=params)