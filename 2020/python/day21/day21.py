import re

foods = []
allergenesToIngredients = dict()
ingredientsToAllergenes = dict()
noneAllergicIngredients = []

def readInput():
    global foods
    global allergenesToIngredients
    global ingredientsToAllergenes

    lines = []

    with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day21\\input_01.txt", 'r') as f:
        lines = f.readlines()

    regex = re.compile("(.*) \(contains (.*)\)")
    for line in lines:
        matches = regex.match(line)
        ingredients = matches[1].split(' ')
        allergenes = matches[2].split(', ')

        foods.append(ingredients)
        for allergene in allergenes:
            if allergene in allergenesToIngredients:
                allergenesToIngredients[allergene] = allergenesToIngredients[allergene] & set(ingredients)
            else:
                allergenesToIngredients[allergene] = set(ingredients)
        for ingredient in ingredients:
            ingredientsToAllergenes[ingredient] = None

def singleOutAllergenes():
    global allergenesToIngredients

    tempDict = dict()

    a = next(x for x in allergenesToIngredients if len(allergenesToIngredients[x]) == 1)
    tempDict[a] = allergenesToIngredients[a]
    allergenesToIngredients.pop(a)
    while len(allergenesToIngredients) > 0:
        ingredient = next(iter(tempDict[a]))        
        for ingredients in allergenesToIngredients.values():
            if ingredient in ingredients:
                ingredients.remove(ingredient)
        
        a = next(x for x in allergenesToIngredients if len(allergenesToIngredients[x]) == 1)
        tempDict[a] = allergenesToIngredients[a]
        allergenesToIngredients.pop(a)
    
    allergenesToIngredients = tempDict

def updateIngredients():
    global allergenesToIngredients
    global ingredientsToAllergenes
    global noneAllergicIngredients

    for allergene, ingredientSet in allergenesToIngredients.items():
        ingredient = next(iter(ingredientSet))
        ingredientsToAllergenes[ingredient] = allergene
    
    noneAllergicIngredients = [i for i in ingredientsToAllergenes if ingredientsToAllergenes[i] == None]

def getNumOfNonAllergicAppearances():
    global foods
    global noneAllergicIngredients

    count = 0
    for food in foods:
        for ingredient in food:
            if(ingredient in noneAllergicIngredients):
                count += 1
    
    return count



readInput()
singleOutAllergenes()
updateIngredients()
count = getNumOfNonAllergicAppearances()
print("Number of ingredients that are none-allergic in all foods: " + str(count))

print(sorted(allergenesToIngredients.items()))
canonicalDangerousIngredientList = []
for allergene,ingredient in sorted(allergenesToIngredients.items()):
    canonicalDangerousIngredientList.append(next(iter(ingredient)))

print(','.join(canonicalDangerousIngredientList))
