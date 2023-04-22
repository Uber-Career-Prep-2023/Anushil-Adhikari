"""
time: 45 minutes
was tough but learning the basic data structure and doing Question 1 helped a lot



"""


class Node:
    def __init__(self,val, next = None, prev = None):#used to create the nodes
        self.val = val
        self.next = next
        self.prev = prev
        
        

class DoubleLinkedList:
    def __init__(self):#used to create the DoubleLinkedList object
        self.head = None
        self.tail = None
        
    def insertAtFront(self, val):#change the val to the head and change the rest of the linked list to it next
        #O(1) complexity for time and space
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None
            self.head.prev = newNode
            
        return self.head
        
    def insertAtBack(self, val):#loop until we reach the end and add the value there
        newNode = Node(val)
        #O(n) complexity for time: We loop through the entire list once, where n is the number of elements in the list.
        #and O(1) for space
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        temp = self.head
        pre = None
        while temp.next is not None:
            temp = temp.next
            pre = temp
            
            
        temp.next = newNode
        newNode.prev = temp
        return
    
    def insertAfter(self, val, loc):#once you find the value loc, put the value after this loc value
        #time complexity: O(n): We loop through the entire list once, where n is the number of elements in the list.
        #space complexity: O(1)
        newNode = Node(val)
        if self.head is None:
            return
        temp = self.head
        pre = None
        #print("temp")
        #print(temp.val)
        
        while temp != loc:
            pre = temp.prev
            temp = temp.next
            
            
        
        if temp == loc:
            if loc.next != None:
                newNode.next = loc.next
                newNode.prev = loc
                
            temp.next = newNode
            
            
            
    def deleteFront(self):#change the head to the next value
        #time complexity: O(1): We loop through the entire list once, where n is the number of elements in the list.
        #space complexity: O(1)
        temp = self.head
        if temp != None:
            self.head = temp.next
            self.head.prev = None
            
        return self.head
    
    
    def deleteBack(self):#loop to the back and change it to None
        #time complexity: O(n): We loop through the entire list once, where n is the number of elements in the list.
        #space complexity: O(1)
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        
        last = None
        now = self.head
        pre = None
        
        while now.next != None:
            last = now
            now = now.next
            pre = now.prev
            
        last.next = None
        last.prev = pre
        
    def deleteNode(self, loc):#once you find the node you are looking for change its next value to the previous value
        #time complexity: O(n): We loop through the entire list once, where n is the number of elements in the list.
        #space complexity: O(1)
        if self.head is None:
            return
            
        temp = self.head
        pre = None
        
        while temp.next != loc and temp.next is not None:
            pre = temp
            temp = temp.next
            #pre = temp
        
        if temp.next == loc:
            after = temp.next.next
            
            temp.next = after
            temp.prev = pre
            
        return self.head
    
    def length(self):#counts the amount of nodes, by looping through the linked list until the temp is None
        #time complexity: O(n): We loop through the entire list once, where n is the number of elements in the list.
        #space complexity: O(1)
        counter = 0
        temp = self.head
        while temp != None:
            counter +=1
            temp = temp.next
        return counter
    
    def reverseIterative(self):#change the order of nodes until they are reversed
        #time complexity: O(n): We loop through the entire list once, where n is the number of elements in the list.
        #space complexity: O(1)
        if self.head == None:
            return
        
        
        now = self.head
        nest = None
        
        while now != None:
            nest = now.next
            now.next = now.prev
            now.prev = nest
            
            if nest == None:
                self.head = now
            now = nest
            
            
        return self.head
    
    
    def helper(self, temp, prev):#Helper function for reverseRecursive method. Recursively reverses the doubly linked list.
        if temp is None:
            return prev
        
        nest = temp.next
        temp.next = prev
        temp.prev = nest
        
        return self.helper(nest, temp)
    
    def reverseRecursive(self):
        #time complexity: O(n)
        #space complexity: O(N)
         self.head = self.helper(self.head, None)
    
    def printe(self):#used to print to see if I am doing it correctly
        if self.head is None:
            print("Empty")
            return
        
        itr = self.head
        temp = ''
        while itr:
            temp += str(itr.val) + '-->'
            itr = itr.next
        print(temp)
        
        

"""
lst = DoubleLinkedList()
lst.insertAtFront(1)
lst.printe()

lst.insertAtFront(2)
lst.printe()

# test insertAtBack method
lst.insertAtBack(3)
lst.printe()

lst.insertAtBack(4)
lst.printe()

# test insertAfter method
loc = lst.head.next
lst.insertAfter(5, loc)
lst.printe()


lst.deleteFront()
lst.printe()


lst.deleteFront()
lst.printe()
print('hello')

# test deleteBack method
lst.deleteBack()
lst.printe()


lst.deleteBack()
lst.printe()


# test deleteNode method
lst.insertAtFront(2)
lst.insertAtFront(1)
lst.insertAtBack(3)
lst.insertAtBack(4)
lst.printe()

node_to_delete = lst.head.next.next
lst.deleteNode(node_to_delete)
lst.printe()



# test length method
print(lst.length())

# test reverseIterative method




lst = DoubleLinkedList()
lst.insertAtBack(1)
lst.insertAtBack(2)
lst.insertAtBack(3)
lst.insertAtBack(4)
lst.insertAtBack(5)

print("Original list:")
lst.printe()

lst.reverseIterative()
print("Reversed list:")
lst.printe()
print("reverse back")
lst.reverseRecursive()
lst.printe()
"""

