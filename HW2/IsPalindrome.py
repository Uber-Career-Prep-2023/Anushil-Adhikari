class Node:
    def __init__(self,val, next = None, prev = None):#used to create the nodes
        self.val = val
        self.next = next
        self.prev = prev

"""
time complexity: O(n), because we looped through the linked list once
space complexity: O(1), because the space we use is constant
time spent: 20 minutes
approach: I looped all the way to the end of the Linked List (last)
then while first.next is not equal to last, I would check if first.val matches last.val, if it doesnt I returned false
If they passed all the way I returned true

"""



def IsPalindrome(head):
    
    last = head
    first = head
    while last.next != None:
        last.prev = last
        last = last.next
        
        
    while (first.next !=last):
        if first.val !=last.val:
            return False
        
        first = first.next
        last = last.prev
    
    return True

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
    #temp += "none"
    print(temp)
    
"""  
def test_case_1():#returns true
    n5 = Node(1)
    n4 = Node(2, n5)
    n3 = Node(3, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    n5.prev = n4
    n4.prev = n3
    n3.prev = n2
    n2.prev = n1
    printe(n1)
    print(IsPalindrome(n1))
    
def test_case_2():#returns true
    n5 = Node(9)
    n4 = Node(2, n5)
    n3 = Node(4, n4)
    n2 = Node(2, n3)
    n1 = Node(9, n2)
    n5.prev = n4
    n4.prev = n3
    n3.prev = n2
    n2.prev = n1
    printe(n1)
    print(IsPalindrome(n1))
    
    
def test_case_3():#returns false
    n5 = Node(9)
    n4 = Node(2, n5)
    n3 = Node(4, n4)
    n2 = Node(12, n3)
    n1 = Node(9, n2)
    n5.prev = n4
    n4.prev = n3
    n3.prev = n2
    n2.prev = n1
    printe(n1)
    print(IsPalindrome(n1))
    
test_case_1()
test_case_2()
test_case_3()
"""