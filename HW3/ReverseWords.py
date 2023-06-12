"""
method used: stack
time complexity: O(n)
space complexity:O(n)
approach: I first split the string and turned the string into a list
then, I popped the last time adn added it to the final string (the one I will return to user)
if the list still exist (meaning there is more words in the list) I added a space, or else I did not
finally I returned the string final to user.
time spent: 15 mintutes
"""

def ReverseWords(string):
    lst = string.split()

    #print(lst)
    final = ""

    while lst:
        temp = lst.pop()
        if lst:
            final += temp
            final += " "

        else:
            final += temp

    return final


print(ReverseWords("Uber Career Prep"))
print(ReverseWords("Emma lives in Brooklyn, New York."))