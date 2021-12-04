
def markBingoCard(bingoCard, draw):
    for line in bingoCard:
        for i in range(len(line)):
            if line[i] == draw:
                line[i] = -1

def isWinner(bingoCard):
    return 0

def calculateWinner(bingoCard, draw):
    return 0



input = []

with open("C:\\python\\aoc\\adventofcode\\2021\\python\\day04\\day04.txt", 'r') as f:
    input = f.read().split('\n\n')


drawing = [int(n) for n in input[0].split(',')]
bingos = []
for i in range(1,len(input)):
    bingoCard = []
    for line in input[i].split('\n'):
        bingoCard.append([int(n) for n in line.split()])

    bingos.append(bingoCard)

for draw in drawing:
    for bingoCard in bingos:
        markBingoCard(bingoCard, draw)
        if isWinner(bingoCard):
            print(str(calculateWinner(bingoCard, draw)))
            break