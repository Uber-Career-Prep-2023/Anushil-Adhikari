#Fixed-size sliding window
#35 min
#time complexity: O(n)
#space complexity: 0(n)
def MaxMeanSubArray(lst,size):
    mean = 0
    
    temp = size
    
    #create a range of input list-size+one
    #this range adjusts for all the numbers in the list
    for i in range(len(lst)-size+1):
        
        #if sum from lst[1] to lst[temp] is greater than mean, change mean value to this
        if (sum(lst[i:temp:1]))/size > mean:
            mean = sum(lst[i:temp:1])/size
            #increase temp by 1 if it does
            temp +=1
        else:
            #increase temp by 1 if it doesnt too
            temp +=1
            
    return mean

#print(MaxMeanSubArray([4, 5, -3, 2, 6, 1], 2))
#print(MaxMeanSubArray([4, 5, -3, 2, 6, 1], 3))
#print(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1], 3))
#print(MaxMeanSubArray([1, 1, 1, 1, -1, -1, 2, -1, -1, 6], 5))
