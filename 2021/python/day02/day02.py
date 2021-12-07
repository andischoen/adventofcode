import os

path = os.path.dirname(os.path.realpath(__file__))

f = open(path + "\input.txt", "r")

depth = 0
pos = 0
for line in f:
    parts = line.split()
    if parts[0] == "up":
        depth -= int(parts[1])
    elif parts[0] == "down":
        depth += int(parts[1])
    else:
        pos += int(parts[1])

print(depth*pos)