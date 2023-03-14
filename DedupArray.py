#9 10 min
#time complexity: O(n)
#space complexity: 0(n)
#method used: Sorting algorithm variation
def DedupArray(lst):
    temp = []
    
    #if lst[i] is not in the temp list add it to the list
    #if it is already in the list go to another index
    for i in lst:
        if i not in temp:
            temp.append(i)
            
    #we can delete the original list to save space
    del(lst)
    return temp

print(DedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))