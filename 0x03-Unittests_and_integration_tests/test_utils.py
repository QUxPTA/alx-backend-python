#!/usr/bin/env python3
"""
Unittest parametization
"""

import unittest
from parameterized import parameterized


def access_nested_map(nested_map, path):
    """
    Access a nested map with a sequence of keys.

    :param nested_map: Dictionary to access
    :param path: Tuple of keys to access the dictionary
    :return: The value corresponding to the nested keys
    """
    for key in path:
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


if __name__ == '__main__':
    unittest.main()
