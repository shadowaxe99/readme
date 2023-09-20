
import unittest
from src.agent.ai_agent import AIAgent

class TestAIAgent(unittest.TestCase):

    def setUp(self):
        self.ai_agent = AIAgent()

    def test_initialization(self):
        self.assertIsInstance(self.ai_agent, AIAgent, "Object should be an instance of AIAgent class.")

    def test_browse(self):
        result = self.ai_agent.browse("https://www.google.com")
        self.assertIsNotNone(result, "Browse method should return a result.")

    def test_search_github(self):
        result = self.ai_agent.search_github("TensorFlow")
        self.assertIsNotNone(result, "Search GitHub method should return a result.")

    def test_integrate_repository(self):
        result = self.ai_agent.integrate_repository("https://github.com/tensorflow/tensorflow")
        self.assertTrue(result, "Integrate repository method should return True if successful.")

if __name__ == '__main__':
    unittest.main()

