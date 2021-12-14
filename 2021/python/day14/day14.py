import os,re
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))

polymere = ''
lines = []
with open(path + "\input-example.txt") as f:
    halves = f.read().split('\n\n')
    polymere = halves[0]
    lines = halves[1].split('\n')

rules = dict()
for line in lines:
    match = re.search('(\w+) -> (\w)',line)
    rules[match.group(1)] = match.group(2)

#print(rules)

def pairinsertion(polymere, rules):
    newpolymere = []
    print("".join(polymere)) 
    for i in range(len(polymere)-1):
        newpolymere.append(polymere[i])
        newpolymere.append(rules[polymere[i]+polymere[i+1]])
    newpolymere.append(polymere[-1])
    return newpolymere

iterations = 12
for i in range(iterations):
    polymere = pairinsertion(polymere, rules)

count = Counter(polymere)

countmostcommon = count.most_common()

print(countmostcommon[0])
print(countmostcommon[-1])

mostminusleast = countmostcommon[0][1] - count.most_common()[-1][1]

print("most common element after " + str(iterations) + " iterations minus least common: " + str(mostminusleast))