
import unittest
from src.models import ai_model

class TestAIModel(unittest.TestCase):

    def setUp(self):
        self.model = ai_model.AiModel()

    def test_model_creation(self):
        self.assertIsNotNone(self.model.model)

    def test_model_training(self):
        training_data = "AI_Readme_Writer/data/training_data/readme_samples.txt"
        self.model.train(training_data)
        self.assertTrue(self.model.is_trained)

    def test_model_prediction(self):
        test_input = "This is a test input"
        prediction = self.model.predict(test_input)
        self.assertIsNotNone(prediction)

if __name__ == '__main__':
    unittest.main()

