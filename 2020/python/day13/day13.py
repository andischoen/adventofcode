import math
from functools import reduce

inputLines = []

def getEarliestAfter(earliestDepartureTime, cadence):
    # 36, 5 -> 36/5 = 7,.. -> ceil = 8 -> 8*5 = 40 -> 4min diff
    iterations = math.ceil(earliestDepartureTime/cadence)
    return (cadence*iterations)

with open("F:\\programming\\github\\adventofcode\\python\\day13\\input_01.txt", 'r') as f:
    inputLines = f.readlines()

earliestDepartureTime = int(inputLines[0])
busIds = inputLines[1].split(',')


def part1():
    earliestBusId = 0
    earliestBusDeparture = 0
    for busId in busIds:
        if busId != 'x':
            cadence = int(busId)
            possibleDeparture = getEarliestAfter(earliestDepartureTime, cadence)
            if earliestBusDeparture == 0 or possibleDeparture < earliestBusDeparture:
                earliestBusId = cadence
                earliestBusDeparture = possibleDeparture

    waitingTime = earliestBusDeparture-earliestDepartureTime
    print("the earliest id*waitingtiem: " + str(waitingTime*earliestBusId))


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def part2():
    buses = []
    offsets = []

    offset = 0

    for busId in busIds:
        if busId != 'x':
            cadence = int(busId)
            buses.append(cadence)
            offsets.append(cadence - offset)
        offset += 1
    
    offsets[0] = 0
    print(buses)
    print(offsets)

    timestamp = chinese_remainder(buses, offsets)

    print(str(timestamp))

    
    

part1()
part2()