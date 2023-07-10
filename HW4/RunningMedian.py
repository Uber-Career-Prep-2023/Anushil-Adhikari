"""
time complex: O(nlog N)
space complex: O(n)
time spent: 35 minutes
approach: create 2 heap, one to store the min and one to stores the max. if max heap is empty
or if the num < max in max heap, add it to max heap, else add it to minheap
then return median
"""


import heapq
def RunningMedian():
    maxs = []
    min = []
    while True:
        temp = input("Enter a number or type stop: ")
        if temp == "stop":
            break
        num = int(temp)

        if len(maxs) == 0 or num < -maxs[0]:
            heapq.heappush(maxs, -num)
        else:
            heapq.heappush(min, num)

        while len(maxs) < len(min):
            heapq.heappush(maxs, -heapq.heappop(min))
        while len(maxs) > len(min) + 1:
            heapq.heappush(min, -heapq.heappop(maxs))

        if len(maxs) == len(min):
            median = (-maxs[0] + min[0]) / 2.0
        else:
            median = -maxs[0]

        print(median)


RunningMedian()
