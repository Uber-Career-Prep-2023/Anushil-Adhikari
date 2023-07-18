"""
time spent: 30 min
Time complex: O(r*c)
space complex: O(r*c)
approach: DP, first I create an empty dp list, with all 0.Then I loop through the arr and find a 1, and
then check its left, top, and left-top boxes to see if they are ones,
if they are that means the box size can be inceased.

"""

def LargestSquareOf1s(arr):
    if not arr:
        return 0

    dp = []
    final = 0

    for i in arr:
        dp.append([0]*len(arr[0]))

    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            if arr[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                if dp[i][j] > final:
                    final = dp[i][j]

    return final


matrix1 = [
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]

matrix2 = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0]
]

print(LargestSquareOf1s(matrix1))
print(LargestSquareOf1s(matrix2))