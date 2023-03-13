"""
Question 2: ReverseVowels
Given a string, reverse the order of the vowels in the string.

Examples:
Input String: "Uber Career Prep"
Modified String: "eber Ceraer PrUp"

Input String: "xyz"
Modified String: "xyz"

Input String: "flamingo"
Modified String: "flominga"

"""
#time spent: 20 minutes
#method used: Forward/backward two pointer method
#time complexity: O(n), b/c it only loops through the array once
#space complexity: 0(n), b/c there is only a 1d list
#approach: start a pointer in the start and the end of string
#if one of them is a vowel, check to see if the other one is a vowel
#keep looping through the string until you find the ext vowel, then replace them
def ReverseVowels(given):
    temp = list(given)
    first = 0
    last = len(given)-1
    vowels = "AEIOUaeiou"
    #print(len(given))
    #print(len(temp))
    final = ""
    
    while first < last:
        if given[first] in vowels:
            if given[last] in vowels:
                #holder = given[last]
                temp[first] = given[last]
                temp[last] = given[first]
                first +=1
                last -=1
            else:
                last -=1
        else:
            first +=1
    
    for i in temp:
        final += i
    
    return final
    
"""
print(ReverseVowels("Uber Career Prep")) returns eber Ceraer PrUp
print(ReverseVowels("xyz")) returns xyz
print(ReverseVowels("flamingo")) returns flominga
print(ReverseVowels("aws")) returns aws
"""