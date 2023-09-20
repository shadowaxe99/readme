
import unittest
from src.agent.github_integration import GithubIntegration

class TestGithubIntegration(unittest.TestCase):

    def setUp(self):
        self.github = GithubIntegration()

    def test_search_repository(self):
        repo_name = "tensorflow/tensorflow"
        result = self.github.search_repository(repo_name)
        self.assertEqual(result, repo_name)

    def test_integrate_repository(self):
        repo_name = "tensorflow/tensorflow"
        result = self.github.integrate_repository(repo_name)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
