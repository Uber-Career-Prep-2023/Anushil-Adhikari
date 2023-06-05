class Heap:

    
    def __init__(self):
        self.storage = []#creating a array used to store the Heap
        self.size = 0
    
    def top(self):
        if len(self.storage) <=0:#if the Heap is empty return None or else return the first element
            return
        
        return self.storage[0]
    
    def parent(self, index):#returns the parents index
        return (index-1)//2
    
    def leftChild(self, index):#returns the leftChild index
        return (2*index)+1
        
    def rightChild(self, index):#returns the rightChild index
        return (2*index)+2
        
    def heapifyUp(self, index):#helper method for insert
        #if the parent Node exists and its value is bigger than the value we are inserting
        #swap the parent value and the new value and set the index the new index parent
        
        
        while self.parent(index) >=0 and self.storage[self.parent(index)] > self.storage[index]:
            
            temp = self.storage[self.parent(index)]
            self.storage[self.parent(index)] = self.storage[index]
            self.storage[index] = temp
            index = self.parent(index)
    
    def insert(self, Node):
        
        self.storage.append(Node)
        self.size +=1
        self.heapifyUp(self.size-1)
        
        
        #removes the top element
    def remove(self):
        
        temp = self.top()
        
        if temp is None:
            return None
        
        self.storage[0] = self.storage[self.size-1]
        
        self.storage.pop()
        self.size -=1
        
        self.heapifyDown()
        return temp
    
    def heapifyDown(self):
        index = 0
        #while the left child exists, set the small variable to its index, compare the left value to the right value
        #which ever is smaller set their index to small, if the head value is < the small variable, break out of loop
        #or else swap the values and set index to small, so it will loop until it finds a smaller value or until there are no more child
        
        while self.leftChild(index) < self.size:
            
            small = self.leftChild(index)
            
            if self.rightChild(index) < self.size and self.storage[self.leftChild(index)] > self.storage[self.rightChild(index)]:
                small = self.rightChild(index)
                
            if self.storage[index] < self.storage[small]:
                break
            else:
                
                temp = self.storage[index]
                self.storage[index] = self.storage[small]
                self.storage[small] = temp

                
            index = small
            
        


a = Heap()
print(a.top())
print(a.storage)

a.insert(10)
a.insert(12)
a.insert(70)
a.insert(8)
a.insert(20)
a.insert(0)
a.insert(60)


print(a.storage)
a.remove()
print(a.storage)