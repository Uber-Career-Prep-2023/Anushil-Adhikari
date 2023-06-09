"""
Question 4: NumberOfIslands
Given a binary matrix in which 1s represent land and 0s represent water.
Return the number of islands (contiguous 1s surrounded by 0s or the edge of the matrix).

type: graph problem
time complex: O(n*m)
space complex: O(1)
approach: I used dfs recursion method to solve this problem
time spent: 35 minutes
"""

def NumberOfIslands(array):
    if not array:
        return 0
    
    islands = 0
    
    def dfs(array, row, col):
        array[row][col] = "2"
        directions = [[row-1, col],[row+1, col], [row, col-1], [row, col+1]]
        #print(array)
        for row, col in directions:
            #print(row, col)
            if row >=0 and col >=0 and row < len(array) and col < len(array[row]) and array[row][col] == "1":
                dfs(array, row, col)
            
    
    for row in range(len(array)):
        for col in range(len(array[row])):
            if array[row][col] == "1":
                dfs(array, row, col)
                islands +=1
            
    return islands

#print("hello")
grid1 = [["1","1","0","0","0"]]
#print(grid1[0][1])
grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
print(NumberOfIslands(grid))
