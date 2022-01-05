import functools

p1_score = 0
p2_score = 0

p1_pos = 8
p2_pos = 7
# p1_pos = 4
# p2_pos = 8

# (1 2 3) die1
# (1 2 3) die2
# (1 2 3) die3

# 111, 112, 113 -> 3, 4, 5
# 121, 122, 123 -> 4, 5, 6
# 131, 132, 133 -> 5, 6, 7
# 211, 212, 213 -> 4, 5, 6
# 221, 222, 223 -> 5, 6, 7
# 231, 232, 233 -> 6, 7, 8
# 311, 312, 313 -> 5, 6, 7
# 321, 322, 323 -> 6, 7, 8
# 331, 332, 333 -> 7, 8, 9
roll_frequency = [(3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1)]

@functools.lru_cache(maxsize=None)
def play(p1_pos, p1_score, p2_pos, p2_score):
    if p2_score >= 21:
        return 0,1

    p1_wins = p2_wins = 0
    for r,f in roll_frequency:
        np1_pos = (p1_pos + r)%10 if (p1_pos + r)%10 else 10
        np1_score = np1_pos+p1_score
        w2,w1 = play(p2_pos, p2_score, np1_pos, np1_score)
        p1_wins += f*w1
        p2_wins += f*w2
    
    return p1_wins, p2_wins


wins1, wins2 = play(p1_pos, p1_score, p2_pos, p2_score)

print("Part2 results P1, P2 -> " + str(wins1) + ", " + str(wins2))