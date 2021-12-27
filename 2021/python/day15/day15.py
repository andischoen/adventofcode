import os,re
import numpy as np
import heapq
from queue import PriorityQueue

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position
    
    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"

    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    
    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f


path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input.txt") as f:
    lines = [list(l) for l in f.read().split('\n')]


directions = {'n':(0,-1),'w':(-1,0),'s':(0,1),'e':(1,0)}
map = np.array(lines, np.int8)
side = len(map)

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
                    print(str(len(visited)))


# predecessor = dict()
def getdistances(map, initialize, dijkstra):
    visited = []
    nextpos = PriorityQueue()
    nextpos.put((0, (0,0)))
    distances = dict()
    initialize(map, distances)
    dijkstra(map, distances, visited, nextpos)
    return distances


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = dict()

    # Heapify the open_list and Add the start node
    heapq.heapify(open_list) 
    heapq.heappush(open_list, start_node)

    # Adding a stop condition
    outer_iterations = 0
    max_iterations = (len(maze[0]) * len(maze) // 2)

    # Loop until you find the end
    while len(open_list) > 0:
        outer_iterations += 1

        # if outer_iterations > max_iterations:
        #   # if we hit this point return the path such as it is
        #   # it will not contain the destination
        #   print("giving up on pathfinding too many iterations")
        #   return None   
        
        # Get the current node
        current_node = heapq.heappop(open_list)
        closed_list[current_node.position] = current_node

        # Found the goal
        if current_node == end_node:
            return current_node.g

        # Generate children
        children = []
        
        for new_position in directions.values(): # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0]>=side or node_position[0]<0 or node_position[1]>=side or node_position[1]<0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            # Child is on the closed list
            if child.position in closed_list:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + map[child.position[1],child.position[0]]
            child.h = ((abs(child.position[0] - end_node.position[0])) + (abs(child.position[1] - end_node.position[1])))
            child.f = child.g + child.h

            # Child is already in the open list
            if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                continue

            # Add the child to the open list
            heapq.heappush(open_list, child)
        print(str(len(closed_list)))
    print("Couldn't get a path to destination")
    return None
# part 1
# distances = getdistances(map, initialize, dijkstra)

# print('Part1: shortest distance to last position: ' + str(distances[(side-1,side-1)]))

origtile = np.copy(map)
for i in range(1,5):
    map = np.concatenate((map,np.array([[((c+i+8)%9)+1 for c in r] for r in origtile])),axis=1)

origtile = np.copy(map)
for i in range(1,5):
    map = np.concatenate((map,np.array([[((c+i+8)%9)+1 for c in r] for r in origtile])), axis=0)

side = len(map)
# distances = getdistances(map, initialize, dijkstra)
bla = astar(map, (0,0), (side-1,side-1))

print('Part2: shortest distance to last position: ' + str(bla))
# print('Part2: shortest distance to last position: ' + str(distances[(side-1,side-1)]))