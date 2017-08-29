import unittest

from models import Bang, Mine, MineField


class MineTestCases(unittest.TestCase):

    def test_is_in_blast_radius(self):
        mine1 = Mine(0, 0, 0)
        mine2 = Mine(1, 0, 1)
        mine3 = Mine(1, 1, 1)

        self.assertFalse(mine1.is_in_blast_radius(mine2))
        self.assertTrue(mine2.is_in_blast_radius(mine1))
        self.assertTrue(mine2.is_in_blast_radius(mine3))
        self.assertFalse(mine3.is_in_blast_radius(mine1))


class MineFieldTestCases(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def test_get_bang_progression(self):
        mine1 = Mine(0, 0, 1)
        mine2 = Mine(1, 0, 0)
        mine_field = MineField({mine1, mine2})
        bangs = mine_field.get_bang_progression(mine1)
        self.assertEqual(len(bangs), 2)
        self.assertTrue(all([isinstance(b, Bang) for b in bangs]))
        self.assertEqual(bangs[0].starter, mine1)
        self.assertEqual(bangs[0].t, 0)
        self.assertEqual(bangs[1].starter, mine1)
        self.assertEqual(bangs[1].t, 1)
