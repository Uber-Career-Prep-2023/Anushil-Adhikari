class Node:
    def __init__(self, val, next = None):#used to create the node
        self.val = val
        self.next = next

"""
time complexity: O(n), because we looped through the linked list once
space complexity: O(n), because we stored the id of the Nodes in a dictt
time spent: 30 minutes
approach: I looped through the Linked List and checked if the ids are unique, if they are I added them to the dictt.
However, if they are not unique, I changed its next Node to None because I know that it is now looping. 
"""


def DisconnectCycle(head):
    dictt = {}
    
    current = head
    
    counter =0
    
    dictt[id(current)] = 1
    
    while current.next != None:
        
        if id(current.next) not in dictt:
            #dictt.append(id(current))
            dictt[id(current.next)] = 1
            current = current.next
            
        elif id(current.next) in dictt:
            current.next = None
            break
        print(dictt)
        
    return current

def printe(head):#used to print to see if I am doing it correctly
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
    n6 = Node(2)
    n5 = Node(5, n6)
    n4 = Node(4, n5)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    n6.next = n2
    #printe(n1)
    DisconnectCycle(n1)
    printe(n1)
    
def test_case_2():
    n6 = Node(4)
    n5 = Node(11, n6)
    n4 = Node(9, n5)
    n3 = Node(12, n4)
    n2 = Node(18, n3)
    n1 = Node(10, n2)
    n6.next = n3
    #printe(n1)
    DisconnectCycle(n1)
    printe(n1)
    
def test_case_3():
    n6 = Node(4)
    n5 = Node(11, n6)
    n4 = Node(9, n5)
    n3 = Node(12, n4)
    n2 = Node(18, n3)
    n1 = Node(10, n2)
    n6.next = n6
    #printe(n1)
    DisconnectCycle(n1)
    printe(n1)
    
test_case_1()
test_case_2()
test_case_3()
"""