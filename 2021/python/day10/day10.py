import os, math

path = os.path.dirname(os.path.realpath(__file__))

openingBraces = ('<', '{', '(', '[')
matches = {'<':'>', '{':'}', '(':')', '[':']'}

def calculateErrorScore(line):
    stack = []
    for c in line:
        if c in openingBraces:
            stack.append(c)
        else:
            opening = stack.pop()
            if not isMatchingBrace(opening, c):
                return getScoreForChar(c)
    
    return 0

def calculateAutocompleteScore(line):
    stack = []
    for c in line:
        if c in openingBraces:
            stack.append(c)
        else:
            opening = stack.pop()
            if not isMatchingBrace(opening, c):
                return 0
    
    return getScoreForAutocomplete(stack)

def isMatchingBrace(opening, closing):
    return matches[opening] == closing

def getScoreForChar(c):
    if c == ')': 
        return 3
    elif c == ']':
        return 57
    elif c == '}': 
        return 1197
    elif c == '>': 
        return 25137
    else:
        return None

def getScoreForAutocomplete(stack):
    autocompletesequence = []
    while len(stack) > 0:
        autocompletesequence.append(matches[stack.pop()])

    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    score = 0
    for c in autocompletesequence:
        score *= 5
        score += points[c]

    return score


lines = []
with open(path + "\input.txt") as f:
    lines = f.read().split()


syntaxerrorscore = []
for line in lines:
    syntaxerrorscore.append(calculateErrorScore(line.strip()))

print("Part1: Syntax Error Score = " + str(sum(syntaxerrorscore)))

autocompletescore = []
for line in lines:
    autocompletescore.append(calculateAutocompleteScore(line.strip()))

autocompletescore = sorted([s for s in autocompletescore if s>0])
winnerindex = math.floor(len(autocompletescore)/2)

print("Part2: Autocomplete Score = " + str(autocompletescore[winnerindex]))