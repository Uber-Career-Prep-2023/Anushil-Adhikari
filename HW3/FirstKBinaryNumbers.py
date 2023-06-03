def FirstKBinaryNumbers(num):
    temp = []
    for i in range(num):
        bob = bin(i)[2::]
        temp.append(bin(i)[2::])
    
    return temp

print(FirstKBinaryNumbers(10))