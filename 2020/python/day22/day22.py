
player1Stack = list()
player2Stack = list()
infiniteLoopMax = 2000

def readInput():
    global player1Stack
    global player2Stack
    
    player1Stack = list()
    player2Stack = list()

    content = ""

    with open("C:\\data\\dotnet_projects\\adventofcode\\python\\day22\\input_01.txt", 'r') as f:
        content = f.read()
    
    players = content.split('\n\n')

    player1Stack = list(map(int, players[0].split('\n')[:0:-1]))
    player2Stack = list(map(int, players[1].split('\n')[:0:-1]))

def invokeGameLoop():
    loop = not playRound()
    while loop:
        loop = not playRound()

def playRound():
    global player1Stack
    global player2Stack

    card1 = player1Stack.pop()
    card2 = player2Stack.pop()

    if card1 > card2: 
        player1Stack.insert(0, card1)
        player1Stack.insert(0, card2)
    else:        
        player2Stack.insert(0, card2)
        player2Stack.insert(0, card1)
    
    return len(player1Stack) == 0 or len(player2Stack) == 0


def playRecursiveGame(stack1, stack2):
    loopCounter = 0
    winner = playRecursiveRound(stack1, stack2)
    while winner == 0:
        loopCounter += 1
        if loopCounter > infiniteLoopMax:
            print("infinite loop prevention now!")
            return 1
        winner = playRecursiveRound(stack1, stack2)

    return winner
        

def playRecursiveRound(stack1, stack2):
    card1 = stack1.pop()
    card2 = stack2.pop()

    winner = 0
    # determine winner
    if card1 <= len(stack1) and card2 <= len(stack2):
        #recursive round
        print("recursive round with:")
        print(stack1[-card1:])
        print(stack2[-card2:])
        winner = playRecursiveGame(stack1[-card1:], stack2[-card2:])
    else:
        # normal round
        winner = 1 if card1 > card2 else 2

    # enqueue cards according to winner
    if winner == 1:
        stack1.insert(0, card1)
        stack1.insert(0, card2)
    else:
        stack2.insert(0, card2)
        stack2.insert(0, card1)
    
    overallWinner = 0
    if len(stack1) == 0:
        overallWinner = 2
    elif len(stack2) == 0:
        overallWinner = 1

    # print(stack1)
    # print(stack2)
    # print("----------------------------")

    return overallWinner

def scoreGame():
    global player1Stack
    global player2Stack

    stack = player1Stack if len(player1Stack) > 0 else player2Stack

    result = 0
    multiplicator = 1
    for i in stack:
        result += multiplicator*i
        multiplicator += 1

    return result

readInput()

# part1
invokeGameLoop()
score = scoreGame()
print("the final score is: " + str(score))

# part2
readInput()
winner = playRecursiveGame(player1Stack, player2Stack)
score = scoreGame()
print("the final score of the recursive game is: " + str(score))