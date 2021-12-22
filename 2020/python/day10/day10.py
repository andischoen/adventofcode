import time
start_time = time.time()

adapters = []
with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day10\\input_01.txt", 'r') as f:
    adapters = list(map(int, f.readlines()))

adapters.sort()

inputJoltage = 0
difference3 = 0
difference1 = 0

stretch = 0
stretches = []
for i in range(len(adapters)):
    adapter = adapters[i]
    joltageDifference = (adapter-inputJoltage)
    if joltageDifference == 1:
        difference1 += 1
        stretch += 1
    elif joltageDifference == 3:
        difference3 += 1
        if stretch > 1:
            stretches.append(stretch)
        stretch = 0
    elif joltageDifference<1 or joltageDifference>3:
        print("this should not happen")
    inputJoltage = adapter
difference3 +=1

print("1 and 3 difference count multiplied: " + str(difference1*difference3))
combinations = 1
for stretch in stretches:
    if stretch == 2:
        combinations *= 2
    elif stretch == 3:
        combinations *= 4
    elif stretch == 4:
        combinations *= 7
print("possible combinations: " + str(combinations))


print("--- %s seconds ---" % (time.time() - start_time))