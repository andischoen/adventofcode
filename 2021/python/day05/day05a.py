
import re

def processCloud(map, x1,y1,x2,y2):
    if x1 == x2:
        r = []
        if y1 < y2:
            r = range(y1, y2+1)
        else:
            r = range(y2, y1+1)

        for y in r:
            if (x1,y) not in map:
                map[(x1,y)] = 1
            else:
                map[(x1,y)] += 1
    elif y1 == y2:
        r = []
        if x1 < x2:
            r = range(x1,x2+1)
        else:
            r = range(x2,x1+1)
        
        for x in r:
            if (x,y1) not in map:
                map[(x,y1)] = 1
            else:
                map[(x,y1)] += 1

def processDiagonal(map, x1,y1,x2,y2):
    change = None
    if x1 < x2 and y1 < y2: # down and to the right
        change = (1,1)
    elif x1 > x2 and y1 < y2: # down and to the left
        change = (-1,1)
    elif x1 < x2 and y1 > y2: # up and to the right
        change = (1,-1)
    elif x1 > x2 and y1 > y2: # up and to the left
        change = (-1,-1)

    if change != None:
        x,y = x1,y1
        while (x,y) != (x2,y2):
            if(x,y) not in map:
                map[(x,y)] = 1
            else:
                map[(x,y)] += 1
            x += change[0]
            y += change[1]
        if(x,y) not in map:
            map[(x,y)] = 1
        else:
            map[(x,y)] += 1




lines = []

with open("C:\\python\\aoc\\adventofcode\\2021\\python\\day05\\day05.txt", 'r') as f:
    lines = f.readlines()


map = dict()
for line in lines:
    match = re.search("(\d+),(\d+) -> (\d+),(\d+)", line)
    x1,y1 = int(match.group(1)), int(match.group(2)) 
    x2,y2 = int(match.group(3)), int(match.group(4))

    processCloud(map, x1,y1,x2,y2)

print("part 1: " + str(len([v for v in map.values() if v > 1])))
    
for line in lines:
    match = re.search("(\d+),(\d+) -> (\d+),(\d+)", line)
    x1,y1 = int(match.group(1)), int(match.group(2)) 
    x2,y2 = int(match.group(3)), int(match.group(4))

    processDiagonal(map, x1,y1,x2,y2)

print("part 2: " + str(len([v for v in map.values() if v > 1])))