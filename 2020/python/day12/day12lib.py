east = 0
south = 0
orientation = 0
orientations = ('E', 'S', 'W', 'N')
waypointEast = 10
waypointSouth = -1

def processInstruction(instruction):
    global east
    global south
    global orientation
    global orientations

    direction = instruction[0]
    distance = int(instruction[1:len(instruction)])

    if direction == 'N':
        south -= distance
    elif direction == 'E':
        east += distance
    elif direction == 'S':
        south += distance
    elif direction == 'W':
        east -= distance
    elif direction == 'L':
        distance = int(distance / 90)
        orientation -= distance
        orientation = orientation % 4
    elif direction == 'R':
        distance = int(distance / 90)
        orientation += distance
        orientation = orientation % 4
    elif direction == 'F':
        processInstruction(orientations[orientation] + str(distance))

def turnLeft(times):
    global waypointSouth
    global waypointEast

    # e:1 s:2   e:2 s:-1
    # ......    ......
    # ......    ....x.
    # ..#...    ..#...
    # ......    ......
    # ...x..    ......

    if times == 1:
        temp = waypointEast
        waypointEast = waypointSouth
        waypointSouth = -temp
    elif times == 2:
        turnAround()
    elif times == 3:
        turnRight(1)

def turnRight(times):
    global waypointSouth
    global waypointEast
    
    # e:1 s:2   e:-1 s:1
    # ......    ......
    # ......    ......
    # ..#...    ..#...
    # ......    x.....
    # ...x..    ......

    if times == 1:
        temp = waypointEast
        waypointEast = -waypointSouth
        waypointSouth = temp
    elif times == 2:
        turnAround()
    elif times == 3:
        turnLeft(1)

def turnAround():
    global waypointSouth
    global waypointEast

    # e:1 s:2   e:-1 s:-2
    # ......    .x....
    # ......    ......
    # ..#...    ..#...
    # ......    ......
    # ...x..    ......

    waypointSouth = -waypointSouth
    waypointEast = -waypointEast

def processInstruction2(instruction):
    global east
    global south
    global waypointEast
    global waypointSouth

    direction = instruction[0]
    distance = int(instruction[1:len(instruction)])

    if direction == 'N':
        waypointSouth -= distance
    elif direction == 'E':
        waypointEast += distance
    elif direction == 'S':
        waypointSouth += distance
    elif direction == 'W':
        waypointEast -= distance
    elif direction == 'L':
        distance = int(distance / 90)
        turnLeft(distance)
    elif direction == 'R':
        distance = int(distance / 90)
        turnRight(distance)
    elif direction == 'F':
        east += (waypointEast*distance)
        south += (waypointSouth*distance)
        

def getManhattanDistance():
    return abs(east) + abs(south)

