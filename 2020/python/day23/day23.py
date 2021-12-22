from DoubleLinkedList import DoubleLinkedList

def makeMove(ringBuffer: DoubleLinkedList):
    # remove 3 items after current node
    removed = list()
    removed.append(ringBuffer.popNode(1))
    removed.append(ringBuffer.popNode(1))
    removed.append(ringBuffer.popNode(1))

    # find where to add
    label = selectTargetCup(ringBuffer, removed, 1000000)

    # add removed values
    ringBuffer.addIterableAfter(removed, label)

    # move currentNode
    ringBuffer.moveCurrentNode(1)

def selectTargetCup(ringBuffer: DoubleLinkedList, removed, max):
    label = ringBuffer.currentNode.value - 1
    label = label if label > 0 else max
    while label in removed:
        label -= 1
        label = label if label > 0 else max
    return label

ringBuffer = DoubleLinkedList()
# example input
#ringBuffer.addIterable([3,8,9,1,2,5,4,6,7])

# real input
ringBuffer.addIterable([9,2,5,1,7,6,8,3,4])
ringBuffer.addIterableAfter(range(10,1000001),4)

# ringBuffer.printList(all=False)
for i in range(10000000):
    if i%100000 == 0:
        print("move " + str(i))
    makeMove(ringBuffer)

ringBuffer.printList(all=False)