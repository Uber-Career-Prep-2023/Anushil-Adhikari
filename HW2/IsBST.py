"""
time complexity: O(n), b/c it vists every nodes
space complexity: O(n), b/b we have to store all the Nodes
time spent: 30 minutes
approach: if the left or right side violates the BST rule return false
or else keep recursioning until the nodes are None, if we have gotten no false until then it is a BST

"""


class BinarySearchTree:
    def __init__(self, value, left = None, right= None):
        self.value = value
        self.left = left
        self.right = right
        

def IsBST(root):
    
    if root == None:
        return True
    
    
    if root.left != None and root.left.value >= root.value:
        return False
    
    if root.right != None and root.right.value <= root.value:
        return False
    
            
    return IsBST(root.left) and IsBST(root.right)
    

root = BinarySearchTree(10)
root.left = BinarySearchTree(8)
root.right = BinarySearchTree(16)
#root.left.left = BinarySearchTree(1)
root.left.right = BinarySearchTree(9)
root.right.left = BinarySearchTree(13)
root.right.right = BinarySearchTree(17)
root.right.right.right = BinarySearchTree(20)

# Check if the tree is a valid binary search tree
result = IsBST(root)
print(result)