p1_score = 0
p2_score = 0

p1_pos = 8
p2_pos = 7

class Die:
    def __init__(self, val):
        self.next = None
        self.val = val

def roll(pos):
    global die
    npos = pos
    for i in range(3):
        npos += die.val
        die = die.next
    npos = npos % 10
    if npos == 0:
        npos = 10    

    return npos

def init_die(sides):
    d = Die(1)
    one = d
    for i in range(2,sides+1):
        d.next = Die(i)
        d = d.next
    d.next = one
    return one

die = init_die(100)
roll_count = 0
flip_flop = True
while p1_score < 1000 and p2_score < 1000:
    roll_count += 3
    if flip_flop:
        p1_pos = roll(p1_pos)
        p1_score += p1_pos
    else:
        p2_pos = roll(p2_pos)
        p2_score += p2_pos

    flip_flop = not flip_flop

score = 0
if p1_score >= 1000:
    score = p2_score
else:
    score = p1_score

print("Part1: lower score x rolls: " + str(score*roll_count))