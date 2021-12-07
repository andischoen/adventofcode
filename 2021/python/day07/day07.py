import os

def getDefaultDistance(pos, target):
    return abs(pos-target)

def getCrabDistance(pos, target):
    n = abs(pos-target)
    return (n*(n+1))/2

def getMinFuel(getDistance):
    fuelMin = None
    for i in range(2000):
        fuel = 0
        for pos in crabs.keys():

            fuel += (getDistance(pos, i) * crabs[pos])
        
        if fuelMin == None or fuelMin > fuel:
            fuelMin = fuel
    
    return fuelMin

path = os.path.dirname(os.path.realpath(__file__))

positions = []
with open(path + "\input.txt") as f:
    positions = [int(pos) for pos in f.read().split(',')]

# positions = sorted(positions)

crabs = dict()
for pos in positions:
    crabs[pos] = crabs.setdefault(pos,0)+1



print("Minimal Fuel: " + str(getMinFuel(getDefaultDistance)))

print("Minimal Fuel (part2): " + str(getMinFuel(getCrabDistance)))