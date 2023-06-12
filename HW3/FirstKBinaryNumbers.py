"""
time spent: 10 min
time complex: O(n)
space complex: O(n)
appraoch: use the bin method to turn the element we are on to its binary code
remove the first 2 item from this b/c it would be 0b, add this to our list
"""


def FirstKBinaryNumbers(num):
    temp = []
    for i in range(num):
        bob = bin(i)[2::]
        temp.append(bin(i)[2::])
    
    return temp

print(FirstKBinaryNumbers(10))
