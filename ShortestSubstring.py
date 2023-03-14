"""
time used: 55 minutes
time complexity: O(n)
space complexity: O(n)
method used: two pointer

Very hard, I did not know how to approach this problem at first
Saw the basic algorithms for this type of problems to understand the approach
My code might not be the most effective way to solve it

"""
def shortest_substr1(str1, str2):
    
    if(len(str2) > len(str1)):
        return False
    temp = {}
    for c in str2:
        if c not in temp:
            temp[c] = 1
        else:
            temp[c] += 1

    first = 0
    last = 0
    counter = 0
    min_len = len(str1)

    while last < len(str1):
        if str1[last] in temp:
            
            temp[str1[last]] -= 1
            
            if temp[str1[last]] >= 0:
                counter += 1

        while counter == len(str2):
            if last - first + 1 < min_len:
                
                min_len = last - first + 1

            if str1[first] in temp:
                
                temp[str1[first]] += 1
                
                if temp[str1[first]] > 0:
                    counter -= 1
            first += 1
            
            
        last += 1

    if min_len != len(str1):
        return min_len
    else:
        return len(str1)


#print(shortest_substr1("abracadabra", "abc")) returns 4
#print(shortest_substr1("zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx")) returns 10
#print(shortest_substr1("dog", "god")) returns 3
"""
Question 5: ShortestSubstr1
Given a str1 and a second str1 representing str2 characters, return the length of the shortest substr1 containing all the str2 characters.

Examples:
Input str1s: "abracadabra", "abc"
Output: 4
(Shortest Substr1: "brac")

Input str1s: "zxycbaabcdwxyzzxwdcbxyzabccbazyx", "zzyzx" (Fun fact: "Zzyzx" is a town in the Mojave Desert in California!)
Output: 10
(Shortest Substr1: "zzxwdcbxyz")

Input str1s: "dog", "god"
Output: 3
(Shortest Substr1: "dog")

"""