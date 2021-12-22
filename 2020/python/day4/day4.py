import re

requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
possibleEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkByr(value):
    if len(value) != 4:
        return False
    return isNumberInRange(value, 1920, 2002)

def checkIyr(value):
    if len(value) != 4:
        return False
    return isNumberInRange(value, 2010, 2020)

def isNumberInRange(number, low, high):
    intValue = int(number)
    return intValue >= low and intValue <= high

def checkHgt(value):
    match = re.match("^([0-9]+)(in|cm)$", value)
    if match != None:
        if match.group(2) == "in":
            return isNumberInRange(match.group(1), 59, 76)
        elif match.group(2) == "cm":
            return isNumberInRange(match.group(1), 150, 193)

    return False

def checkEyr(value):
    if len(value) != 4:
        return False
    return isNumberInRange(value, 2020, 2030)

def checkHcl(value):
    match = re.match("^#[0-9a-f]{6}$", value)
    return match != None

def checkEcl(value):
    return value in possibleEyeColors

def checkPid(value):
    match = re.match("^[0-9]{9}$", value)
    return match != None


def evalPassport(passport):
    elements = re.split("\\s+", passport)

    valid = True
    for field in requiredFields:
        valid = valid and any(element.startswith(field) for element in elements)

    return valid

def evalPassport2(passport):
    elements = re.split("\\s+", passport)

    elementDictionary = {}
    for element in elements:
        parts = element.split(":")
        elementDictionary[parts[0]] = parts[1]

    valid = True
    valid = valid and "byr" in elementDictionary and checkByr(elementDictionary["byr"])
    valid = valid and "iyr" in elementDictionary and checkIyr(elementDictionary["iyr"])
    valid = valid and "eyr" in elementDictionary and checkEyr(elementDictionary["eyr"])
    valid = valid and "hgt" in elementDictionary and checkHgt(elementDictionary["hgt"])
    valid = valid and "hcl" in elementDictionary and checkHcl(elementDictionary["hcl"])
    valid = valid and "ecl" in elementDictionary and checkEcl(elementDictionary["ecl"])
    valid = valid and "pid" in elementDictionary and checkPid(elementDictionary["pid"])

    return valid

content = ""
with open("input_01.txt", 'r') as f:
    content = f.read()

passports = content.split("\n\n")

passportCounter = 0
for passport in passports:
    if evalPassport2(passport):
        passportCounter += 1

print ("valid passports = " + str(passportCounter))