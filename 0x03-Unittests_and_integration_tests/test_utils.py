import unittest
from unittest.mock import patch, Mock
from utils import get_json, memoize


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function"""

    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """Test get_json with mocked requests.get"""
        test_payload1 = {"payload": True}
        test_payload2 = {"payload": False}

        # Mocking requests.get and its return value
        mock_response1 = Mock()
        mock_response1.json.return_value = test_payload1

        mock_response2 = Mock()
        mock_response2.json.return_value = test_payload2

        mock_get.side_effect = [mock_response1, mock_response2]

        result1 = get_json("http://example.com")
        result2 = get_json("http://holberton.io")

        # Asserting requests.get called with the respective URL
        mock_get.assert_any_call("http://example.com")
        mock_get.assert_any_call("http://holberton.io")

        # Asserting the outputs of get_json
        self.assertEqual(result1, test_payload1)
        self.assertEqual(result2, test_payload2)


class TestMemoize(unittest.TestCase):
    """Test case for the memoize decorator"""

    def test_memoize(self):
        """Test memoize decorator"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            mock_a_method.return_value = 42

            obj = TestClass()
            result1 = obj.a_property
            result2 = obj.a_property

            mock_a_method.assert_called_once()
            self.assertEqual(result1, result2)


if __name__ == "__main__":
    unittest.main()
