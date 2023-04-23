class Node:
    def __init__(self, val, next = None):#used to create the node
        self.val = val
        self.next = next
        

"""
time complexity: O(n) loops through the nodes once
space complexity: O(n) stores all the non dupes in the list temp
time: 20 minutes

"""

def DedupSortedList(head):
    temp = []
    
    
    curr = head
    prev = None
    
    while curr != None:
        if curr.val in temp:
            prev.next = curr.next
            curr = curr.next
        
        elif curr.val not in temp:
            temp.append(curr.val)
            prev = curr
            curr = curr.next
            
def printe(head):#used to print to see if I am doing ti correctly
    if head is None:
        print("Empty")
        return
        
    itr = head
    temp = ''
    while itr:
        temp += str(itr.val) + '-->'
        itr = itr.next
    print(temp)



n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(4)
n6 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
head_n = n1
printe(head_n)
DedupSortedList(head_n)
printe(head_n)
        
