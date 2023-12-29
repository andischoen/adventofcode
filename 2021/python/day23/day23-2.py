import os
import day23lib as lib

path = os.path.dirname(os.path.realpath(__file__))

walls_and_spaces = (' ', '#')
map = dict()
cave = ''
with open(path + "\input.txt") as f:
    for line in f.read().split('\n'):
        cave += ''.join([c for c in line if c not in walls_and_spaces])

print(cave)

