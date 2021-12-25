import os,re
import numpy as np
from numpy.ma.core import count

path = os.path.dirname(os.path.realpath(__file__))

blocks = []
with open(path + "\input.txt") as f:
    blocks = f.read().split('\n\n')


scanners = dict()
scannercoords = [(0,0,0)]
for block in blocks:
    lines = block.split('\n')
    scannerline = lines[0]
    match = re.search('--- scanner (\d+)', scannerline)
    scannerid = int(match.group(1))
    scanners[scannerid] = []
    for i in range(1, len(lines)):
        line = lines[i]
        scanners[scannerid].append(tuple([int(coord) for coord in line.split(',')]))

matrices = [np.array([[ 1, 0, 0],
                      [ 0, 1, 0],
                      [ 0, 0, 1]]),

            np.array([[ 0,-1, 0], # turn on z anti-clockwise
                      [ 1, 0, 0],
                      [ 0, 0, 1]]),

            np.array([[-1, 0, 0],
                      [ 0,-1, 0],
                      [ 0, 0, 1]]),

            np.array([[ 0, 1, 0],
                      [-1, 0, 0],
                      [ 0, 0, 1]]),

            np.array([[-1, 0, 0], # turn on z but opposite view angle
                      [ 0, 1, 0],
                      [ 0, 0,-1]]),

            np.array([[ 0,-1, 0], 
                      [-1, 0, 0],
                      [ 0, 0,-1]]),

            np.array([[ 1, 0, 0],
                      [ 0,-1, 0],
                      [ 0, 0,-1]]),

            np.array([[ 0, 1, 0],
                      [ 1, 0, 0],
                      [ 0, 0,-1]]),

            np.array([[ 1, 0, 0], # turn on y -> z = -y, y = z
                      [ 0, 0, 1],
                      [ 0,-1, 0]]),

            np.array([[ 0, 0,-1],
                      [ 1, 0, 0],
                      [ 0,-1, 0]]),

            np.array([[-1, 0, 0],
                      [ 0, 0,-1],
                      [ 0,-1, 0]]),

            np.array([[ 0, 0, 1],
                      [-1, 0, 0],
                      [ 0,-1, 0]]),

            np.array([[ 0, 0, 1], # turn on y but opposite view angle
                      [ 1, 0, 0],
                      [ 0, 1, 0]]),

            np.array([[-1, 0, 0],
                      [ 0, 0, 1],
                      [ 0, 1, 0]]),

            np.array([[ 0, 0,-1],
                      [-1, 0, 0],
                      [ 0, 1, 0]]),

            np.array([[ 1, 0, 0],
                      [ 0, 0,-1],
                      [ 0, 1, 0]]),

            np.array([[ 0, 0, 1], # turn on x anti-clockwise -> z = -x
                      [ 0, 1, 0],
                      [-1, 0, 0]]),

            np.array([[ 0,-1, 0],
                      [ 0, 0, 1],
                      [-1, 0, 0]]),

            np.array([[ 0, 0,-1],
                      [ 0,-1, 0],
                      [-1, 0, 0]]),

            np.array([[ 0, 1, 0],
                      [ 0, 0,-1],
                      [-1, 0, 0]]),

            np.array([[ 0, 0,-1], # turn on x but opposite view angle
                      [ 0, 1, 0],
                      [ 1, 0, 0]]),

            np.array([[ 0,-1, 0],
                      [ 0, 0,-1],
                      [ 1, 0, 0]]),

            np.array([[ 0, 0, 1],
                      [ 0,-1, 0],
                      [ 1, 0, 0]]),

            np.array([[ 0, 1, 0],
                      [ 0, 0, 1],
                      [ 1, 0, 0]])]

def findoverlappingscanners(scanners):
    beacons = set(scanners[0])

    scanners.pop(0)

    while len(scanners) > 0:
        for k in [k for k in scanners.keys()]:
            if trymatch(beacons, scanners[k]):
                scanners.pop(k)
            print(str(len(scanners)))

    return beacons

def trymatch(beacons, scanner):
    result = False
    # create matrix and try to find matches, min 12
    matrix = None
    matrix = findtranslations(beacons, scanner)
    if not(matrix is None):
        result = True
        for x,y,z in scanner:
            px,py,pz,one = np.matmul(matrix, np.array([[x],[y],[z],[1]]))
            point = (int(px),int(py),int(pz))
            beacons.add(point)
        px,py,pz,one = np.matmul(matrix, np.array([[0],[0],[0],[1]]))
        scannercoord = (int(px),int(py),int(pz))
        scannercoords.append(scannercoord)
    return result

def findtranslations(beacons, scanner):
    matrix = None
    for b in beacons:
        for p in scanner:
            matrix = matchpoints(b, p, beacons, scanner)
            if not(matrix is None):
                return matrix
    return matrix

def matchpoints(b,p,beacons,scanner):
    length = len(scanner)
    for matrix in matrices:
        # rotate point first
        translatedp = np.matmul(matrix, p)
        vector = b-translatedp
        translatematrix = np.r_[np.c_[matrix,vector],[(0,0,0,1)]]

        countmatch = 0
        counttotal = 0
        for x,y,z in scanner:
            px,py,pz,one = np.matmul(translatematrix, np.array([[x],[y],[z],[1]]))
            point = (int(px),int(py),int(pz))
            if point in beacons:
                countmatch += 1
            counttotal += 1

            if countmatch == 12:
                return translatematrix

            if (length - counttotal + countmatch) < 12:
                #that's not it
                break
    return None

def getmanhattan(coord1, coord2):
    return abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1]) + abs(coord1[2]-coord2[2])



beacons = findoverlappingscanners(scanners)
print("Part1: num of total beacons: " + str(len(beacons)))

def getmaxmanhattan(scannercoords, getmanhattan):
    maxdist = None
    for i in range(len(scannercoords)):
        for j in range(i+1, len(scannercoords)):
            dist = getmanhattan(scannercoords[i], scannercoords[j])
            if maxdist == None or dist > maxdist:
                maxdist = dist
    return maxdist

maxdist = getmaxmanhattan(scannercoords, getmanhattan)

print("Part2: Max manhattan distance = " + str(maxdist))