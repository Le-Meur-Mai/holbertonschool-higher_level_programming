#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_valid_integer(self):
        '''Test result when all int are positive'''
        self.assertEqual(max_integer([1, 2, 10, 5]), 10)
        '''Test result when all int are negative'''
        self.assertEqual(max_integer([1, 6, -7, 3]), 6)
        '''Test result when there is one int'''
        self.assertEqual(max_integer([3]), 3)
        '''Test result when the max number is at different positions'''
        self.assertEqual(max_integer([10, 2, 3]), 10)
        self.assertEqual(max_integer([3, 10, 2]), 10)
        self.assertEqual(max_integer([2, 3, 10]), 10)

    def text_max_error(self):
        '''Test result when a list is empty'''
        self.assertEqual(max_integer([]), None)
