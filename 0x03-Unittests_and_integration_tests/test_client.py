#!/usr/bin/env python3
"""Parameterize and patch as decorators"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)
from typing import Dict, List, Tuple


class TestGithubOrgClient(unittest.TestCase):
    """test the GithubOrgClient class"""

    @parameterized.expand([
        ("google", {'org_name': "google"}),
        ("abc", {'org_name': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org_name: str, res: Dict,
                 mock_get: MagicMock) -> None:
        """Tests the `org` method."""
        mock_get.return_value = MagicMock(return_value=res)
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), res)
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self) -> None:
        """test public repo url"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repo:
            mock_repo.return_value = "https://api.github.com/users/google/repo"
            self.assertEqual(GithubOrgClient("google")._public_repos_url,
                             "https://api.github.com/users/google/repo")

    @parameterized.expand([
        ({'license': {'key': "my_license"}}, "my_license", True),
        ({'license': {'key': "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tests the `has_license` method."""
        client = GithubOrgClient("google")
        has_license = client.has_license(repo, key)
        self.assertEqual(has_license, expected)

    def test_public_repos(self):
        """test GithubOrgClient.public_repos"""
        

