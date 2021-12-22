
lastMentioned = {19:[1,0], 20:[2,0], 14:[3,0], 0:[4,0], 9:[5,0], 1:[6,0]}
# lastMentioned = {0:[1,0], 3:[2,0], 6:[3,0]}
# lastMentioned = {3:[1,0], 1:[2,0], 2:[3,0]}
startingNumbers = [19,20,14,0,9,1]
# startingNumbers = [0,3,6]
# startingNumbers = [3,1,2]

# part 1
index = 6
lastNumber = 1
while index <= 2020:
    lastNumber = startingNumbers[-1]
    age = 0
    for i in range(len(startingNumbers)-2, -1, -1):
        if startingNumbers[i] == lastNumber:
            age = index-1 - i
            break
    startingNumbers.append(age)
    index += 1

print("number at 2020: " + str(lastNumber))

# part 2
index = 7
lastNumber = 1
age = 0
while index <= 30000000:
    age = lastMentioned[lastNumber][1]
    lastNumber = age
    if age in lastMentioned:
        newAge = index - lastMentioned[age][0]
        lastMentioned[age][0] = index
        lastMentioned[age][1] = newAge
    else:
        lastMentioned[age] = [index, 0]
    index += 1

print("number at 2020: " + str(age))