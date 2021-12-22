

activeCubes = dict()
neighbours = [(-1,-1, 0),
              (-1, 0, 0),
              (-1, 1, 0),
              ( 0,-1, 0),
              #middle
              ( 0, 1, 0),
              ( 1,-1, 0),
              ( 1, 0, 0),
              ( 1, 1, 0),

              (-1,-1,-1),
              (-1, 0,-1),
              (-1, 1,-1),
              ( 0,-1,-1),
              ( 0, 0,-1),
              ( 0, 1,-1),
              ( 1,-1,-1),
              ( 1, 0,-1),
              ( 1, 1,-1),
              
              (-1,-1, 1),
              (-1, 0, 1),
              (-1, 1, 1),
              ( 0,-1, 1),
              ( 0, 0, 1),
              ( 0, 1, 1),
              ( 1,-1, 1),
              ( 1, 0, 1),
              ( 1, 1, 1),]


def readInput():
    global activeCubes

    inputLines = []
    with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day17\\input_01.txt", 'r') as f:
        inputLines = f.readlines()

    for r in range(len(inputLines)):
        line = inputLines[r].strip()
        for c in range(len(line)):
            if line[c] == '#':
                activeCubes[(r,c,0)] = True
    
def iterate():
    global activeCubes

    nextConfig = dict()

    minR = None
    maxR = None
    minC = None
    maxC = None
    minZ = None
    maxZ = None
    for r,c,z in activeCubes:
        if minR == None or r<minR:
            minR = r
        if maxR == None or r>maxR:
            maxR = r
        if minC == None or c<minC:
            minC = c
        if maxC == None or c>maxC:
            maxC = c
        if minZ == None or z<minZ:
            minZ = z
        if maxZ == None or z>maxZ:
            maxZ = z
    minR -= 1
    maxR += 1
    minC -= 1
    maxC += 1
    minZ -= 1
    maxZ += 1

    for r in range(minR, maxR+1):
        for c in range(minC, maxC+1):
            for z in range(minZ, maxZ+1):
                numNeighbours = getActiveNeighbours(r,c,z)
                
                if (r,c,z) in activeCubes and (numNeighbours == 2 or numNeighbours == 3):
                    nextConfig[(r,c,z)] = True
                elif (r,c,z) not in activeCubes and numNeighbours == 3:
                    nextConfig[(r,c,z)] = True

    activeCubes = nextConfig                

        
def getActiveNeighbours(r,c,z):
    global activeCubes
    global neighbours

    count = 0
    for rOffset,cOffset,zOffset in neighbours:
        if (r+rOffset, c+cOffset, z+zOffset) in activeCubes:
            count += 1

    return count

readInput()
for i in range(6):
    iterate()
count = len(activeCubes)
print("number of active cubes after 6 iterations: " + str(count))