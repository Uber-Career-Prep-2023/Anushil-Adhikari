from collections import deque

"""
time spent: 35 min
time complex: O(n)
space complex: O(n)
approach: first, I created 2 arr (one for dog, one for cat) and appended animals then I looped through the happens arr,
and check if its a person, if it is what animal they want and then I check if we have that animal, if we do. we give
them the oldest type of that animal. if we dont have that animal, we give them the oldest animal. if it is not a person,
I add check if its a dog or a cat and add it to the right list

"""

def third(arr):
    return arr[2]
def AdoptAPet(arr, happens):
    arr = sorted(arr, key=third, reverse=True)
    dogs = deque()
    cats = deque()
    for i in arr:
        if i[1] == "dog":
            dogs.appendleft(i)
        elif i[1] == "cat":
            cats.appendleft(i)


    for x, y , z in happens:
        if y == 'person':
            if z == "dog":
                if dogs:
                    name, type, days = dogs.pop()
                    print(name, type)
                elif cats:
                    name, type, days = cats.pop()
                    print(name, type)
            elif z == "cat":
                if cats:
                    name, type, days = cats.pop()
                    print(name, type)
                elif dogs:
                    name, type, days = dogs.pop()
                    print(name, type)
        else:
            if y == "dog":
                dogs.appendleft((x, y, z))


            elif y == "cat":
                cats.appendleft((x, y, z))



array = [("Sadie", "dog", 4), ("Woof", "cat", 7), ("Chirpy", "dog", 2), ("Lola", "dog", 1)]
a2 = [("Bob", "person", "dog"), ( "Floofy", "cat", 1), ("Sally", "person", "cat"), ("Ji", "person", "cat"), ("Ali", "person", "cat")]
h = AdoptAPet(array, a2)
print(h)
