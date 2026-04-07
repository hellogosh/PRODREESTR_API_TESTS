import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ApiClient:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL')
        self.token = os.getenv('TOKEN')
        self.session = requests.Session()

        self.session.cookies.set("session-cookie",
                                 "18a416a1427b92ec247a030a80267f931cedce47463e836fa0066c1ca41d07329d4c5f09a3e10e5be236cb5f2eebba56")
        self.session.cookies.set("SESSION", "faec3440-125a-4b62-abb2-a481fab37652")

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