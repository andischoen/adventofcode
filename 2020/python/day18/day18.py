import day18lib as lib

calculations = []

def readInput():
    global calculations

    inputLines = []
    with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day18\\input_01.txt", 'r') as f:
        inputLines = f.readlines()

    calculations = list(map(lambda s: list(filter(lambda c: c != ' ' and c != '\n', list(s))), inputLines))

def calculateResults():
    
    sum = 0
    for calc in calculations:
        sum += lib.calculateLine(calc)

    return sum

def calculateResults2():
    
    sum = 0
    for calc in calculations:
        sum += lib.calculateLineAdvanced(calc)

    return sum




readInput()
sum = calculateResults()
print("homework sum: " + str(sum))
# part 2
sum = calculateResults2()
print("homework sum2: " + str(sum))