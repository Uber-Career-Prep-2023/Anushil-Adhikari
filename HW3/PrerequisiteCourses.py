""""
time spent: 40 min
time complexity: O(n)
space complexity: O(n)
approach: for this problem, I used topological sorting. I checked how many arrows were pointing to each class and the ones with 0
got added to queue. Then I looped through the queue, pop the first element and add this element to the final array (the one we will return to user)
now check all the other Node that share this element and subtract one from its edge.
if the elements now have 0 edges, add it to the queue do this until we have no more elements in the queue


"""

def PrerequisiteCourses(arr, dictt):

    temp = {}

    for i in arr:
        temp[i] = []

    for key,value in dictt.items():
        for i in value:
            temp[i].append(key)



    indegrees = {}
    for i in arr:
        indegrees[i] = 0

    for i in temp:
        for v in temp[i]:
            indegrees[v] +=1

    q = []

    for i in indegrees:
        if indegrees[i] == 0:
            q.append(i)



    final = []
    while q:
        first = q.pop(0)
        final.append(first)

        for i in temp[first]:
            indegrees[i] -=1
            if indegrees[i] == 0:
                q.append(i)
    return final

lst = ["Intro to Programming", "Data Structures", "Advanced Algorithms", "Operating Systems", "Databases"]
dictt = { "Data Structures": ["Intro to Programming"], "Advanced Algorithms": ["Data Structures"], "Operating Systems": ["Advanced Algorithms"], "Databases": ["Advanced Algorithms"] }
lst1 = ["Intro to Writing", "Contemporary Literature", "Ancient Literature", "Comparative Literature", "Plays & Screenplays"]
dictt1 = { "Contemporary Literature": ["Intro to Writing"], "Ancient Literature": ["Intro to Writing"], "Comparative Literature": ["Ancient Literature", "Contemporary Literature"], "Plays & Screenplays": ["Intro to Writing"] }
bob = PrerequisiteCourses(lst, dictt)
bob1 = PrerequisiteCourses(lst1, dictt1)
print(bob)
print(bob1)