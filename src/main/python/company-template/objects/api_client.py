import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint, query):
        url = f"{self.base_url}{endpoint}?{query}"
        response = requests.get(url)
        return response

    def post(self, endpoint, data, query):
        url = f"{self.base_url}{endpoint}?{query}"
        response = requests.post(url, json=data)
        return response