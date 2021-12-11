import os
from os import system, name

directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
def makeOneStep(oceanfloor):
    length = len(oceanfloor)
    fired = [[False for i in range(length)] for i in range(length)]

    increaseoctopi(oceanfloor, length)

    for x in range(length):
        for y in range(length):
            fire(oceanfloor, x, y, fired, length)
    
    for x in range(length):
        for y in range(length):
            if oceanfloor[y][x] > 9:
                oceanfloor[y][x] = 0

    printfloor(oceanfloor, fired, length)
    return sum([sum(a) for a in fired])


def fire(oceanfloor, x, y, fired, length):
    if oceanfloor[y][x] > 9 and not fired[y][x]:
        fired[y][x] = True
        for dX, dY in directions:
            nX = x+dX
            nY = y+dY
            if nX >= 0 and nX < length and nY >= 0 and nY < length:
                oceanfloor[nY][nX] += 1
                fire(oceanfloor,nX,nY,fired,length)


def increaseoctopi(oceanfloor, length):
    for x in range(length):
        for y in range(length):
            oceanfloor[y][x] += 1


def printfloor(oceanfloor, fired, length):
    for y in range(length):
        print("".join([str(i) for i in oceanfloor[y]]) + "  " + "".join([str(int(b)) for b in fired[y]]))

    print("")

path = os.path.dirname(os.path.realpath(__file__))

oceanfloor = []
with open(path + "\input.txt") as f:
    for line in f.read().split():
        oceanfloor.append([int(n) for n in line])


flashes = 0
for i in range(100):
    flashes += makeOneStep(oceanfloor)

print("Part1: number of flashes after 100 steps = " + str(flashes))

for i in range(10000):
    flashes = makeOneStep(oceanfloor)
    if flashes == 100:
        print("Part2: step when all flash: " + str(i+101))
        break