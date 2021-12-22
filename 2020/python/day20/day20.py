import re
import math

edges = dict()
matchingEdges = dict()
tiles = dict()
pictureMatrix = []
side = 0
picture = []

def readInput():
    
    content = ""
    with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day20\\input_01.txt", 'r') as f:
        content = f.read()

    tilesList = content.split('\n\n')

    for tile in tilesList:
        readTile(tile)

def readTile(tile):
    lines = list(tile.split('\n'))
    match = re.match("Tile ([0-9]*):", lines.pop(0))
    id = match[1]

    matchingEdges[id] = dict()

    # 0 -> north
    # 1 -> east/right
    # 2 -> south
    # 3 -> west/left
    edges[(id,0)] = lines[0]
    edges[(id,1)] = ''.join(map(lambda s: s[-1], lines))
    edges[(id,2)] = lines[-1]
    edges[(id,3)] = ''.join(map(lambda s: s[0], lines))

    tiles[id] = lines

def findMatchingEdges():
    edgeKeys = list(edges.keys())
    for i in range(len(edgeKeys)):
        key = edgeKeys[i]
        value = edges[key]

        for j in range(i+1,len(edgeKeys)):
            compareKey = edgeKeys[j]
            compareValue = edges[compareKey]

            if compareKey[0] == key:
                # ignore the edges of the same tile
                continue
            else:
                if value == compareValue or ''.join(reversed(value)) == compareValue:
                    matchingEdges[key[0]][key[1]] = compareKey
                    matchingEdges[compareKey[0]][compareKey[1]] = key

def stitchImage(startingTile):
    global matchingEdges
    global pictureMatrix
    global side
    global picture

    side = int(math.sqrt(len(matchingEdges)))

    pictureMatrix = []
    
    # arrange and align tiles
    next = startingTile
    for row in range(side):
        pictureMatrix.append(list())
        for col in range(side):
            pictureMatrix[row].append(next)
            alignTile(row, col)

            next = getNextTile(row, col)
    
    # remove edges and create stiched image
    for row in range(side):
        picture.extend(['']*8)
        for col in range(side):
            tile = removeEdge(pictureMatrix[row][col])
            for i in range(len(tile)):
                picture[(row*8)+i] += tile[i]


            
def alignTile(row, col):
    global tiles

    turns = getNumOfTurnsCounterClockwise(row, col)

    tileId = pictureMatrix[row][col]
    tile = tiles[tileId]
    tiles[tileId] = turnTileCounterClockwise(tile, turns)
    updateMatchingEdges(tileId, turns)

    flipIfNecessary(row, col)
    

def getNumOfTurnsCounterClockwise(row, col):
    global pictureMatrix
    global matchingEdges

    tile = pictureMatrix[row][col]
    neighbours = matchingEdges[tile]

    if row == 0 and col == 0:
        # top left corner
        return 0
    elif col == 0:
        # look up first
        top = pictureMatrix[row-1][col]
        for key, value in neighbours.items():
            if value[0] == top:
                return key # if it's on top (0) then don't turn, if it's right, then turn once, and so on
    else:
        # look left first
        left = pictureMatrix[row][col-1]
        for key, value in neighbours.items():
            if value[0] == left:
                return (key+1)%4 # if it's pointing left (3) then don't turn, if it's up, turn once and so on
                # 3 -> 0
                # 0 -> 1
                # 1 -> 2
                # 2 -> 3

def turnTileCounterClockwise(tile, turns):
    
    # 1 2 3  -> 3 6 9
    # 4 5 6     2 5 8
    # 7 8 9     1 4 7

    for i in range(turns):
        newTile = []

        for col in range(len(tile)-1,-1,-1):
            newTile.append(''.join(map(lambda s: s[col], tile)))
        
        tile = newTile

    return tile

def updateMatchingEdges(id, turns):
    offset = turns*3

    newMatchingEdges = dict()
    if turns > 0:
        for edgeKey, edgeValue in matchingEdges[id].items():
            newIndex = (edgeKey+offset)%4
            newMatchingEdges[newIndex] = edgeValue
        
        matchingEdges[id] = newMatchingEdges
            
def flipIfNecessary(row, col):
    global matchingEdges

    if col == 0 and col == 0:
        #top left corner
        return
    elif col == 0:
        # tile is turned already, if left (3) exists, then we must flip
        tileId = pictureMatrix[row][col]
        neighbours = matchingEdges[tileId]

        if 3 in neighbours:
            flipTileVertically(tileId)
    else:
        
        tileId = pictureMatrix[row][col]
        neighbours = matchingEdges[tileId]

        if row == 0:
            if 0 in neighbours:
                flipHorizontally(tileId)
        else:
            northTile = pictureMatrix[row-1][col]

            if 0 not in neighbours or neighbours[0][0] != northTile:
                flipHorizontally(tileId)

def flipTileVertically(tileId):
    global tiles
    global matchingEdges

    tile = tiles[tileId]

    newTile = flipVertically(tile)

    tiles[tileId] = newTile

    neighbours = matchingEdges[tileId]
    temp = 0
    if 3 in neighbours and 1 in neighbours:
        # shouldn't happen... all except the left most column should flip horizontally
        temp = neighbours[3]
        neighbours[3] = neighbours[1]
        neighbours[1] = temp
    elif 3 not in neighbours:
        # shouldn't happen... all except the left most column should flip horizontally
        neighbours[3] = neighbours[1]
        neighbours.pop(1)
    elif 1 not in neighbours:
        neighbours[1] = neighbours[3]
        neighbours.pop(3)

def flipVertically(tile):
    newTile = []
    for line in tile:
        newTile.append(''.join(reversed(line)))
    return newTile

def flipHorizontally(tileId):
    global tiles
    global matchingEdges

    tile = tiles[tileId]

    newTile = []
    for line in reversed(tile):
        newTile.append(line)

    tiles[tileId] = newTile

    neighbours = matchingEdges[tileId]
    if 2 not in neighbours:
        neighbours[2] = neighbours[0]
        neighbours.pop(0)
    elif 0 not in neighbours:
        neighbours[0] = neighbours[2]
        neighbours.pop(2)
    else:
        temp = neighbours[2]
        neighbours[2] = neighbours[0]
        neighbours[0] = temp

def getNextTile(row, col):
    global pictureMatrix
    global side
    global matchingEdges

    neighbours = ''
    if col == side-1:
        if row == side-1:
            # last tile - no next tile
            return None
        else:
            above = pictureMatrix[row][0]
            neighbours = matchingEdges[above]
            return neighbours[2][0]
    else:
        left = pictureMatrix[row][col]
        neighbours = matchingEdges[left]
        return neighbours[1][0]

def removeEdge(tileId):
    global tiles

    tile = tiles[tileId]
    resultTile = []
    resultTile = tile[1:len(tile)-1]

    resultTile = list(map(lambda s: s[1:len(s)-1], resultTile))

    return resultTile

def markSeamonsters(picture):
#                1    1    2
#      0....5....0....5....0
#    0                   # 
#    1 #    ##    ##    ###
#    2  #  #  #  #  #  #   
    offsets = [(0,18),(1,0),(1,5),(1,6),(1,11),(1,12),(1,17),(1,18),(1,19),(2,1),(2,4),(2,7),(2,10),(2,13),(2,16)]
    for row in range(len(picture)-2):
        for col in range(len(picture)-19): # it's a square
            isMonster = False
            for rowOffset, colOffset in offsets:
                if picture[row+rowOffset][col+colOffset] != '#':
                    isMonster = False
                    break # this is not a seamonster
                # if we end up here - it's a seamonster...
                isMonster = True
            if isMonster:
                for rowOffset, colOffset in offsets:
                    line = list(picture[row+rowOffset])
                    line[col+colOffset] = 'O'
                    picture[row+rowOffset] = ''.join(line)


readInput()
findMatchingEdges()

corners = list(filter(lambda t: len(matchingEdges[t])==2, matchingEdges))

result = 1
for corner in corners:
    result *= int(corner)

print("corner ids multiplied: " + str(result))

# stitch tiles - start with first corner, then go left to right by following the tiles dict
# rotate and flip as needed e.g. #1,1 -> #2,3 and #2,2 has no partner -> flip top to bottom
# remove edge and add to picture
# (show picture)
# find seamonsters - hm.... probably manually see if there's a rotation/flip needed for the picture
# then create a mask with offset tuples and make a compare method, send it all possible coordinates and replace all pixels with O if found
# count remaining #...
# uff

stitchImage(startingTile=corners[0])
# we need to do turn 3x counterclockwise and flip - i found out manually
picture = turnTileCounterClockwise(picture,3) 
picture = flipVertically(picture)

markSeamonsters(picture)

for line in picture:
    print(line)

count = 0
for line in picture:
    for c in line:
        if c == '#':
            count += 1

print("Roughness: "+ str(count))