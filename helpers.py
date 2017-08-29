import re

from exceptions import MineValueError
from models import Mine


def make_mine(s):
    mine_data = [re.sub('[()]', '', x) for x in s.split(',') if x]
    try:
        return Mine(*mine_data)
    except (TypeError, ValueError):
        raise MineValueError()


def process_input(s):
    return {make_mine(m) for m in s.replace(' ', '').split('),') if m}
