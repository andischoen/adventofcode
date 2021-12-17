import os,re

path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input-example.txt") as f:
    lines = f.read().split('\n')


directions = [(0,-1),(-1,0),(0,1),(1,0)]
side = len(lines)

for x in range(side):
    for y in range(side):
        findshortestpath(lines)