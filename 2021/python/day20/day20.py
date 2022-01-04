import os,re
import math

path = os.path.dirname(os.path.realpath(__file__))

neighbours = [(-1,-1),(0,-1),(1,-1),(-1,0),(0,0),(1,0),(-1,1),(0,1),(1,1)]

lookup = []
image = dict()
outside = '0'

with open(path + "\input.txt") as f:
    parts = f.read().split('\n\n')
    lookup = ['0']*512 
    for i in range(len(parts[0])):
        if parts[0][i] == '#':
            lookup[i] = '1'
        else:
            lookup[i] = '0'

    lines = parts[1].split('\n')
    for i in range(len(lines)):
        line = lines[i]
        for pos in range(len(line)):
            if line[pos] == '#':
                image[(pos,i)] = '1'
            else:
                image[(pos,i)] = '0'

def iterate(image):
    global outside
    next = dict()

    minx,miny,maxx,maxy = get_bounds(image)

    for x in range(minx,maxx+1):
        for y in range(miny, maxy+1):
            bin = ''
            for dx,dy in neighbours:
                nx = x+dx
                ny = y+dy
                if (nx,ny) in image:
                    bin += image[(nx,ny)]
                else:
                    bin += outside
            index = int(bin,2)
            next[(x,y)] = lookup[index]

    if lookup[0] == '1':
        if outside == '0':
            outside = '1'
        else:
            outside = '0'

    return next


def get_bounds(image):
    minx = miny = maxx = maxy = None

    for x,y in image.keys():
        if image[(x,y)] == '1':
            if minx == None or minx > x:
                minx = x
            if maxx == None or maxx < x:
                maxx = x
            if miny == None or miny > y:
                miny = y
            if maxy == None or maxy < y:
                maxy = y

    return minx-4,miny-4,maxx+4,maxy+4


for i in range(2):
    image = iterate(image)

count = len([c for c in image.values() if c == '1'])

print("Part1: count of light pixels = " + str(count))

for i in range(48):
    image = iterate(image)

count = len([c for c in image.values() if c == '1'])

print("Part1: count of light pixels = " + str(count))