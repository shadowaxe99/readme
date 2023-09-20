
import unittest
from src.agent.browser import Browser

class TestBrowser(unittest.TestCase):

    def setUp(self):
        self.browser = Browser()

    def test_browse(self):
        url = "https://www.example.com"
        content = self.browser.browse(url)
        self.assertIsNotNone(content)

    def test_search(self):
        query = "AI research papers"
        results = self.browser.search(query)
        self.assertIsNotNone(results)

if __name__ == '__main__':
    unittest.main()
