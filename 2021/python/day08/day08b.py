import os, re


def getmapping(alldigits):
    mapping = dict()

    find1478(alldigits, mapping)
    find235(alldigits, mapping)
    find690(alldigits, mapping)

    return mapping

def find1478(alldigits, mapping):
    for digit in alldigits:
        length = len(digit)
        if length == 2:
            mapping[digit] = 1
            mapping[1] = digit
        elif length == 4:
            mapping[digit] = 4
            mapping[4] = digit
        elif length == 3:
            mapping[digit] = 7
            mapping[7] = digit
        elif length == 7:
            mapping[digit] = 8
            mapping[8] = digit

def find235(alldigits, mapping):
    # all have 5 segments
    # 3 contains all segments from 1, but not 5 and 2
    # segments of 4 less the ones from 1 gives 2 segments that need to be in 5, but not 3 and 2
    for digit in alldigits:
        length = len(digit)
        if length == 5:
            if mapping[1][0] in digit and mapping[1][1] in digit:
                mapping[digit] = 3
                mapping[3] = digit
            elif (set(mapping[4]) - set(mapping[1])).issubset(set(digit)):
                mapping[digit] = 5
                mapping[5] = digit
            else:
                mapping[digit] = 2
                mapping[2] = digit

def find690(alldigits, mapping):
    # 9 contains all segments of 4, but 0 and 6 not
    # 8 minus the segments of 5, gives 2 segments that are only found in 0
    for digit in alldigits:
        length = len(digit)
        if length == 6:
            if set(mapping[4]).issubset(set(digit)):
                mapping[digit] = 9
                mapping[9] = digit
            elif (set(mapping[8]) - set(mapping[5])).issubset(set(digit)):
                mapping[digit] = 0
                mapping[0] = digit
            else:
                mapping[digit] = 6
                mapping[6] = digit


def decodeline(line):
    parts = line.split(" | ")
    alldigits = ["".join(sorted(n)) for n in parts[0].split()]
    outputdigits = ["".join(sorted(n)) for n in parts[1].split()]

    mapping = getmapping(alldigits)

    output = ""
    for digit in outputdigits:
        output = output + str(mapping[digit])
    return int(output)


path = os.path.dirname(os.path.realpath(__file__))

lines = []
with open(path + "\input.txt") as f:
    lines = f.readlines()

outputNumbers = []
for line in lines:
    outputNumbers.append(decodeline(line))


print("Sum of output: " + str(sum(outputNumbers)))