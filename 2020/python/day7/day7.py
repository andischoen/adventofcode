import re

rulesOuterToInnerDict = {}
rulesInnerToOuterDict = {}
possibleOuterColors = set()

def addOuterColors(color):
    if color in rulesInnerToOuterDict and len(rulesInnerToOuterDict[color]) > 0:
        for outerColor in rulesInnerToOuterDict[color]:
            possibleOuterColors.add(outerColor)
            addOuterColors(outerColor)

def getNumberOfBagsContained(color):
    counter = 0
    if color in rulesOuterToInnerDict:
        for containedBag in rulesOuterToInnerDict[color]:
            counter += (1 * int(containedBag[0])) # for the bag iself
            counter += int(containedBag[0]) * getNumberOfBagsContained(containedBag[1])
        
    return counter

rules = []
with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day7\\input_01.txt", 'r') as f:
    rules = f.readlines()

innerBagMatcher = re.compile("([0-9]+) ([a-z ]+) bags*[,.]")

for rule in rules:
    ruleParts = rule.split("bags contain")
    outerBag = ruleParts[0].strip()
    innerBags = ruleParts[1]

    matches = innerBagMatcher.findall(innerBags)

    innerBagsColors = []
    if matches != None:
        for match in matches:
            color = match[1]
            innerBagsColors.append(match)

            if color not in rulesInnerToOuterDict:
                rulesInnerToOuterDict[color] = set()

            rulesInnerToOuterDict[color].add(outerBag)

    rulesOuterToInnerDict[outerBag] = innerBagsColors


color = "shiny gold"

# part 1
addOuterColors(color)
print("number of possible outer colors: " + str(len(possibleOuterColors)))

# part 2
numberOfBagsContained = getNumberOfBagsContained(color)
print("number of bags to buy " + str(numberOfBagsContained))
