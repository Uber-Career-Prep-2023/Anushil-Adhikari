"""
Question 8: CoinChange
Given a list of coin denominations and a target sum, return the number of possible ways to make change for that sum.

Examples:
Input:
Coins: [2, 5, 10]

Sum: 20
Output: 6 (Options are: 10 2s; 4 5s; 2 10s; 5 2s & 2 5s; 5 2s & 1 10; 2 5s & 1 10)

Sum: 15
Output: 2 (Options are: 5 2s & 1 5; 1 5 & 1 10)


"""

"""
time spent: 25 minutes
time complexity: O(n)
space complexity: O(n)
approach: To solve this problem, I used dynamic programming. First, I created an array that is 1 bigger than the sum.
I will use this list to see how many ways there are to add up to this index. I changed the first element to a one, 
because there is only one way to add to 0 (to add no coins). Then I loop through the array given to us. I do another loop
from this coin to the last element in my temp list. Then I calculate how many ways I can add up to each number.
Finally, I return how many ways we can add up to the sum.
"""

def CoinChange(arr, sum):
    temp = [0] * (sum+1)
    temp[0] = 1

    for coin in arr:
        for u in range(coin, len(temp)):
            temp[u] += temp[u-coin]

    return temp[sum]

print(CoinChange([2, 5, 10], 20))
print(CoinChange([2, 5, 10], 15))
