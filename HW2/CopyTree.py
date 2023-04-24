class BinarySearchTree:
    def __init__(self, value, left = None, right= None):
        self.value = value
        self.left = left
        self.right = right
        
    """
time complexity: O(n), because we have to visit all the nodes
space complexity: O(n), because we have to store a new tree
approach: check if the root is None (to see if there is a tree for us to copy)
if its not None, copy the Node value, and recursively copy both of its branches
time spent: 30 minutes
    """
        
def CopyTree(root):
    
    if root != None:
        copy = BinarySearchTree(root.value)
        copy.left = CopyTree(root.left)
        copy.right = CopyTree(root.right)
    else:
        return None
    
    return copy

"""
root = BinarySearchTree(1)
root.left = BinarySearchTree(2)
root.right = BinarySearchTree(3)
root.left.left = BinarySearchTree(4)
root.left.right = BinarySearchTree(5)

new_root = CopyTree(root)

root.value = 0
root.left.value = -1
root.right.value = -2

print(new_root.value == 1)
print(new_root.left.value == 2)
print(new_root.right.value == 3)
print(new_root.left.left.value == 4)
print(new_root.left.right.value == 5)
"""



