import os

path = os.path.dirname(os.path.realpath(__file__))

maxAge = 8
resetAge = 6

def ageSwarm(swarm):
    ageZero = swarm[0]
    for i in range(maxAge):
        swarm[i] = swarm[i+1]
    swarm[maxAge] = ageZero
    swarm[resetAge] += ageZero

fishAges = []

with open(path + "\input.txt", "r") as f:
    fishAges = [int(num) for num in f.read().split(',')]


swarm = dict()
for i in range(maxAge+1):
    swarm[i] = 0

for age in fishAges:
    swarm[age] += 1

for i in range(80):
    ageSwarm(swarm)

print("Lanternfish in swarm after 80 days: " + str(sum(swarm.values())))

for i in range(256-80):
    ageSwarm(swarm)

print("Lanternfish in swarm after 256 days: " + str(sum(swarm.values())))
