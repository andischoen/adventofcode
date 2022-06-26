lines = list()
#             0123456789012
lines.append('#############')
lines.append('#...........#')
lines.append('###.#.#.#.###')
lines.append('  #.#.#.#.#  ')
lines.append('  #########  ')

positions_outside = [(1,1),(2,1),(4,1),(6,1),(8,1),(10,1),(11,1)]

class Amphipod():

    def __init__(self, letter):
        self.letter = letter
        if letter == 'A':
            self.consumption = 1
            self.target_index = 3
        elif letter == 'B':
            self.consumption = 10
            self.target_index = 5
        elif letter == 'C':
            self.consumption = 100
            self.target_index = 7
        else:
            self.consumption = 1000
            self.target_index = 9

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

    def is_done(self):
        for key,val in self.map.items():
            if (val.letter == 'A' and (key[0] != 3 or (key[1] != 2 and key[1] != 3))) or \
               (val.letter == 'B' and (key[0] != 5 or (key[1] != 2 and key[1] != 3))) or \
               (val.letter == 'C' and (key[0] != 7 or (key[1] != 2 and key[1] != 3))) or \
               (val.letter == 'D' and (key[0] != 9 or (key[1] != 2 and key[1] != 3))):
               return False

        return True

    def get_possible_movers(self) -> list():
        movers = list()
        
        for x in range(1,12): # movers in hallway
            if (x,1) in self.map:
                movers.append((x,1))

        for x in (3,5,7,9):
            if (x,2) in self.map:
                if self.map[(x,2)].target_index != x: # a amphipod in the upper part of the room that does not belong
                    movers.append((x,2))
                elif self.map[(x,3)].target_index != x: # an amphipod in the upper part belonging, but blocking someone else
                        movers.append((x,2))
            else:
                if (x,3) in self.map and self.map[(x,3)].target_index != x: # an amphipod in the lower part not belonging
                    movers.append((x,3))

        return movers

    def get_possible_dest(self, pos) -> list():
        destinations = list()
        if pos[1] > 1: # it's in a burrow
            x = pos[0]
            for xt in range(x+1,12): # targets to the right
                t = (xt,1)
                if t not in positions_outside:
                    continue
                if t not in self.map:
                    destinations.append(t)
                else:
                    break # rest is blocked
            for xt in range(x-1,0,-1): # targets to the left
                t = (xt,1)
                if t not in positions_outside:
                    continue
                if t not in self.map:
                    destinations.append(t)
                else:
                    break # rest is blocked
        else: # needs to move back
            xt = self.map[pos].target_index
            blocked = False
            step = 1
            if xt > pos[0]:
                step = -1
            for xpath in range(xt, pos[0], step): # find blockers
                if (xpath,1) in self.map:
                    return destinations # no path to destination
            if (xt,3) in self.map:
                if self.map[(xt,3)].target_index == xt: # correct amphipod on deepest position
                    destinations.append((xt,2))
            else: # correct room free
                destinations.append((xt,3))

        return destinations


class Cave2():
    def __init__(self, map: str):
        self.map = map