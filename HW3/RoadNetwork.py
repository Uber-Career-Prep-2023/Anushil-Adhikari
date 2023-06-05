


"""
time spent: 35 minutes
time complex: O(n)
space complex: O(n)
approach: I used bfs to solve this problem
first I created a dictionary with all the links, then I checked if the Node was in the visited, if not, I performed bfs to it and increasd
the counter
In the bfs method, I created a queue and added the Node to it, I also added it to the visited array. Then I performed basic bfs, until
there were no more items left in the queue
"""

def RoadNetworks(lst1, lst2):
    dictt = {}
    visit = []
    for i,u in lst2:
        if i not in dictt:
            dictt[i] = [u]
        else:
            dictt[i].append(u)
        
        if u not in dictt:
            dictt[u] = [i]
        else:
            dictt[u].append(i)
    
    def bfs(point):
        q = []
        q.append(point)
        visit.append(point)
        
        while q:
            first = q.pop(0)
            
            for i in dictt[first]:
                if i not in visit:
                    q.append(i)
                    visit.append(i)
    count = 0
    for i in dictt:
        if i not in visit:
            bfs(i)
            count +=1
    
    if len(visit) == len(dictt):
        return count
            
    return 0

lst1 = ["Kona", "Hilo", "Volcano", "Lahaina", "Hana", "Haiku", "Kahului", "Princeville", "Lihue", "Waimea"]
lst2 = [("Anchorage", "Homer"), ("Glacier Bay", "Gustavus"), ("Copper Center", "McCarthy"), ("Anchorage", "Copper Center"), ("Copper Center", "Fairbanks"), ("Healy", "Fairbanks"), ("Healy", "Anchorage")]
lst3 = [("Kona", "Volcano"), ("Volcano", "Hilo"), ("Lahaina", "Hana"), ("Kahului", "Haiku"), ("Hana", "Haiku"), ("Kahului", "Lahaina"), ("Princeville", "Lihue"), ("Lihue", "Waimea")]
print(RoadNetworks(lst1,lst3))


