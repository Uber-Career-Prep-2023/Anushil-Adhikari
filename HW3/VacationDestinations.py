"""
time spent: 35 minutes
time complexity: O(n)
space complexity: O(n)
approach: I used the bfs method to solve this problem. first I created a hashmap with all the cities.
Then, I checked which cities you can go to from this city within our time limit. When adding to the queue,
since our stopover adds an hour, I added (x, h - y-1) to the q, so when it loops again it would check how far we can get
from that city.

"""


def VacationDestinations(array, location, hours):

    dictt = {}

    for x,y,z in array:
        dictt[x] = []
        dictt[y] = []

    for x,y,z in array:
        dictt[x].append((y, z))
        dictt[y].append((x, z))

    #print(dictt)

    q = [(location, hours)]
    visit = set()
    visit.add((location, hours))
    final = []
    while q:
        first, h = q.pop(0)
        for x,y in dictt[first]:
            if x != location:
                if y <= h:
                    if (x, y) not in visit:
                        final.append(x)
                        q.append((x, h - y-1))
                        visit.add((x, h - y-1))

    return final

lst = [("Boston", "New York", 4), ("New York", "Philadelphia", 2), ("Boston", "Newport", 1.5), ("Washington D.C.", "Harper's Ferry", 1), ("Boston", "Portland", 2.5), ("Philadelphia", "Washington D.C.", 2.5)]
print(VacationDestinations(lst, "New York", 5))
print(VacationDestinations(lst, "New York", 7))
print(VacationDestinations(lst, "New York", 8))
