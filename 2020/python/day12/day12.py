import day12lib as lib

instructions = []


filepath = "C:\\data\\dotnet_projects\\adventofcode\\python\\day12\\input_01.txt"
#filepath = "C:\\data\\dotnet_projects\\adventofcode\\python\\day12\\input_02.txt"
with open(filepath, 'r') as f:
    instructions = f.readlines()

# for instruction in instructions:
#     lib.processInstruction(instruction)

# part 2
for instruction in instructions:
    lib.processInstruction2(instruction)

print("east: " + str(lib.east) + " south: " + str(lib.south))
print("manhattan distance = " + str(lib.getManhattanDistance()))