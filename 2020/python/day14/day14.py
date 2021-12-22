import re

mem = dict()
mem2 = dict()
mask = ""
memoryRegex = re.compile("mem\[([0-9]*)\] = ([0-9]*)")

def getMaskedInt(number, mask):
    binValue = "{:0>36b}".format(number)
    maskedValue = ""
    for i in range(len(mask)):
        if mask[i] == 'X':
            maskedValue += binValue[i]
        else:
            maskedValue += mask[i]

    return int(maskedValue, 2)


def getAddress(memId, mask):
    binAddress = "{:0>36b}".format(memId)
    resultAddress = ""
    for i in range(len(mask)):
        if mask[i] == 'X':
            resultAddress += 'X'
        elif mask[i] == '0':
            resultAddress += binAddress[i]
        else:
            resultAddress += '1'
    
    return resultAddress


def writeAddress(memId, mask, value):
    address = getAddress(memId, mask)
    possibleAddresses = []
    for c in address:
        if c == 'X':
            if len(possibleAddresses) == 0:
                possibleAddresses.append('0')
                possibleAddresses.append('1')
            else: 
                for i in range(len(possibleAddresses)):
                    a = possibleAddresses[i]
                    possibleAddresses[i] = a + '1'
                    possibleAddresses.append(a + '0')
        else:
            if len(possibleAddresses) == 0:
                possibleAddresses.append(c)
            else:
                for i in range(len(possibleAddresses)):
                    a = possibleAddresses[i]
                    possibleAddresses[i] = a + c
    
    for a in possibleAddresses:
        mem2[int(a,2)] = value


inputLines = []
with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day14\\input_01.txt", 'r') as f:
    inputLines = f.readlines()

for line in inputLines:
    if line.startswith("mask"):
        mask = line.split()[2]
    else:
        match = memoryRegex.match(line)
        memIndex = int(match[1])
        number = int(match[2])

        # part 1
        maskedNum = getMaskedInt(number, mask)
        mem[memIndex] = maskedNum

        # part 2
        writeAddress(memIndex, mask, number)


# part 1
sum = 0
for val in mem.values():
    sum+=val


print("Sum of memory values: " + str(sum))

# part 2    
sum = 0
for val in mem2.values():
    sum+=val

print("Sum of memory values: " + str(sum))