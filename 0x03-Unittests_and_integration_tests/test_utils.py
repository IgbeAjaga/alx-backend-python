#!/usr/bin/env python3
"""Unit tests for utils.py"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various inputs"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map exception handling"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestUtilsGetJson(unittest.TestCase):
    """Test case for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json with different URLs and payloads"""
        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestUtilsMemoize(unittest.TestCase):
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
            obj.a_property
            obj.a_property

            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
