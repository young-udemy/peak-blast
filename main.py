import time

from exceptions import MineValueError
from helpers import process_input
from mines import find_big_bangs


file_name = input('Enter file name with mine data.\n'
                  'Format: (x-coord, y-coord, explosion power)\n'
                  'Example: (1.0, 2.0, 1.5), ..., (2.0, 3.0, 2.0)\n\n')


try:
    file = open(file_name, 'r')
    mine_data = file.read()
except FileNotFoundError:
    print('Data file not found')
    exit()


try:
    mines = process_input(mine_data)
except MineValueError:
    print('Invalid input')
    exit()


elapsed = 0
if mines:
    s = time.perf_counter()
    bangs = find_big_bangs(mines)
    elapsed = '{0:.2f}'.format(time.perf_counter() - s)

    print('Peak explosion count: {}'.format(bangs[0].mine_count))
    for bang in bangs:
        print(bang)


print('\n{} mine(s) processed in {} seconds.'.format(len(mines), elapsed))
