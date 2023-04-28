"""
time complexity: 0(n): we have to go every Node
space complexity: 0(n) i think because we dont have constant space
time spent: 25 minutes
approach: if the root value equals target return it, if the root value is greater than target, check its left branches
if the value is greater than target, loop through its right side of branch, finally, if it is smaller than the target return the value
thoughts: looked very simple at the beginning however, took some time to figure out how to get the closest number to value
"""



class BinarySearchTree:
    def __init__(self, value, left = None, right= None):
        self.value = value
        self.left = left
        self.right = right


def FloorInBST(root, target):
    if root is None:
        return None

    if root.value == target:
        return root.value

    if root.value > target:
        return FloorInBST(root.left, target)
            
    if root.value < target:
        temp = FloorInBST(root.right, target)
        if temp is not None and temp <= target:
            return temp

    return root.value
    

"""
root = BinarySearchTree(8)
root.left = BinarySearchTree(3)
root.right = BinarySearchTree(10)
root.left.left = BinarySearchTree(1)
root.left.right = BinarySearchTree(6)
root.left.right.left = BinarySearchTree(4)
root.left.right.right = BinarySearchTree(7)
root.right.right = BinarySearchTree(14)
root.right.right.left = BinarySearchTree(13)
print(FloorInBST(root, 14))
""" 


            
    
    