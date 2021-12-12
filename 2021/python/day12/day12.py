import os

path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input.txt") as f:
    lines = f.read().split('\n')


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


def findPaths(currentcave, path, connections):
    paths = []

    if currentcave == 'end':
        return [path]

    for cave in connections[currentcave]:
        if cave.isupper() or (cave.islower() and cave not in path):
            newPath = [c for c in path]
            newPath.append(cave)
            paths = paths + findPaths(cave, newPath, connections)
    
    return paths

def findPaths2small(currentcave, path, connections):
    paths = []

    if currentcave == 'end':
        return [path]

    for cave in connections[currentcave]:
        if (cave.isupper() or 
            ((cave.islower() and cave not in path) or 
            ('2' not in path and (cave != 'end' and cave != 'start')))):
            newPath = [c for c in path]
            newPath.append(cave)
            if(cave.islower() and cave in path):
                newPath.append('2')
            paths = paths + findPaths2small(cave, newPath, connections)
    
    return paths

connections = initializePaths(lines)

#print(connections)

paths = []
currentcave = 'start'
path = [currentcave]
paths = findPaths(currentcave, path, connections)


print("Part1: number of paths: " + str(len(paths)))

paths = []
currentcave = 'start'
path = [currentcave]
paths = findPaths2small(currentcave, path, connections)

#print(paths)

print("Part2: number of paths: " + str(len(paths)))