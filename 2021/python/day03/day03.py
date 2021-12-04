lines = []

with open("F:\\programming\\github\\adventofcode\\2021\\python\\day03.txt", 'r') as f:
    lines = f.readlines()


gamma = ''
epsilon = ''

for c in range(len(lines[0].strip())):
    zeroCounter = 0
    for line in lines:
        if line[c] == '0':
            zeroCounter += 1
    
    if zeroCounter > 500:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'


print(int(gamma,2))
print(int(epsilon,2))

powerConsumption = int(gamma,2)*(int(epsilon,2))

print(powerConsumption)