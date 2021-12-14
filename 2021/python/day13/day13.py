import os,re

path = os.path.dirname(os.path.realpath(__file__))

coords = []
folds = []
with open(path + "\input.txt") as f:
    halves = f.read().split('\n\n')
    coords = halves[0].split('\n')
    folds = halves[1].split('\n')


def fold(page, fold):
    match = re.search('fold along (.)=(\d+)', fold)
    foldalongaxis = match.group(1)
    foldalong = int(match.group(2))

    foldedpage = dict()
    for x,y in page.keys():
        nX = x
        nY = y
        if foldalongaxis == 'y' and y > foldalong:
            nY = foldalong-(y-foldalong)
        elif foldalongaxis == 'x' and x > foldalong:
            nX = foldalong-(x-foldalong)

        foldedpage[(nX,nY)] = True

    return foldedpage


def printpage(page):
    minX = None
    minY = None
    maxX = None 
    maxY = None
    for x,y in page:
        if minX == None or x < minX:
            minX = x
        if minY == None or y < minY:
            minY = y
        if maxX == None or x > maxX:
            maxX = x
        if maxY == None or y > maxY:
            maxY = y
    
    for y in range(minY, maxY+1):
        for x in range(minX, maxX+1):
            if (x,y) in page:
                print('#', end='')
            else:
                print('.', end='')
        print('\n', end='')




page = dict()
for coord in coords:
    parts = coord.split(',')
    x = int(parts[0])
    y = int(parts[1])

    page[(x,y)] = True

page = fold(page, folds[0])

numofdots = len([b for b in page.values() if b])
print("Part1: number of dots after first fold: " + str(numofdots))

for i in range(1,len(folds)):
    page = fold(page, folds[i])

print("Part2: ")
printpage(page)