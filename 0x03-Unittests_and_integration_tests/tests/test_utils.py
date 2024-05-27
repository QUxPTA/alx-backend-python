#!/usr/bin/env python3
"""
Unittest parameterization and mocking
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
import requests


def access_nested_map(nested_map, path):
    """
    Access a nested map with a sequence of keys.

    :param nested_map: Dictionary to access
    :param path: Tuple of keys to access the dictionary
    :return: The value corresponding to the nested keys
    :raises KeyError: If a key in the path does not exist
    :raises TypeError: If a non-dict is encountered before the end of the path
    """
    for key in path:
        if not isinstance(nested_map, dict):
            raise KeyError(key)
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """
    Makes an HTTP GET request to the given URL and returns the JSON response.

    :param url: URL to make the GET request to
    :return: JSON response from the GET request
    """
    response = requests.get(url)
    return response.json()


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with different nested maps and paths.

        :param nested_map: The nested dictionary to access.
        :param path: The tuple representing the sequence of keys
                                 to access the nested dictionary.
        :param expected: The expected result of accessing the
                                 nested dictionary with the given path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises a KeyError for invalid paths.

        :param nested_map: The nested dictionary to access.
        :param path: The tuple representing the sequence of keys
                                 to access the nested dictionary.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function to ensure it returns the expected result.

        :param test_url: URL to make the GET request to.
        :param test_payload: The expected JSON payload
                        returned by the GET request.
        :param mock_get: Mock object for requests.get.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
