import os,re
from anytree import Node, RenderTree, render,search
import anytree
import math

from anytree.util import rightsibling

path = os.path.dirname(os.path.realpath(__file__))

nubmers = []
with open(path + "\input-example.txt") as f:
    numbers = f.read().split('\n')

def createtreefornumber(sfnumber, index, p):
    sftree = None
    left = None
    right = None
    stack = list()

    i = index
    leftread = False
    while i < len(sfnumber):
        if sfnumber[i] == '[':
            stack.append('[')
            if sftree == None:
                sftree = Node('[', parent=p)
            elif left == None and len(stack) == 2:
                left = createtreefornumber(sfnumber, i, sftree)
            elif right == None and len(stack) == 2:
                right = createtreefornumber(sfnumber, i, sftree)
            # else skip
            
        elif sfnumber[i] == ']':
            stack.pop()
            if len(stack) == 0:
                # done
                return sftree
        elif sfnumber[i] == ',':
            leftread = True
        else:
            # it's a number
            if len(stack) == 1:
                if not leftread:
                    left = Node(int(sfnumber[i]), parent=sftree)
                else:
                    right = Node(int(sfnumber[i]), parent=sftree)
        
        i += 1

def reduce(numtree):
    if explode(numtree):
        return True
    if split(numtree):
        return True
    return False

def explode(numtree:Node):
    result = False
    nodes = search.findall(numtree, filter_= lambda node: node.name=='[' and node.depth == 4)
    if len(nodes) != 0:
        result = True
        # get leftmost pair
        node = None
        for n in nodes:
            if n.children[0].is_leaf and n.children[1].is_leaf:
                node = n
                break
 
        addtoleft(node)
        addtoright(node)
        node.name = 0
        node.children = []
        
    return result

def split(numtree):
    result = False
    nodes = search.findall(numtree, filter_= lambda node: node.is_leaf and node.name > 9)
    if len(nodes) != 0:
        result = True
        node = nodes[0]

        leftval = math.floor(node.name / 2)
        rightval = math.ceil(node.name / 2)

        Node(leftval, parent=node)
        Node(rightval, parent=node)
        node.name = '['
    return result

def addtoright(node):
    # walk up til node has rightsibling, then go always left
    right = node.children[1]
    n = node
    while n != None and anytree.util.rightsibling(n) == None:
        n = n.parent
    if n != None:
        n = anytree.util.rightsibling(n)
        while not n.is_leaf:
            n = n.children[0]
        n.name += right.name

def addtoleft(node):
    # walk up til node has leftsibling, then go always right
    left = node.children[0]
    n = node
    while n != None and anytree.util.leftsibling(n) == None:
        n = n.parent
    if n != None:
        n = anytree.util.leftsibling(n)
        while not n.is_leaf:
            n = n.children[1]
        n.name += left.name

def renderflat(numtree:Node):
    n = numtree
    if n.is_leaf:
        return str(n.name)
    else:
        output = []
        output.append('[')
        output.append(renderflat(n.children[0]))
        output.append(',')
        output.append(renderflat(n.children[1]))
        output.append(']')
        return ''.join(output)

def getmagnitude(numtree:Node):
    if numtree.is_leaf:
        return numtree.name
    else:
        return 3*getmagnitude(numtree.children[0]) + 2*getmagnitude(numtree.children[1])


def add(numtree, right):
    newnode = Node("[")
    numtree.parent = newnode
    right.parent = newnode
    return newnode


def part1(numbers):
    numtree = None
    for sfnumber in numbers:
        if numtree == None:
            numtree = createtreefornumber(sfnumber, 0, None)
        else:
            right = createtreefornumber(sfnumber, 0, None)
            numtree = add(numtree, right)

        print ('====================================')
        print(renderflat(numtree))

        while reduce(numtree):
            pass
        # print(renderflat(numtree))

    print(renderflat(numtree))
    print("Part1: magnitude of snailfish homework: " + str(getmagnitude(numtree)))


def part2(numbers):
    mag = 0
    for i in range(len(numbers)):
        print("index: " + str(i))
        for j in range(i+1, len(numbers)):
            left = createtreefornumber(numbers[i],0,None)
            right = createtreefornumber(numbers[j],0,None)


            result = add(left,right)

            while reduce(result):
                pass

            m = getmagnitude(result)
            if m > mag:
                mag = m
                print("new mag : " + str(mag))

            result = add(right,left)

            while reduce(result):
                pass

            m = getmagnitude(result)
            if m > mag:
                mag = m
                print("new mag : " + str(mag))
            print(renderflat(result))

    print("Part2: max magnitude of snailfish homework: " + str(mag))




# part1(numbers)
part2(numbers)