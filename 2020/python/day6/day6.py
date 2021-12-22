import day6lib as lib


content = ""

with open("F:\\programming\\github\\adventofcode\\python\\day6\\input_01.txt", 'r') as f:
    content = f.read()

groups = content.split("\n\n")

sumOfAnswers = 0
for group in groups:
    # part1: 
    # sumOfAnswers += getGroupAnswersCount(group)

    # part2: 
    sumOfAnswers += lib.getGroupCommonAnswerCount(group)

print("sum of answers: " + str(sumOfAnswers))