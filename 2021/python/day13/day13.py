import os

path = os.path.dirname(os.path.realpath(__file__))

coords = []
folds = []
with open(path + "\input-example.txt") as f:
    halves = f.read().split('\n\n')
    coords = halves[0].split('\n')
    folds = halves[1].split('\n')


def fold(page, fold):
    return 0


page = dict()
for coord in coords:
    parts = coord.split(',')
    x = int(parts[0])
    y = int(parts[1])

    page[(x,y)] = True

fold(page, folds[0])

numofdots = len([b for b in page.values() if b])
print("Part1: number of dots after first fold: " + str(numofdots))

