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

        @patch('client.GithubOrgClient.org', return_value={"public_repos": 10})
        def test_public_repos_url(self, mock_org):
            """
            Test the _public_repos_url method of GithubOrgClient.

            :param mock_org: Mock object for the org property.
            """
            # Create an instance of GithubOrgClient
            client = GithubOrgClient("example_org")

            # Call the _public_repos_url method
            result = client._public_repos_url

            # Retrieve the URL from the org mock object
            url_from_mock = mock_org.return_value['repos_url']

            # Assert that the result is the expected URL
            self.assertEqual(result, url_from_mock)


if __name__ == '__main__':
    unittest.main()
