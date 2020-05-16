def Rsolution(A):
    print(len(A))
    countList = []
    count = 0
    for each in range(len(A)):
        for i in range(len(A)):
            if A[each] == 1 and A[i] == 6:
                count += 2
            elif A[each] == 2 and A[i] == 5:
                count += 2
            elif A[each] == 3 and A[i] == 4:
                count += 2
            elif A[each] == 4 and A[i] == 3:
                count += 2
            elif A[each] == 5 and A[i] == 2:
                count += 2
            elif A[each] == 6 and A[i] == 1:
                count += 2
            elif A[each] == A[i]:
                count += 0
            else:
                count += 1
        countList.append(count)
        count = 0
    return min(countList)
m = input()
print(Rsolution(m))