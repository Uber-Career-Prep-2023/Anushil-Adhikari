class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtFront(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        return self.head
        
        
    def insertAtBack(self, val):
        newNode = Node(val)
        
        if self.head is None:
            self.head = newNode
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        return
    
    def insertAfter(self, val, loc):
        newNode = Node(val)
        temp = self.head
        
        while temp != loc:
            temp = temp.next
        
        if temp == loc:
            if loc.next != None:
                newNode.next = loc.next
            temp.next = newNode
            
    def deleteFront(self):
        temp = self.head
        if temp != None:
            self.head = temp.next
            
        return self.head
    def deleteBack(self):
        
        if self.head is None:
            return
        
        last = None
        now = self.head
        
        while now.next != None:
            last = now
            now = now.next
            
        last.next = None
        
    def deleteNode(self, loc):#might have to fix
        
        if self.head is None:
            return
            
        temp = self.head
        
        while temp.next != loc:
            temp = temp.next
        
        if temp.next == loc:
            after = temp.next.next
            temp.next = after
            
        return self.head
    
    def length(self):
        counter = 0
        temp = self.head
        while temp != None:
            counter +=1
            temp = temp.next
        return counter
    
    def reverseIterative(self):
        last = None
        now = self.head
        
        while now:
            temp = now.next
            now.next = last
            last = now
            now = temp
        return last
    
    def helper(self, temp):
        if not temp or not temp.next:
            return temp
        
        head = self.helper(temp.next)
        temp.next.next = temp
        temp.next = None
        return head
    
    def reverseRecursive(self):
        self.head = self.helper(self.head)
    
    def printe(self):
        if self.head is None:
            print("Empty")
            return
        
        itr = self.head
        temp = ''
        while itr:
            temp += str(itr.val) + '-->'
            itr = itr.next
        print(temp)
        
            

lst = LinkedList()
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

node_to_delete = lst.head.next.next
lst.deleteNode(node_to_delete)
lst.printe()



# test length method
print(lst.length())

# test reverseIterative method
print("in recurvice")
new_head = lst.reverseIterative()
lst.head = new_head
lst.printe()

lst = LinkedList()
lst.insertAtBack(1)
lst.insertAtBack(2)
lst.insertAtBack(3)
lst.insertAtBack(4)
lst.insertAtBack(5)

print("Original list:")
lst.printe()

lst.reverseRecursive()
print("Reversed list:")
lst.printe()
#lst.printe()  # should print "4-->3-->2-->1-->"




        
        


