import os, re

path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input.txt") as f:
    lines = f.read().split()


directions = [(-1,0),(0,1),(1,0),(0,-1)]

maxDown = len(lines)
maxRight = len(lines[0])

solution = 0
lowpoints = []
for y in range(maxDown):
    for x in range(maxRight):
        pos = int(lines[y][x])

        lowPoint = True
        for down,right in directions:
            neighbourX = x+right
            neighbourY = y+down
            if neighbourX >= 0 and neighbourX < maxRight and neighbourY >= 0 and neighbourY < maxDown:
                neighbour = int(lines[neighbourY][neighbourX])
                if neighbour <= pos:
                    lowPoint = False
                    break
        
        if lowPoint:
            solution += 1 + pos
            lowpoints.append((x,y))

print("Sum lowpoints: " + str(solution))
