#Q7
#55 min
def KAnagrams(string, second, k):
    
    if len(string) != len(second):
        return False
    
    temp1 = {}
    temp2 = {}
    for i in string:
        if i in second:
            if i not in temp1:
                temp1[i] = 1
            else:
                temp1[i] +=1
        else:
            k -=1
    
    for i in second:
        if i in string:
            if i not in temp2:
                temp2[i] = 1
            else:
                temp2[i] +=1
    #print(temp1)
    #print(temp2)
    #print(sum(temp1.values()))
    
    #print(sum(temp2.values()))
    #print(k)
    if sum(temp1.values()) > sum(temp2.values()):
        return sum(temp1.values()) == sum(temp2.values())+k
    elif sum(temp1.values()) < sum(temp2.values()):
        return sum(temp2.values()) == sum(temp1.values())+k
    #return len(temp)+k == len(string)
    return sum(temp1.values())+k == sum(temp2.values())

print(KAnagrams("baseball", "basketball", 1))

print(KAnagrams("apple", "peach", 1))