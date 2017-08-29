import math

from caches import DictCache


class Bang:

    def __init__(self, starter, t, mine_count, mines):
        """
        :param mine starter: triggering mine
        :param int t: time
        :param int mine_count: number of mines exploding at T
        :param list mines: mines exploding at T
        """
        self.starter = starter
        self.t = t
        self.mine_count = mine_count
        self.mines = mines

    def __repr__(self):
        return '({}, {}) at T={}'.format(self.starter.x_coord, self.starter.y_coord, self.t)


class Mine:

    def __init__(self, x_coord, y_coord, magnitude):
        """
        :param float x_coord: x position
        :param float y_coord: y position
        :param float magnitude: explosion power. >= 0
        """
        self.x_coord = float(x_coord)
        self.y_coord = float(y_coord)
        self.magnitude = float(magnitude)

    def is_in_blast_radius(self, other):
        """
        :param mine other: other mine in question
        :return: bool
        """
        dist = math.sqrt((other.x_coord - self.x_coord) ** 2 + (other.y_coord - self.y_coord) ** 2)
        return dist <= self.magnitude


class MineField:

    def __init__(self, mines=None):
        """
        :param set mines: mines
        """
        self.mines = mines
        self.cache = DictCache()

    def get_bang_progression(self, starter):
        """
        :param mine starter: triggering mine
        :return: list
        """
        bangs = self.get_bangs({starter}, self.mines - {starter})
        return [Bang(starter, i, c[0], c[1]) for i, c in enumerate(bangs)]

    def get_bangs(self, triggers, candidates):
        """
        :param set triggers: triggering mines for this iteration
        :param set candidates: 'live' mines in the field
        :return: list
        """
        if not triggers:
            return []

        sorted_triggers = self._sort_mines(triggers)
        sorted_candidates = self._sort_mines(candidates)

        cache_namespace = 'bangs'
        cache_key = str(hash(tuple(sorted_triggers))) + str(hash(tuple(sorted_candidates)))

        bangs = self.cache.get(cache_namespace, cache_key)

        if bangs is None:
            new_triggers = set()
            for mine in sorted_triggers:
                new_triggers |= self.get_mines_in_blast_radius(mine, sorted_candidates)
            bangs = ([(len(sorted_triggers), sorted_triggers)] +
                     self.get_bangs(new_triggers, candidates - new_triggers))
            self.cache.set(cache_namespace, cache_key, bangs)

        return bangs

    def get_mines_in_blast_radius(self, trigger, candidates):
        """
        :param mine trigger: triggering mine
        :param list candidates: sorted 'live' mines in the field
        :return: set
        """
        cache_namespace = 'radius'
        cache_key = str(hash(trigger)) + str(hash(tuple(candidates)))

        mines = self.cache.get(cache_namespace, cache_key)

        if mines is None:
            mines = {m for m in candidates
                     if (abs(trigger.x_coord - m.x_coord) <= trigger.magnitude and
                         abs(trigger.y_coord - m.y_coord) <= trigger.magnitude and
                         trigger.is_in_blast_radius(m))}
            self.cache.set(cache_namespace, cache_key, mines)

        return mines

    @staticmethod
    def _sort_mines(mines):
        """
        :param iterable mines:
        :return: list
        """
        return sorted(mines, key=lambda m: (m.x_coord, m.y_coord))
