import elf_code_lib as lib

instructions = []

with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day8\\input_01.txt", 'r') as f:
    instructions = f.readlines()

lib.executeWithLoopDetection(instructions)
accumulator = lib.getAccumulatorValue()

print("accumulator before endless loop: " + str(accumulator))

# part 2
for i in range(len(instructions)):
    keep = instructions[i]
    if instructions[i].startswith("nop"):
        instructions[i] = instructions[i].replace("nop", "jmp")
    elif instructions[i].startswith("jmp"):
        instructions[i] = instructions[i].replace("jmp", "nop")
    else:
        continue

    if lib.executeWithLoopDetection(instructions):
        accumulator = lib.getAccumulatorValue()
        print("accumulator with corrected code: " + str(accumulator))
    else:
        instructions[i] = keep