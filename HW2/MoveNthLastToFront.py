class Node:
    def __init__(self, val, next = None):#used to create the node
        self.val = val
        self.next = next

"""
time complexity: O(n), because we are looping through the Nodes once
space complexity: O(1), the space is constant and not changing
time spent: 25 minutes
approach: I looped through the Linked List and counted how many nodes there are,
then I used this to find the Node location(the one I need to move to the front).
then I looped again until I found that number, once I found it I created a tempory Node for the Node in that location.
Then I deleted that Node from the linked list, broke out of the loop and made this Node the head and connected the rest of the Linked list
with this new head.

"""


def MoveNthLastToFront(head, move):
    counter = 0
    current = head
    
    while current.next != None:
        counter +=1
        current = current.next
    counter = counter - (move-1)#node I want to move to the front
    
    tempHead = head
    tempCounter = 0
    #tempCounter = 0
    
    temp_Node = None
    
    while tempHead.next != None:
        tempCounter +=1
        
        if tempCounter == counter:
            temp_Node = tempHead.next
            tempHead.next = tempHead.next.next
            break
            
        tempHead = tempHead.next
    
    
    
    if temp_Node != None:
        temp_Node.next = head
    
    return temp_Node

def printe(head):#used to print to see if I am doing ti correctly
    #print("hello")
    if head is None:
        print("Empty")
        return
        
    itr = head
    temp = ''
    while itr:
        temp += str(itr.val) + '-->'
        itr = itr.next
    temp += "none"
    print(temp)

"""
def test_case_1():
    n5 = Node(5)
    n4 = Node(4, n5)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    printe(n1)
    head = MoveNthLastToFront(n1, 2)
    printe(head)

def test_case_2():
    n9 = Node(19)
    n8 = Node(6,n9)
    n7 = Node(11,n8)
    n6 = Node(9,n7)
    n5 = Node(20,n6)
    n4 = Node(7,n5)
    n3 = Node(8,n4)
    n2 = Node(2,n3)
    n1 = Node(15,n2)
    printe(n1)
    head = MoveNthLastToFront(n1, 2)
    printe(head)

def test_case_3():
    n9 = Node(19)
    n8 = Node(6,n9)
    n7 = Node(11,n8)
    n6 = Node(9,n7)
    n5 = Node(20,n6)
    n4 = Node(7,n5)
    n3 = Node(8,n4)
    n2 = Node(2,n3)
    n1 = Node(15,n2)
    printe(n1)
    head = MoveNthLastToFront(n1, 7)
    printe(head)


#test_case_1()
#test_case_2()
test_case_3()
"""

