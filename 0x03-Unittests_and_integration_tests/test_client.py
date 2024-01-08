#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for the GithubOrgClient class"""

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test org method"""
        org_name = 'testorg'
        test_payload = {"test": "data"}
        mock_get_json.return_value = test_payload

        org_client = GithubOrgClient(org_name)
        result = org_client.org()

        mock_get_json.assert_called_once_with(org_client.ORG_URL.format(org=org_name))
        self.assertEqual(result, test_payload)

    def test_public_repos(self):
        """Test public_repos method"""
        org_client = GithubOrgClient('testorg')
        org_client.repos_payload = [
            {"name": "repo1", "license": {"key": "my_license"}},
            {"name": "repo2", "license": {"key": "other_license"}},
        ]

        result = org_client.public_repos(license="my_license")
        self.assertEqual(result, ["repo1"])

        result = org_client.public_repos(license="other_license")
        self.assertEqual(result, ["repo2"])

        result = org_client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])

    def test_has_license(self):
        """Test has_license method"""
        org_client = GithubOrgClient('testorg')
        repo = {"license": {"key": "my_license"}}
        self.assertTrue(org_client.has_license(repo, "my_license"))
        self.assertFalse(org_client.has_license(repo, "other_license"))

        repo = {}
        self.assertFalse(org_client.has_license(repo, "my_license"))


if __name__ == "__main__":
    unittest.main()
