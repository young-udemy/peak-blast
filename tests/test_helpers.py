import unittest

from exceptions import MineValueError
from helpers import make_mine, process_input


class MakeMineTestCases(unittest.TestCase):

    def test_with_proper_string(self):
        mine = make_mine('1.1, 2.2, 3.3')
        self.assertEqual(mine.x_coord, 1.1)
        self.assertEqual(mine.y_coord, 2.2)
        self.assertEqual(mine.magnitude, 3.3)

    def test_with_empty_string(self):
        with self.assertRaises(MineValueError):
            make_mine('')

    def test_with_wrong_param_count(self):
        with self.assertRaises(MineValueError):
            make_mine('1, 2')

    def test_with_invalid_values(self):
        with self.assertRaises(MineValueError):
            make_mine('1, 2, a')


class ProcessInputTestCases(unittest.TestCase):

    def test_with_empty_string(self):
        mines = process_input('')
        self.assertEqual(len(mines), 0)

    def test_with_valid_string(self):
        mines = process_input('(1, 1, 1), (2, 2, 2)')
        self.assertEqual(len(mines), 2)

    def test_with_trailing_delimiter(self):
        mines = process_input('(1, 1, 1),')
        self.assertEqual(len(mines), 1)
