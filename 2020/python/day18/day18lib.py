def calculateLine(calc):
    stack = []
    operatorStack = []

    for token in calc:
        if token >= '0' and token <= '9':
            num = int(token)
            stack.append(num)
            if len(operatorStack) > 0 and (operatorStack[-1] == '+' or operatorStack[-1] == '*'):
                stack.append(calculate(stack.pop(), stack.pop(), operatorStack.pop()))
        elif token == '(':
            operatorStack.append(token)
        elif token == ')':
            if operatorStack.pop() == '(':
                if len(operatorStack) > 0 and (operatorStack[-1] == '+' or operatorStack[-1] == '*'):
                    stack.append(calculate(stack.pop(), stack.pop(), operatorStack.pop()))
            else:
                raise ArithmeticError('brackets not matching')
        elif token == '+' or token == '*':
            operatorStack.append(token)
    
    return stack.pop()


def calculate(left, right, op):
    if op == '+':
        return left + right
    elif op == '*':
        return left * right
    else:
        return None


def calculateLineAdvanced(calc):
    stack = []
    operatorStack = []

    for token in calc:
        if token >= '0' and token <= '9':
            num = int(token)
            stack.append(num)
            if len(operatorStack) > 0 and (operatorStack[-1] == '+'):
                stack.append(calculate(stack.pop(), stack.pop(), operatorStack.pop()))
        elif token == '(':
            operatorStack.append(token)
        elif token == ')':
            runLeftOverCalculations(operatorStack, stack)
            if operatorStack.pop() == '(':
                if len(operatorStack) > 0 and (operatorStack[-1] == '+'):
                    stack.append(calculate(stack.pop(), stack.pop(), operatorStack.pop()))
            else:
                raise ArithmeticError('brackets not matching')
        elif token == '+' or token == '*':
            operatorStack.append(token)
            
    runLeftOverCalculations(operatorStack, stack)
    return stack.pop()

def runLeftOverCalculations(operatorStack, stack):
    while len(operatorStack) > 0 and operatorStack[-1] != '(':
        stack.append(calculate(stack.pop(), stack.pop(), operatorStack.pop()))
