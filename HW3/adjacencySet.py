"""
thoughts: very hard because I had never done graph problems before. I had to research everything before starting the problems.

"""
def adjacencySet(array):
    
    """
    Given an array of sets, create a dictionary with the connect from each Node to another.
    time complexity: O(n)
    space complexity: O(n)
    approach: create a dictionary and for each Node in the array create a unique set for it in the dict
    loop again and and add which nodes they are connected to the dict
    """
    temp = {}
    
    for i in array:
        if i[0] not in temp:
            temp[i[0]] = set()
        if i[1] not in temp:
            temp[i[1]] = set()
            
    for i in array:
        #print(i[1])
        temp[i[0]].add(i[1])
    
         
    return temp

bob = [(1, 2), (2, 3), (1, 3), (3, 2), (2, 0)]

graph = adjacencySet(bob)
#print("graph is: "+str(graph))


#graph -> dict
#target -> int
def dfs(target, graph, start, visit = []):
    """
    time complex: O(V+E)
    space complex: O(V)
    if the starting item is the target return true, if not add it to the visit array. Then loop through the graph using the start key
    then using a recurive method check all of its connections. if they match the target return true or else return false
    """
    
    if start == target:
        return True
    
    visit.append(start)
    
    for i in graph[start]:
        if i not in visit:
            temp = dfs(target, graph, i)
            if temp == True:
                return True
    return False
    

#print(dfs(0,graph,1))


def bfs(target, graph, start):
    """
    time complex: O(V+E)
    space complex:O(V)
    basic bfs
    """
    queue = [start]
    visit = [start]
    
    if start == target:
        return True
    
    while queue:
        
        #print("queue is " +str(queue))
        
        first = queue.pop(0)
        
        #print("first item is "+str(first))
        for i in graph[first]:
            if i == target:
                return True
            if i not in visit:
                visit.append(i)
                queue.append(i)
    return False


def topological(graph):
    """
    time complex: O(V+E)
    space complex:O(V)
    approach: Initialize a value of 0 for each Node
    then count the amount of edges each nodes has and set it in the dict
    put all the Node with 0 edges into queue
    loop through queue, pop the first element and add this element to the final array (the one we will return to user)
    now check all the other Node that share this element and subtract one from its edge. if the elements now have 0 edges, add it to the queue
    do this until we have no more elements in the queue. Now we have to check if the length of the final array and our dict is the same
    if it is not the same, we know there is a loop so we return "there is a cycle". if it is equal we return the final list to user

    """
    in_degree = {}
    for i in graph:
        in_degree[i] = 0
    
    for i in graph:
        #print(graph[i])
        for v in graph[i]:
            in_degree[v] +=1
    
    queue = []
    for i in in_degree:
        if in_degree[i] == 0:
            queue.append(i)
            
    final = []
    #print(queue)
    print(in_degree)
    while queue:
        item = queue.pop(0)
        
        final.append(item)
        
        #print(graph[item])
        
        
        for i in graph[item]:
            in_degree[i] -=1
            
            if in_degree[i] == 0:
                queue.append(i)
                
    if len(final) != len(graph):
        return "there is a cycle"
    
        #print(in_degree)
        
        
    return final
    #print("final is: "+str(final))

#print(topological(graph))
#temp = [(5,0),(4,0),(5,2),(4,1),(2,3),(3,1),(4,1)]
#graph1 = adjacencySet(temp)

#print("graph1 is: "+str(graph1))
#topological(graph1)
#print(topological(graph1))
