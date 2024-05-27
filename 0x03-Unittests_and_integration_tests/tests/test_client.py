#!/usr/bin/env python3
"""
Unittest for GithubOrgClient
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient, get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        :param org_name: Name of the organization to test.
        :param mock_get_json: Mock object for get_json.
        """
        # Define the mocked responses for different organization names
        responses = {
            "google": {"login": "google"},
            "abc": {"login": "abc"}
        }

        # Configure the side_effect of the mock to return
        # the appropriate response based on the organization name
        mock_get_json.side_effect = lambda url: responses[url.split('/')[-1]]

        client = GithubOrgClient(org_name)
        result = client.org
        self.assertEqual(result, responses[org_name])

        @patch('client.get_json')
        @patch('client.GithubOrgClient._public_repos_url',
               return_value='https://api.github.com/orgs/example_org/repos')
        def test_public_repos(self, mock_public_repos_url, mock_get_json):
            """
                    Test the public_repos property of GithubOrgClient.

                    :param mock_public_repos_url: Mock object for
                    _public_repos_url property.
                    :param mock_get_json: Mock object for get_json method.
                    """
            # Mock payload for get_json
            payload = [{"name": "repo1"}, {"name": "repo2"}]

            # Configure side_effect of mock_get_json to return the payload
            mock_get_json.return_value = payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("example_org")

            # Access the public_repos property
            result = client.public_repos

            # Assert that the result is what we expect from the chosen payload
            self.assertEqual(result, ["repo1", "repo2"])

            # Assert that the mocked property was called once
            mock_public_repos_url.assert_called_once()

            # Assert that get_json was called once with the correct URL
            mock_get_json.assert_called_once_with(
                'https://api.github.com/orgs/example_org/repos')


if __name__ == '__main__':
    unittest.main()
