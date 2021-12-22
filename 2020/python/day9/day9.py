


numbers = []
offendingNumber = 0

def checkNumber(i):
    for j in range(i-25, i-1):
        for k in range (j+1, i):
            if int(numbers[j])+int(numbers[k]) == int(numbers[i]):
                return True
    return False

def checkContiguousSum(i, offendingNumber):
    global numbers
    sum = 0
    lastIndex = 0
    for j in range(i, len(numbers)):
        sum += int(numbers[j])
        if sum > offendingNumber:
            break
        if sum == offendingNumber:
            lastIndex = j
            break
    
    return lastIndex

def smallestLargestSum(i, lastIndex):
    contiguousRange = []
    for j in range(i, lastIndex+1):
        contiguousRange.append(int(numbers[j]))

    contiguousRange.sort()
    return contiguousRange[0] + contiguousRange[len(contiguousRange)-1]


with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day9\\input_01.txt", 'r') as f:
    numbers = f.readlines()


for i in range(25,len(numbers)):
    if not checkNumber(i):
        print("first number that does not satisfy: " + str(numbers[i]))
        offendingNumber = int(numbers[i])
        break

# part 2
for i in range(len(numbers)):
    lastIndex = checkContiguousSum(i, offendingNumber)
    if lastIndex>0 and lastIndex-i>1:
        sum = smallestLargestSum(i, lastIndex)
        print("sum of last and first number in contiguous range: " + str(sum))
        break