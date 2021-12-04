


def getFrequency(values):
    valueCount = len(values)
    frequencyZero = [0] * len(values[0].strip())

    for value in values:
        for i in range(len(value)):
            if value[i] == '0':
                frequencyZero[i] += 1
    
    for i in range(len(frequencyZero)):
        frequencyZero[i] = frequencyZero[i]/valueCount

    return frequencyZero

lines = []

with open("F:\\programming\\github\\adventofcode\\2021\\python\\day03.txt", 'r') as f:
    lines = f.readlines()

i = 0
while (len(lines)>1):
    frequencyZero = getFrequency(lines)

