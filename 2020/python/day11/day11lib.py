seats = []
directions = ((1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1))

def getOccupiedSeatInDirection(row, col, rowInc,colInc):
    global seats
    r = row + rowInc
    c = col + colInc
    while c>=0 and c<len(seats[0]) and r>=0 and r<len(seats):
        if seats[r][c] == '#':
            return 1
        elif seats[r][c] == 'L':
            return 0
        r += rowInc
        c += colInc
    return 0
    
    

def getOccupiedVisualSeats(row, col):
    global seats
    count = 0
    for r,c in directions:
        count += getOccupiedSeatInDirection(row, col, r,c)
    return count

def getOccupiedSurroundingSeats(row, col):
    global seats
    count = 0

    for rowInc,colInc in directions:
        c = col + colInc
        r = row + rowInc
        if c>=0 and c<len(seats[0]) and r>=0 and r<len(seats):
            if seats[r][c] == '#':
                count += 1    
    return count

def switchSeats():
    global seats

    newSeatConfig = []
    switch = False
    for row in range(len(seats)):
        line = seats[row]
        newSeatConfig.append([])
        for col in range(len(line)):
            occupiedSurroungings = 0
            occupiedSurroungings = getOccupiedSurroundingSeats(row, col)
            if seats[row][col] == 'L' and occupiedSurroungings == 0:
                    newSeatConfig[row].append('#')
                    switch = True
            elif seats[row][col] == '#' and occupiedSurroungings >= 4:
                    newSeatConfig[row].append('L')
                    switch = True
            else:
                newSeatConfig[row].append(seats[row][col])
    
    seats = newSeatConfig
    
    return switch

def switchSeats2():
    global seats

    newSeatConfig = []
    switch = False
    for row in range(len(seats)):
        line = seats[row]
        newSeatConfig.append([])
        for col in range(len(line)):
            occupiedSeats = 0
            occupiedSeats = getOccupiedVisualSeats(row, col)
            if seats[row][col] == 'L' and occupiedSeats == 0:
                    newSeatConfig[row].append('#')
                    switch = True
            elif seats[row][col] == '#' and occupiedSeats >= 5:
                    newSeatConfig[row].append('L')
                    switch = True
            else:
                newSeatConfig[row].append(seats[row][col])
    
    seats = newSeatConfig
    
    return switch

def getOccupiedSeats():
    global seats
    count = 0

    for row in range(len(seats)):
        line = seats[row]
        for col in range(len(line)):
            if seats[row][col] == '#':
                count += 1
    return count

def setSeats(s):
    global seats
    seats = s