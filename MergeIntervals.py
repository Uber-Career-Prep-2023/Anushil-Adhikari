"""
Question 8: MergeIntervals
Given a list of integer pairs representing the low and high end of an interval, inclusive, return a list in which overlapping intervals are merged.

Examples:

Input: [(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]
Output: [(4, 8), (1, 3), (9, 12)]

Input: [(5, 8), (6, 10), (2, 4), (3, 6)]
Output: [(2, 10)]

Input: [(10, 12), (5, 6), (7, 9), (1, 3)]
Output: [(10, 12), (5, 6), (7, 9), (1, 3)]

"""

"""
time spent: 20 minutes
I used the Sorting & Searching Techniques for this problem
#time complexity: O(n log n), b/c it only loops through the array once and it also sorts the array
#space complexity: 0(n),



"""
def MergeIntervals(lst):
    
    lst.sort()
    final = []
    #print(lst)
    
    for i in range(1, len(lst)):
        if lst[i-1][1] >= lst[i][0]:
            temp =(lst[i-1][0], max(lst[i-1][1], lst[i][1]))
            lst[i] = temp
        else:
            final.append(lst[i-1])
            
    final.append(lst[-1])
    
    return final

"""
print(MergeIntervals([(2, 3), (4, 8), (1, 2), (5, 7), (9, 12)]))
print(MergeIntervals([(5, 8), (6, 10), (2, 4), (3, 6)]))
print(MergeIntervals([(10, 12), (5, 6), (7, 9), (1, 3)]))
 """   
    