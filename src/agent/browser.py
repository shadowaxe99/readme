
import requests
from bs4 import BeautifulSoup

class Browser:
    def __init__(self):
        self.session = requests.Session()

    def get_page_content(self, url):
        response = self.session.get(url)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser')

    def search(self, url, query):
        search_url = f"{url}/search?q={query}"
        return self.get_page_content(search_url)
