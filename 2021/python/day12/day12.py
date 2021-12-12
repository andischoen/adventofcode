import os

path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input-example.txt") as f:
    lines = f.readlines()


def initializePaths(lines):
    connections = dict()
    for line in lines:
        parts = line.split('-')
        if parts[0] not in connections:
            connections[parts[0]] = set()
        if parts[1] not in connections:
            connections[parts[1]] = set()
    
        connections[parts[0]].add(parts[1])
        connections[parts[1]].add(parts[0])
    return connections

connections = initializePaths(lines)


paths = []
currentcave = 'start'
for cave in connections[currentcave]:
    path = [currentcave]
    findPaths(currentcave, path)
    paths.append(path)