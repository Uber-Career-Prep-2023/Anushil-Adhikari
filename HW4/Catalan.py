"""
time complex: O(n^2)
space complex: O(n)
time spent: 15 minutes
approach: I created a helper function that helps me find the factorial. Then I did a for loop until the given number
and added it to the final array. finally, I returned this array

"""


def Catalan(num):
    final = []
    def fact(num):
        if num == 0:
            return 1
        if num == 1:
            return 1

        return num*(fact(num-1))

    for i in range(num+1):
        temp = fact(2*i)//(fact(i+1)*fact(i))
        final.append(temp)
    return final
print(Catalan(1))
print(Catalan(5))



