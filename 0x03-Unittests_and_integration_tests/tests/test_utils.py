#!/usr/bin/env python3
"""
Unittest parameterization
"""

import unittest
from parameterized import parameterized


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


if __name__ == '__main__':
    unittest.main()
