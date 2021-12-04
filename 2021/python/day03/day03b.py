


def getFrequency(values):
    valueCount = len(values)
    frequencyZero = [0] * len(values[0].strip())

    for value in values:
        for i in range(len(value.strip())):
            if value[i] == '0':
                frequencyZero[i] += 1
    
    for i in range(len(frequencyZero)):
        frequencyZero[i] = frequencyZero[i]/valueCount

    return frequencyZero

lines = []

with open("C:\\python\\aoc\\adventofcode\\2021\\python\\day03\\day03.txt", 'r') as f:
    lines = f.readlines()

i = 0
oxygen = [num for num in lines]
co2 = [num for num in lines]
while (len(oxygen)>1):
    frequencyZero = getFrequency(oxygen)
    print("zero frequency at pos " + str(i) + " : " + str(frequencyZero[i]))
    if frequencyZero[i] <= 0.5:
        oxygen = [num for num in oxygen if num[i] == '1']
    else:
        oxygen = [num for num in oxygen if num[i] == '0']
    i += 1

print("---------------------------")
i = 0
while (len(co2)>1):
    frequencyZero = getFrequency(co2)
    print("zero frequency at pos " + str(i) + " : " + str(frequencyZero[i]))
    if frequencyZero[i] <= 0.5:
        co2 = [num for num in co2 if num[i] == '0']
    else:
        co2 = [num for num in co2 if num[i] == '1']
    i += 1

oxyInt = int(oxygen[0],2)
co2Int = int(co2[0],2)
print("oxygen: " + str(oxygen[0]) + " -> " + str(oxyInt))
print("co2: " + str(co2[0]) + " -> " + str(co2Int))
print("together: " + str(oxyInt*co2Int))