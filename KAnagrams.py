#Q7
#55 min
#time complexity: O(n)
#space complexity: 0(n)
#method used: Hash the elements
def KAnagrams(string, second, k):
    
    #if the length of the strings do not match, return false
    if len(string) != len(second):
        return False
    
    #dict to keep track of how many times a letter popped up in string one
    temp1 = {}
    
    #dict to keep track of how many times a letter popped up in string two
    temp2 = {}
    
    for i in string:
        #checks how many times a letter in string one, also pops up in string two
        if i in second:
            #if it pops up in both add it to temp1
            if i not in temp1:
                temp1[i] = 1
            else:
                #if it is already in temp1 incrase the value by one
                temp1[i] +=1
                
        #if it appears in string one but does not appear in string two, -1 from k,
        #because that is how man letters we are allowed to switch
        else:
            k -=1
    
    for i in second:
        #checks how many times a letter in string two, also pops up in string one
        if i in string:
            if i not in temp2:
                temp2[i] = 1
            else:
                temp2[i] +=1
    
    #print("temp1: "+str(temp1))
    #print("temp2: "+str(temp2))
    
    #if the value of temp1 is bigger than temp2,
    #check if temp2 values +k is equal to temp1 value
    #if it is not return false
    if sum(temp1.values()) > sum(temp2.values()):
        return sum(temp1.values()) == sum(temp2.values())+k
    
    #same thing as the top but we are checking if temp2 value is bigger than temp1
    elif sum(temp1.values()) < sum(temp2.values()):
        return sum(temp2.values()) == sum(temp1.values())+k
    
    #if the values are the same, add k to one of them (doesnt matter which one cuz k should be zero for it to return true)
    #if k is not 0 it would be false
    return sum(temp1.values())+k == sum(temp2.values())



#print(KAnagrams("apple", "peach", 1))
#print(KAnagrams("apple", "peach", 2))
#print(KAnagrams("cat", "dog", 3))
#print(KAnagrams("debit curd", "bad credit", 1))
#print(KAnagrams("baseball", "basketball", 1))
