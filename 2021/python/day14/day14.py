import os,re
from collections import Counter

path = os.path.dirname(os.path.realpath(__file__))

polymere = ''
lines = []
with open(path + "\input.txt") as f:
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
    # print("".join(polymere)) 
    for i in range(len(polymere)-1):
        newpolymere.append(polymere[i])
        newpolymere.append(rules[polymere[i]+polymere[i+1]])
    newpolymere.append(polymere[-1])
    return newpolymere

def iteratepairs(pairs, rules):
    newpairs = dict()
    for pair in pairs:
        c = rules[pair]
        pair1 = pair[0] + c
        pair2 = c + pair[1]

        count = pairs[pair]
        newpairs[pair1] = newpairs.setdefault(pair1, 0) + count
        newpairs[pair2] = newpairs.setdefault(pair2, 0) + count
    return newpairs

def getpairsinpolymere(polymere):
    pairs = dict()
    for i in range(len(polymere)-1):
        pair = polymere[i] + polymere[i+1]
        pairs[pair] = pairs.setdefault(pair, 0) + 1

    return pairs

def countletters(pairs, lastletter):
    count = dict()

    for pair in pairs:
        count[pair[0]] = count.setdefault(pair[0], 0) + pairs[pair]

    count[lastletter] += 1

    return count

iterations = 10
origpoplymere = polymere
for i in range(iterations):
    polymere = pairinsertion(polymere, rules)
    # print(Counter(polymere))

count = Counter(polymere)

countmostcommon = count.most_common()

mostminusleast = countmostcommon[0][1] - count.most_common()[-1][1]

print("Part1: most common element after " + str(iterations) + " iterations minus least common: " + str(mostminusleast))

pairs = getpairsinpolymere(origpoplymere)
iterations = 40
for i in range(iterations):
    pairs = iteratepairs(pairs, rules)

count = countletters(pairs, origpoplymere[-1])
count = Counter(count)
# print(count)

countmostcommon = count.most_common()

mostminusleast = countmostcommon[0][1] - count.most_common()[-1][1]

print("Part2: most common element after " + str(iterations) + " iterations minus least common: " + str(mostminusleast))
