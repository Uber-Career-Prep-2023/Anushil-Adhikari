#9 10 min
def DedupArray(lst):
    temp = []
    for i in lst:
        if i not in temp:
            temp.append(i)
    del(lst)
    return temp

print(DedupArray([0, 0, 1, 4, 5, 5, 5, 8, 9, 9, 10, 11, 15, 15]))