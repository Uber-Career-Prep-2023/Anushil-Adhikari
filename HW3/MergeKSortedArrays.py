"""
method used: heap
time complexity: O(nlog k) k-how many arrays
space complexity: O(n)
time spent: 35 minutes
approach: first, I created a heap class and did the basic insert/delete methods
Then in my MergeKSortedArrays method, I created a heap and inserted all the values from array into the heap
Then, I loop through the heap and remove the first element and added this element to my final array (the one I will return to user)
finally, once the loop end I return the final array
"""


class Heap:
    def __init__(self):
        self.storage = []
        self.count = 0

    def parent(self, i,):
        return (i-1)//2

    def leftchild(self, i):
        return (2*i)+1

    def rightChild(self, index):
        return (2*index)+2


    def insert(self, val):
        self.storage.append(val)
        self.count +=1
        self.Heapify(len(self.storage)-1)

    def Heapify(self, index):

        while self.parent(index) >=0 and self.storage[self.parent(index)] > self.storage[index]:
            temp = self.storage[self.parent(index)]
            self.storage[self.parent(index)] = self.storage[index]
            self.storage[index] = temp
            index = self.parent(index)

    def HeapifyDown(self):
        i = 0

        while self.leftchild(i) < self.count:
            small = self.leftchild(i)

            if self.rightChild(i) < self.count:
                if self.storage[small] > self.storage[self.rightChild(i)]:
                    small = self.rightChild(i)

            if self.storage[i] <= self.storage[small]:
                break
            else:
                temp = self.storage[i]
                self.storage[i] = self.storage[small]
                self.storage[small] = temp
                i = small

    def removeMin(self):

        if len(self.storage) == 0:
            return None

        top = self.storage[0]
        self.storage[0] = self.storage[len(self.storage)-1]
        self.count -= 1
        self.storage.pop()
        self.HeapifyDown()
        return top


def MergeKSortedArrays(num, array):
    heap = Heap()
    final = []

    for i in array:
        for u in range(len(i)):
            heap.insert(i[u])

    while heap.count:
        temp = heap.removeMin()
        final.append(temp)

    return final

print(MergeKSortedArrays(2, [[1, 2, 3, 4, 5], [1, 3, 5, 7, 9]]))
print(MergeKSortedArrays(3, [[1, 4, 7, 9], [2, 6, 7, 10, 11, 13, 15], [3, 8, 12, 13, 16]]))
