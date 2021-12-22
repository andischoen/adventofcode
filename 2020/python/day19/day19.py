
rules = dict()
messages = []

def readInput():
    
    inputLines = []
    with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day19\\input_01_2.txt", 'r') as f:
        inputLines = f.readlines()

    readRules = True
    for line in inputLines:
        if line.strip() == "":
            readRules = False
        elif readRules:
            rule = line.split(":")
            ruleNum = int(rule[0])
            ruleDef = rule[1].strip()

            if ruleDef.startswith('"'):
                rules[ruleNum] = ruleDef[1]
            else:
                ruleDef = ruleDef.split(" ")

                sequence = []
                rules[ruleNum] = []
                for token in ruleDef:
                    if token != '|':
                        sequence.append(int(token))
                    else:
                        rules[ruleNum].append(sequence)
                        sequence = []
                rules[ruleNum].append(sequence)
        else:
            messages.append(line.strip())

def applyRule(testInput, ruleId):
    global rules

    rule = rules[ruleId]

    if type(rule) == list:
        
        index = testInput[1]

        for option in rule:
            result = True
            testInput[1] = index #reset index!!
            for item in option:
                result = applyRule(testInput, item)
                if not result:
                    #shortcut evaluation
                    break
            if result:
                #shortcut evaluation
                return result
        return False

    else:
        index = testInput[1]
        text = testInput[0]

        if index >= len(text):
            return False

        result = text[index] == rule
        testInput[1] = index + 1
        return result
        


readInput()
count = 0
for message in messages:
    testInput = [message, 0]
    if applyRule(testInput, 0) and testInput[1] == len(message):
        count += 1

# part 2:
# I modified rules 8 and 11 - in the end for those rules it's
# 8: 42+ (rule number 42 one or multiple times)
# 11: 42*x 31*x (rule 42 one or multiple times followed by 31 the SAME number of times)
# so i tried: rule 8 with 42 42 and 42 42 42 and so on
# equally for 11
# and then combinations of both
# in the end I summed up the matching messages to come to the number
# 2x 8 # of matchin rules: 49
# 3x 8 # of matchin rules: 24
# 4x 8 # of matchin rules: 13
# 5x 8 # of matchin rules: 8
# 2x 11 # of matchin rules: 24
# 3x 11 # of matchin rules: 6
# 4x 11 # of matchin rules: 5
# 2x 8 2x 11 # of matchin rules: 14
# 3x 8 2x 11 # of matchin rules: 6
# 2x 8 3x 11 # of matchin rules: 5
# 3x 8 3x 11 # of matchin rules: 2

print("# of matchin rules: " + str(count))

