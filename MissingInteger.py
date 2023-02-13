#Q6
#5 minutes

#why do we need the num input
def MissingInteger(lst, num):
    #since the arrays always come in a sort array
    #we can check if lst[i+1] is not in the list we can return the number
    for i in lst:
        if (i+1) not in lst:
            return i+1
    return []



#print(MissingInteger([1, 2, 3, 4, 6, 7],7))
#print(MissingInteger([1],2))
#print(MissingInteger([1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12],12))

