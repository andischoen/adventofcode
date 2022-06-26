import os
import day23lib as lib

path = os.path.dirname(os.path.realpath(__file__))


lowest_score = 14376

# done? -> compare score and store if lower
# else: 
#   if score higher - return
#   who can move?
#   for each: where can they move
#       for each move:
#           copy cave and move, calc score, pass to subsequent call

def make_move(cave: lib.Cave):
    global lowest_score
    if cave.is_done():
        if lowest_score == None or cave.score < lowest_score:
            lowest_score = cave.score
            print(cave)
            print(lowest_score)
            print(cave.moves)
        return

    if lowest_score != None and cave.score > lowest_score:
        return

    #TODO run deadlock detection here
    possible_movers = cave.get_possible_movers()
    for m in possible_movers:
        possible_dest = cave.get_possible_dest(m)
        for d in possible_dest:
            new_cave = lib.Cave(cave.map, cave.score, cave.moves)
            new_cave.move(m, d)
            # print(new_cave)
            make_move(new_cave)


walls_and_spaces = (' ', '.', '#')
map = dict()
with open(path + "\input.txt") as f:
    y = 0
    for line in f.read().split('\n'):
        for x in range(len(line)):
            if line[x] not in walls_and_spaces:
                map[(x,y)] = lib.Amphipod(line[x])
        y += 1

cave = lib.Cave(map,0,list())
score = None

make_move(cave)

print(lowest_score)


