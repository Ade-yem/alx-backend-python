#!/usr/bin/env python3
"""Parameterize a unit test"""

import unittest
from unittest.mock import patch
import utils
from parameterized import parameterized
from typing import Dict, Tuple, List, Union, Callable


class TestAccessNestedMap(unittest.TestCase):
    """ test that the method returns what it is supposed to"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple,
                               expected: Union[Dict, int]) -> None:
        """test the function"""
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict,
                                         path: Tuple,
                                         expected: Exception) -> None:
        """test Exception"""
        with self.assertRaises(expected):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test the get json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str,
                      test_payload: Dict,
                      mock_get: Callable) -> None:
        """tests get_json method"""
        res = type('MockResponse', (object,), {'json': lambda: test_payload})
        mock_get.return_value = res
        result = utils.get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """test memoize"""

    def test_memoize(self) -> None:
        """test memoize"""
        class TestClass:
            def a_method(self):
                return 42

            @utils.memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mock_meth:
            test = TestClass()
            test.a_property
            test.a_property
            mock_meth.assert_called_once()

            self.assertEqual(test.a_property, mock_meth.return_value)
