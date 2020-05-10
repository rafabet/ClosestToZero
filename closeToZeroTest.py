import unittest
from closestToZero import *

class TestCloseToZeros(unittest.TestCase):

    def test_arrayIsUndefined(self):
        res = closestToZero()
        self.assertEqual(res, 0)

    def test_arrayIsEmpty(self):
        arr = []
        res = closestToZero(arr)
        self.assertEqual(res, 0)

    def test_functionArraySizeOne(self):
        arr = [-1]
        res = closestToZero(arr)
        self.assertEqual(res, -1)

    def test_functionArraySizeTwo(self):
        arr = [-1, 2]
        res = closestToZero(arr)
        self.assertEqual(res, -1)

    def test_functionArraySizeEqualNumReturnsPos(self):
        arr = [-1, 1]
        res = closestToZero(arr)
        self.assertEqual(res, 1)

    def test_functionArraySizeNotEqualNumReturnsPos(self):
        arr = [-1, 1]
        res = closestToZero(arr)
        self.assertNotEqual(res, -1)

    def test_functionArraySizeThreeEqualNum(self):
        arr = [-1, 1, 0]
        res = closestToZero(arr)
        self.assertEqual(res, 0)

    def test_functionArraySizeSevenRandomNum(self):
        arr = [9, -1, 3, 7, -2, 9, 10]
        res = closestToZero(arr)
        self.assertEqual(res, -1)

    def test_functionArraySizeEightRandomNum(self):
        arr = [9, -4, 3, 7, -13, 890, 10, 5]
        res = closestToZero(arr)
        self.assertEqual(res, 3)
