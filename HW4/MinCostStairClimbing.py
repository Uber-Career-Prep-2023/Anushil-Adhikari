"""
time complex: O(n)
space complex: O(n)
time spent: 30 minutes
apprach: DP, I first created an array that count how much tax it charges to go to each step. Then I looped
through this arr skipping the first 2 element (b/c I can take 2 ground step for free). Then I checked which step
is cheaper to take. Finally, I set the temp[i] to this number (saying this is the cheapest way to get there)
finally, I return how many steps it takes to get to the end

"""

def MinCostStairClimbing(arr):
    temp = []

    for i in range(len(arr)+1):
        temp.append(None)

    temp[0] = 0
    temp[1] = 0

    for i in range(2, len(temp)):
        one = temp[i-1]+arr[i-1]
        two = temp[i-2]+arr[i-2]
        temp[i] = min(one, two)
        #print(temp)
    return temp[len(arr)]


print(MinCostStairClimbing([4, 1, 6, 3, 5, 8]))
print(MinCostStairClimbing([11, 8, 3, 4, 9, 13, 10]))