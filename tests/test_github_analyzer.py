
import unittest
from src.utils.github_analyzer import GithubAnalyzer

class TestGithubAnalyzer(unittest.TestCase):

    def setUp(self):
        self.github_analyzer = GithubAnalyzer()

    def test_analyze_repo(self):
        repo_url = "https://github.com/user/repo"
        result = self.github_analyzer.analyze_repo(repo_url)
        self.assertIsInstance(result, dict)

    def test_get_readme_content(self):
        repo_url = "https://github.com/user/repo"
        result = self.github_analyzer.get_readme_content(repo_url)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()

