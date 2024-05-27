#!/usr/bin/env python3
"""
Unittest for GithubOrgClient
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient, get_json
import requests

# Import fixtures
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

        # Assert that the result is the expected URL
        self.assertEqual(
            result, "https://api.github.com/orgs/example_org/repos")

    @patch('client.get_json', return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    @patch('client.GithubOrgClient._public_repos_url',
           return_value="https://api.github.com/orgs/example_org/repos")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test the public_repos method of GithubOrgClient.

        :param mock_public_repos_url: Mock object for
        _public_repos_url property.
        :param mock_get_json: Mock object for get_json function.
        """
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("example_org")

        # Call the public_repos method
        result = client.public_repos()

        # Assert that the result is the expected list of repositories
        expected_result = ["repo1", "repo2"]
        self.assertEqual(result, expected_result)

        # Assert that the _public_repos_url property was called once
        mock_public_repos_url.assert_called_once()

        # Assert that the get_json function was called once
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test the has_license method of GithubOrgClient.

        :param repo: Dictionary representing the repository data.
        :param license_key: Key of the license to check.
        :param expected_result: Expected result of has_license method.
        """
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("example_org")

        # Mock the get_json method to return the repository data
        with patch('client.get_json', return_value=repo):
            # Call the has_license method
            result = client.has_license(license_key)

        # Assert that the result matches the expected result
        self.assertEqual(result, expected_result)

    def test_public_repos(self):
        """
        Test the public_repos method of GithubOrgClient
        without specifying a license.
        """
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("example_org")

        # Mock the get_json method to return the repository data
        with patch('client.get_json',
                   side_effect=[org_payload, repos_payload]):
            # Call the public_repos method
            result = client.public_repos()

        # Assert that the result matches the expected list of repositories
        self.assertEqual(result, expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the public_repos method of GithubOrgClient
        with a specified license.
        """
        # Create an instance of GithubOrgClient
        client = GithubOrgClient("example_org")

        # Mock the get_json method to return the repository data
        with patch('client.get_json',
                   side_effect=[org_payload, repos_payload]):
            # Call the public_repos method with a specified license
            result = client.public_repos(license="apache-2.0")

        # Assert that the result matches the expected
        # list of repositories with Apache 2.0 license
        self.assertEqual(result, apache2_repos)


@parameterized_class([
    {"org_payload": org_payload,
     "repos_payload": repos_payload,
     "expected_repos": expected_repos,
     "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock requests.get.
        """
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.return_value = Mock()
        cls.mock_get.return_value.json.side_effect = [
            cls.org_payload,
            cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop patcher.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the public_repos method with integration.
        """
        client = GithubOrgClient("example_org")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the public_repos method with a specified license with integration.
        """
        client = GithubOrgClient("example_org")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
