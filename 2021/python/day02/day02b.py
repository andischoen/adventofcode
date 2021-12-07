
import os

path = os.path.dirname(os.path.realpath(__file__))

f = open(path + "\input.txt", "r")

depth = 0
pos = 0
aim = 0
for line in f:
    parts = line.split()
    if parts[0] == "up":
        aim -= int(parts[1])
    elif parts[0] == "down":
        aim += int(parts[1])
    else:
        x = int(parts[1])
        pos += x
        depth += x*aim

print(depth*pos)