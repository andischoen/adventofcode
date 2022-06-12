import os,re,math

path = os.path.dirname(os.path.realpath(__file__))

#############
#...........#
###.#.#.#.###
  #.#.#.#.#
  #########
lines = list()
lines.append('#############')
lines.append('#...........#')
lines.append('###.#.#.#.###')
lines.append('  #.#.#.#.#  ')
lines.append('  #########  ')

class Amphipod():

    def __init__(self, letter):
        self.letter = letter
        if letter == 'A':
            self.consumption = 1
        elif letter == 'B':
            self.consumption = 10
        elif letter == 'C':
            self.consumption = 100
        else:
            self.consumption = 1000

class Cave():

    def __init__(self, map:dict, score, moves:list):
        self.map = map.copy()
        self.score = score
        self.moves = moves.copy()


    def __str__(self) -> str:
        out = ''
        for y in range(len(lines)):
            for x in range(13):
                if (x,y) in self.map:
                    out += self.map[(x,y)].letter
                else:
                    out += lines[y][x]
            if y == 0:
                out += '\t' + str(self.score)
            out += '\n'
        
        return out

    def move(self, start, dest):
        a = self.map.pop(start)
        self.map[dest] = a
        dist = abs(start[0]-dest[0]) + abs(start[1] - dest[1])
        self.score += dist * a.consumption

        self.moves.append((start,dest,a.letter))

    def print_moves(self):
        for m in self.moves:
            print(m)
            

walls_and_spaces = (' ', '.', '#')
map = dict()
with open(path + "\input.txt") as f:
    y = 0
    for line in f.read().split('\n'):
        for x in range(len(line)):
            if line[x] not in walls_and_spaces:
                map[(x,y)] = Amphipod(line[x])
        y += 1

cave = Cave(map,0,list())
score = None

# done? -> compare score and store if lower
# else: 
#   if score higher - return
#   who can move?
#   for each: where can they move
#       for each move:
#           copy cave and move, calc score, pass to subsequent call


