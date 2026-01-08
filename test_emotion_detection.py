"""Unit tests for the EmotionDetection package."""
from EmotionDetection.emotion_detection import app
import unittest

class TestEmotionDetection(unittest.TestCase):
    """Tests for emotion detection output."""

    def setUp(self):
        """Create a Flask test client before each test."""
        self.client = app.test_client()

    def test_dominant_emotions(self):
        """Verify the dominant emotion value for the following test case statements."""
        test_case_statements = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for statement, expected in test_case_statements:
            response = self.client.get("/ask", query_string={"text": statement})
            data = response.get_json()

            self.assertIsNotNone(data)
            self.assertIn("dominant_emotion", data)
            self.assertEqual(data["dominant_emotion"], expected)


if __name__ == "__main__":
    unittest.main()
