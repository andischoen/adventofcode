import os, re, math

directions = [(-1,0),(0,1),(1,0),(0,-1)]

path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input.txt") as f:
    lines = f.read().split()


maxDown = len(lines)
maxRight = len(lines[0])

def calculateBasin(lowpoint, map):
    basin = set()
    basin.add(lowpoint)
    addToBasin(lowpoint, map, basin)

    return len(basin)

def addToBasin(lowpoint, map, basin):
    lowpointX = lowpoint[0]
    lowpointY = lowpoint[1]
    lowpointValue = int(map[lowpointY][lowpointX])

    for dirX,dirY in directions:
        neighbourX = lowpointX + dirX
        neighbourY = lowpointY + dirY
        if isInBounds(neighbourX, neighbourY):
            neighbourValue = int(map[neighbourY][neighbourX])
            if neighbourValue > lowpointValue and neighbourValue != 9:
                basin.add((neighbourX, neighbourY))
                addToBasin((neighbourX,neighbourY), map, basin)
    

def isInBounds(neighbourX, neighbourY):
    return neighbourX >= 0 and neighbourX < maxRight and neighbourY >= 0 and neighbourY < maxDown



solution = 0
lowpoints = []
for y in range(maxDown):
    for x in range(maxRight):
        pos = int(lines[y][x])

        isLowPoint = True
        for down,right in directions:
            neighbourX = x+right
            neighbourY = y+down
            if isInBounds(neighbourX, neighbourY):
                neighbour = int(lines[neighbourY][neighbourX])
                if neighbour <= pos:
                    isLowPoint = False
                    break
        
        if isLowPoint:
            solution += 1 + pos
            lowpoints.append((x,y))

print("Part 1 - Sum lowpoints: " + str(solution))


basins = []
for low in lowpoints:
    basins.append(calculateBasin(low, lines))

basins = sorted(basins, reverse=True)
largestBasinsMultiplied = math.prod(basins[0:3])

print("Part 2: 3 largest basins multiplied: " + str(largestBasinsMultiplied))

