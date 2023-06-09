"""""
time spent: 40 minutes (had a hard time figuring out the bfs)
methods used: bfs
time complexity: O(n)
space complexity: O(n)
approach: first I created a holder list for each Node. Then I appended its color and which node it leads to its value.
I then, created the queue and visit array and added the (orgin, its color and distance) inside.
In my bfs, I checked if first( first item on q) is on temp dictt, if it is, I checked to make sure the color is different
and that this tuple is not in the visit array. if it passes this I add it to queue with a increased in distance by 1.
this would loop until I find my destination.
"""


def AlternatingPath(array, orgin, destination):
    temp = {}
    count = 0
    if orgin == destination:
        return -1
    if not array:
        return -1

    for i in array:
        temp[i[0]] = []
        temp[i[1]] = []

    for first, second, third in array:
        temp[first].append((second, third))

    q = []
    visit = []

    q.append((orgin, "", 0))
    visit.append((orgin, ""))



    print(temp)
    while q:
        first, color, distance = q.pop(0)

        if first == destination:
            return distance

        if first in temp:
            for n, c in temp[first]:
                if c != color and (n, c) not in visit:
                    q.append((n,c, distance+1))
                    visit.append((n, c))
    return -1



map = [("A", "B", "blue"), ("A", "C", "red"), ("B", "D", "blue"), ("B", "E", "blue"), ("C", "B", "red"), ("D", "C", "blue"), ("A", "D", "red"), ("D", "E", "red"), ("E", "C", "red")]
bob = AlternatingPath(map, "A", "E")
print(bob)#should print out 4
bob1 = AlternatingPath(map, "E", "D")
print(bob1)#should print out -1