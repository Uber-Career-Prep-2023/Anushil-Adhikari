#10 time spent: 20 min
#method used: pointer method
#questions: is test two wrong in the examples because I dont get why it would return 4
#time complexity: O(n)
#space complexity: O(n)

def TwoSum(arr, target):
    counter = 0
    firstPointer = 0
    lastPointer = len(arr)-1
    arr.sort()
    
    while(firstPointer < lastPointer):
        if(arr[firstPointer] + arr[lastPointer] == target):
            counter +=1
            lastPointer -=1
        else:
            lastPointer -=1
        
        if(firstPointer == lastPointer):
            firstPointer +=1
            lastPointer = len(arr)-1
    
    return counter

##print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 10))
##print(TwoSum([1, 10, 8, 3, 2, 5, 7, 2, -2, -1], 8))
##print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 6))
##print(TwoSum([4, 3, 3, 5, 7, 0, 2, 3, 8, 6], 1))