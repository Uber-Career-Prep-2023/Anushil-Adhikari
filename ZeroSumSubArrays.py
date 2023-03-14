"""
Input Array: [4, 5, 2, -1, -3, -3, 4, 6, -7]
Output: 2
(Subarrays: [5, 2, -1, -3, -3], [-3, 4, 6, -7])

Input Array: [1, 8, 7, 3, 11, 9]
Output: 0

Input Array: [8, -5, 0, -2, 3, -4]
Output: 2
(Subarrays: [0], [8, -5, 0, -2, 3, -4])

"""
"""
time spent: 30 minutes
time complexity: O(n)
space compexity: 0(n)
method used: Hash the elements

"""


def ZeroSumSubArrays(arr):
    counter = 0
    temp = {}
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        if total in temp:
            counter += 1
            temp[total] += 1
        else:
            temp[total] = 1
            
    if(0 in temp):
        #print("num of zero: "+str(temp[0]))
        counter += temp[0]
    
    return counter

"""
print(ZeroSumSubArrays([4, 5, 2, -1, -3, -3, 4, 6, -7])) returns 2
print(ZeroSumSubArrays([1, 8, 7, 3, 11, 9])) returns 0
print(ZeroSumSubArrays([8, -5, 0, -2, 3, -4])) returns 2
print(ZeroSumSubArrays([1,-1,2,-2,-1])) returns 3
 """   

    
