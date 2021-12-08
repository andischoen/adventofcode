import os, re

path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input.txt") as f:
    lines = f.readlines()

output = []
for line in lines:
    match = re.search(".* \| (\w+) (\w+) (\w+) (\w+)", line)
    output.append(match.group(1))
    output.append(match.group(2))
    output.append(match.group(3))
    output.append(match.group(4))

count = 0
for digit in output:
    length = len(digit)
    if length == 2 or length == 4 or length == 3 or length == 7:
        count += 1

print("Count of 1, 4, 7, 8: " + str(count))