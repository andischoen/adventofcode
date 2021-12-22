def getGroupCommonAnswerCount(group):
    forms = group.split("\n")

    listOfSets = []
    for i in range(len(forms)):
        listOfSets.append(set())
        for answer in forms[i]:
            listOfSets[i].add(answer)
    
    commonAnswers = listOfSets[0]
    for answerSet in listOfSets:
        commonAnswers = commonAnswers.intersection(answerSet)
    
    return len(commonAnswers)

def getGroupAnswersCount(group):
    forms = group.split("\n")

    setOfAnswers = set()
    for form in forms:
        for answer in form:
            setOfAnswers.add(answer)
    
    return len(setOfAnswers)