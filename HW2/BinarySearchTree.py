class BinarySearchTree:
    def __init__(self, value, left = None, right= None):
        self.value = value
        self.left = left
        self.right = right
        
        
    def smallest(self):
        if self.left == None:
            return self.value
        
        return BinarySearchTree.smallest(self.left)
    
    def biggest(self):
        if(self.right == None):
            return self.value
        
        return BinarySearchTree.biggest(self.right)
    
    def contains(self, value):
        
        if self.value == value:
            return True
        
        if(self.left != None):
            if(self.left.contains(value) == True):
                return True
            
        
                
        if(self.right != None):
            if(self.right.contains(value) == True):
                return True
        
        return False
    
    def insert(self, value):
        
        if self == None:
            return BinarySearchTree(value)
        
        if value < self.value:
            if self.left == None:
                
                self.left = BinarySearchTree(value)
                
            else:
                self.left.insert(value)
            
        elif value > self.value:
            if self.right == None:
                self.right = BinarySearchTree(value)
                
            else:
                self.right.insert(value)
        
        return self.value
    
    def delete(self, value):
        
        if self == None:
            return None
        
        if(self.value > value):
            if self.left is not None:
                self.left = self.left.delete(value)
                
        elif self.value < value:
            if self.right is not None:
                self.right = self.right.delete(value)
                
        #stuck dont how to delete the Node and connect the roots back

# Define the Binary Search Tree
n1 = BinarySearchTree(10)
n2 = BinarySearchTree(6)
n3 = BinarySearchTree(15)
n4 = BinarySearchTree(2)
n5 = BinarySearchTree(20)
n6 = BinarySearchTree(7)
n7 = BinarySearchTree(12)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n6
n3.right = n5
n3.left = n7

# Test the smallest function
result = n1.smallest()

print("smallest: "+str(result))

largest = n1.biggest()
print("biggest: "+str(largest))

print("contains:", end = " ")
print(n1.contains(7))

root = BinarySearchTree(10)
root.insert(6)
root.insert(15)
root.insert(2)
root.insert(7)
root.insert(12)
root.insert(20)




    

