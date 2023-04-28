class BinarySearchTree:
    def __init__(self, value, left = None, right= None):
        self.value = value
        self.left = left
        self.right = right
"""
time complexity: O(n)
space complexity: O(n)
time spent: 35 minutes
approach: using helper method, I add the left most value of the tree to the list. The helper method
compares the level to the length of the list. if the level is greater than the list length it means its the left most
value, so it will add it to the list.


"""




def LeftView(root):
    
    temp = [root.value]
    helper(root, 1, temp)
    
    return temp

def helper(root, level, temp):
    if root == None:
        return
    
    if level > len(temp):
        temp.append(root.value)
    
    helper(root.left, level + 1, temp)
    helper(root.right, level + 1, temp)
    

"""
root = BinarySearchTree(7)
root.left = BinarySearchTree(8)
root.right = BinarySearchTree(3)

root.right.left = BinarySearchTree(9)
root.right.left.left = BinarySearchTree(20)


root.right.right = BinarySearchTree(13)


root.right.right.right = BinarySearchTree(14)
root.right.right.right.right = BinarySearchTree(15)

print(LeftView(root))

root = BinarySearchTree(7)
root.left = BinarySearchTree(20)
root.left.left = BinarySearchTree(15)
root.left.right = BinarySearchTree(6)
root.right = BinarySearchTree(4)
root.right.left = BinarySearchTree(8)
root.right.right = BinarySearchTree(11)
print(LeftView(root))
"""
