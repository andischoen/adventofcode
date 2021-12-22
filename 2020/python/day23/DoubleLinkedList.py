from Node import Node

class DoubleLinkedList:

    def __init__(self):
        self.currentNode = None
        self.labelDict = dict()

    def addAfterCurrentNode(self, value):
        self.addAfterNode(self.currentNode, value)

    def addAfterNode(self, node, value):
        if self.currentNode == None:
            self.currentNode = Node(value)
            self.labelDict[value] = self.currentNode
            self.currentNode.next = self.currentNode
            self.currentNode.last = self.currentNode
        else:
            insertNode = Node(value)
            self.labelDict[value] = insertNode
            nextNode = node.next

            node.next = insertNode
            insertNode.last = node
            insertNode.next = nextNode

            nextNode.last = insertNode

    def addIterable(self, iterable):
        for it in iterable:
            self.addAfterCurrentNode(it)
            self.moveCurrentNode(1)

        self.moveCurrentNode(1)

    def addIterableAfter(self, iterable, label):
        node = self.labelDict[label]
        
        for it in iterable:
            self.addAfterNode(node, it)
            node = node.next


    def moveCurrentNode(self, by):
        for i in range(by):
            self.currentNode = self.currentNode.next
    

    def popNode(self, offset):
        node = self.currentNode
        
        # only one node left
        if self.currentNode.next == self.currentNode:
            self.labelDict.pop(self.currentNode.value)
            self.currentNode = None
            return node.value

        for i in range(offset):
            node = self.currentNode.next
        
        if node == self.currentNode:
            self.currentNode = self.currentNode.next

        node.last.next = node.next
        node.next.last = node.last
        self.labelDict.pop(node.value)

        return node.value

    def printList(self,all=True):
        node = self.labelDict[1]
        
        printNode = node.next
        result = ""
        if all:
            while printNode != node:
                result += str(printNode.value)
                printNode = printNode.next
        else:
            for i in range(15):
                printNode = printNode.last
            for i in range(30):
                result += str(printNode.value) + " "
                printNode = printNode.next
        
        print(result)

    def __str__(self) -> str:
        resultStr = "(" + str(self.currentNode.value) + ")"
        node = self.currentNode.next
        while node != self.currentNode:
            resultStr += " " + str(node.value)
            node = node.next

        return resultStr