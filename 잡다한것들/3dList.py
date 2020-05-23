a = int(input("which 3d list? "))
b = [[[0, 1, 1], [0, 2, 1], [1, 4, 3]], [[0, 1, 3], [0, 0, 0], [3, 4, 2]], [[2, 3, 4], [1, 3, 2], [4, 3, 0]]]
dummy = []
for each in range(len(b)):
    for eachNum in range(len(b)):
        checkingList = b[a-1][int(each)][int(eachNum)]
        dummy.append(checkingList)
print("the numbers in that axis is:")
for each in range(len(b[0])*len(b[0])):
    print(dummy[each])
dummy = []