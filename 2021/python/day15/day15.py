import os,re
import numpy as np
from queue import PriorityQueue

path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input.txt") as f:
    lines = [list(l) for l in f.read().split('\n')]


directions = {'n':(0,-1),'w':(-1,0),'s':(0,1),'e':(1,0)}
side = len(lines)
map = np.array(lines, np.int8)

def initialize(map, distances):
    for x in range(side):
        for y in range(side):
            distances[(x,y)] = float('inf')
    
    distances[(0,0)] = 0

def dijkstra(map, distances, visited, nextpos: PriorityQueue):
    while not nextpos.empty():
        (distance,pos) = nextpos.get()
        visited.append(pos)

        for d in directions:
            (dx,dy) = directions[d]
            (nx,ny) = (pos[0] + dx, pos[1] + dy)
            neighbor = (nx,ny)
            if nx>=0 and nx<side and ny>=0 and ny<side and neighbor not in visited:
                olddistance = distances[neighbor]
                newdistance = int(map[ny,nx]) + distances[pos]
                if newdistance < olddistance:
                    nextpos.put((newdistance, neighbor))
                    distances[neighbor] = newdistance


# predecessor = dict()
visited = []
nextpos = PriorityQueue()
nextpos.put((0, (0,0)))
distances = dict()
initialize(map, distances)
dijkstra(map, distances, visited, nextpos)

print('Part1: shortest distance to last position: ' + str(distances[(side-1,side-1)]))