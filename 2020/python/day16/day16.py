from os.path import split
import re


inputLines = []
fieldDefinitions = dict()
invalidFields = []
validTickets = []
finalRules = dict()
myticketFields = []

def checkFieldAgainsRule(value, rule):
    rule1 = rule[0]
    rule2 = rule[1]

    return (value >= rule1[0] and value <= rule1[1]) or (value >= rule2[0] and value <= rule2[1])

def evaluateTicket(ticketFields):
    for field in ticketFields:
        value = int(field)
        if not (any(checkFieldAgainsRule(value, rule) for rule in fieldDefinitions.values())):
            invalidFields.append(value)
            return False
    return True
        
def findFieldIndices():
    global validTickets

    for i in range(len(validTickets[0])):
        candidateRules = list(fieldDefinitions.values())

        for ticket in validTickets:
            field = ticket[i]
            for rule in fieldDefinitions.values():
                if rule in candidateRules:
                    if not checkFieldAgainsRule(int(field), rule):
                        candidateRules.remove(rule)

        for r in candidateRules: 
            r[2].append(i)

def reduceFieldIndices():
    

    r = next((x for x in fieldDefinitions if len(fieldDefinitions[x][2]) == 1), None)
    while len(finalRules) < 20:
        index = fieldDefinitions[r][2][0]
        finalRules[r] = index
        fieldDefinitions.pop(r)
        for r in fieldDefinitions.values():
            r[2].remove(index)
        r = next((x for x in fieldDefinitions if len(fieldDefinitions[x][2]) == 1), None)
        


with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day16\\input_01.txt", 'r') as f:
    inputLines = f.readlines()

readRules = True
readMyTicket = True
rulesRegEx = re.compile("(.*): ([0-9]+)\-([0-9]+) or ([0-9]+)\-([0-9]+)")
for line in inputLines:
    if readRules:
        if line.startswith("your ticket:"):
            readRules = False
        else:
            match = rulesRegEx.match(line)
            if match != None:
                fieldDefinitions[match[1]] = [(int(match[2]), int(match[3])), (int(match[4]), int(match[5])), list()]
    elif readMyTicket:
        if line.startswith("nearby tickets:"):
            readMyTicket = False
        elif len(line) > 3:
            myticketFields = line.split(",")
    else:
        ticketFields = line.split(",")
        if evaluateTicket(ticketFields):
            validTickets.append(ticketFields)



sum = sum(invalidFields)
print("Sum of invalid fields: " + str(sum))

findFieldIndices()
reduceFieldIndices()
print(fieldDefinitions)
print(finalRules)

result = 1
for key, value in finalRules.items():
    if key.startswith("departure"):
        result *= int(myticketFields[value])

print("Result of part 2: " + str(result))