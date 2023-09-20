
import unittest
from src.utils import file_analyzer

class TestFileAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = file_analyzer.FileAnalyzer()

    def test_analyze_file(self):
        result = self.analyzer.analyze_file('AI_Readme_Writer/src/utils/file_analyzer.py')
        self.assertIsInstance(result, dict)

    def test_get_file_content(self):
        content = self.analyzer.get_file_content('AI_Readme_Writer/src/utils/file_analyzer.py')
        self.assertIsInstance(content, str)

if __name__ == '__main__':
    unittest.main()
