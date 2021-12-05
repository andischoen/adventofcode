
def markBingoCard(bingoCard, draw):
    for line in bingoCard:
        for i in range(len(line)):
            if line[i] == draw:
                line[i] = -1

def isWinner(bingoCard):
    for line in bingoCard:
        if sum(line) == -5:
            return True
    if -5 in [sum(num) for num in zip(*bingoCard)]:
        return True

def calculateWinner(bingoCard, draw):
    total = 0
    for line in bingoCard:
        total += sum([n for n in line if n >= 0])
    
    return total*draw



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

winners = []
for draw in drawing:
    i = 0
    for bingoCard in bingos:
        i += 1
        if i not in winners:
            markBingoCard(bingoCard, draw)
            if isWinner(bingoCard):
                winners.append(i)
                print(str(i) + " " + str(calculateWinner(bingoCard, draw)))