import unittest

from mines import find_big_bangs
from models import Mine


class FindBigBangsTestCases(unittest.TestCase):

    def test_with_no_mines(self):
        self.assertEqual(find_big_bangs(set()), [])

    def test_with_1_mine(self):
        mine = Mine(1, 1, 1)
        bangs = find_big_bangs({mine})
        self.assertEqual(len(bangs), 1)
        self.assertEqual(bangs[0].starter, mine)

    def test_no_chain_reaction(self):
        mine1 = Mine(5, 5, 1)
        mine2 = Mine(0, 0, 1)
        bangs = find_big_bangs({mine1, mine2})
        self.assertEqual(len(bangs), 2)
        self.assertEqual(bangs[0].t, 0)
        self.assertEqual(bangs[0].starter, mine2)
        self.assertEqual(bangs[0].mine_count, 1)
        self.assertEqual(bangs[1].t, 0)
        self.assertEqual(bangs[1].starter, mine1)
        self.assertEqual(bangs[1].mine_count, 1)

    def test_has_chain_reactions(self):
        mine1 = Mine(1, 1, 1)
        mine2 = Mine(1, 0, 1)
        mine3 = Mine(0, 1, 1)
        mine4 = Mine(1.1, 1.1, 1)
        bangs = find_big_bangs({mine1, mine2, mine3, mine4})
        self.assertEqual(len(bangs), 1)
        self.assertEqual(bangs[0].starter, mine1)
        self.assertEqual(bangs[0].t, 1)
        self.assertEqual(bangs[0].mine_count, 3)

    def test_has_multi_peak_explosion(self):
        mine1 = Mine(0, 1, 1)
        mine2 = Mine(0, 0, 1)
        bangs = find_big_bangs({mine1, mine2})
        self.assertEqual(len(bangs), 4)
        self.assertEqual(bangs[0].starter, mine2)
        self.assertEqual(bangs[0].t, 0)
        self.assertEqual(bangs[0].mine_count, 1)
        self.assertEqual(bangs[1].starter, mine2)
        self.assertEqual(bangs[1].t, 1)
        self.assertEqual(bangs[1].mine_count, 1)
        self.assertEqual(bangs[2].starter, mine1)
        self.assertEqual(bangs[2].t, 0)
        self.assertEqual(bangs[2].mine_count, 1)
        self.assertEqual(bangs[3].starter, mine1)
        self.assertEqual(bangs[3].t, 1)
        self.assertEqual(bangs[3].mine_count, 1)
