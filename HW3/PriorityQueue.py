class PriorityQueue:
    
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def top(self):
        if len(self.queue) <=0:#if the Queue is empty return None or else return the first element
            return
        return self.queue[0]
    
    def parent(self, index):#returns the parents index
        return (index-1)//2
    
    def leftChild(self, index):#returns the leftChild index
        return (2*index)+1
    
    def rightChild(self, index):#returns the rightChild index
        return (2*index)+2

    
    def heapifyUp(self, index):
        """"
        if the parent Node exists and its weight is smaller than the weight we are inserting
        swap the parent Node and the new Node and set the index the new index parent
        time complex: O(log n)
        space complex: O(1)
        """
        
        while self.parent(index) >=0 and self.queue[self.parent(index)][1] < self.queue[index][1]:
            temp = self.queue[self.parent(index)]  #parent value

            self.queue[self.parent(index)] = self.queue[index]
            self.queue[index] = temp

            index = self.parent(index)
    
    def insert(self, string, weight):
        self.queue.append((string, weight))
        self.size +=1
        self.heapifyUp(self.size-1)

    def heapifyDown(self):
        index = 0
        """"
        while the left child exists(right cannot exist if there is no left child), set the biggest variable to its index,
        compare the left weight to the right weight which ever is bigger set their index to biggest, 
        if the head weight is > the small variable, break out of loop, or else swap the weight and set index to biggest,
        so it will loop until it finds a bigger weight or until there are no more child
        time complex: O(log n)
        space complex: O(1)
        
        """

        while self.leftChild(index) < len(self.queue)-1 and self.queue[index][1] < self.queue[self.leftChild(index)][1]:
            biggest = self.leftChild(index)
            if self.rightChild(index) < len(self.queue)-1 and self.queue[self.leftChild(index)][1] < self.queue[self.rightChild(index)][1]:
                biggest = self.queue[self.rightChild(index)]

            if self.queue[index][1] > self.queue[biggest][1]:
                break
            else:
                temp = self.queue[index]
                self.queue[index] = self.queue[biggest]
                self.queue[biggest] = temp
                index = biggest


    def remove(self):
        temp = self.top()
        if temp is None:
            return None
        self.queue[0] = self.queue[self.size-1]
        self.queue.pop()
        self.size -= 1
        self.heapifyDown()



a = PriorityQueue()
a.insert("hello", 1)
a.insert("my", 4)
a.insert("Anushil", 10)
a.insert("Adhikari", 6)
a.insert("bob", 2)

print(a.queue)
a.remove()
print(a.queue)
a.insert("danny", 190)
a.insert("d", 1910)
a.insert("s", 1930)
print(a.queue)