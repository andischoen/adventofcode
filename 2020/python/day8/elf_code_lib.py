
accumulator = 0


def executeWithLoopDetection(instructions):
    pointer = 0
    global accumulator
    accumulator = 0
    executedInstructions = []

    while pointer not in executedInstructions:
        instruction = instructions[pointer]
        parts = instruction.split(" ")
        operation = parts[0]
        operand = parts[1]

        executedInstructions.append(pointer)
        instructionIncrement = 1

        if operation == "acc":
            accumulator += int(operand)
        elif operation == "jmp":
            instructionIncrement = int(operand)

        pointer += instructionIncrement
        if pointer == len(instructions):
            return True # program exited normally

    return False # loop detected

def getAccumulatorValue():
    return accumulator