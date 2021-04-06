def doubleSort(A, B):
    for i in range(0, len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                A[j], A[minIndex] = A[minIndex], A[j]
                B[j], B[minIndex] = B[minIndex], B[j]
    return [A, B]

InpL = []
for _ in range(4):
    a = str(input("문장 입력 바람: "))
    InpL.append(a.split(' '))

# 2D -> 1D
tempL = [eachElement for each in InpL for eachElement in each]

CountDict = dict()

for each in set(tempL):
    CountDict[each] = tempL.count(each)/len(tempL)

KeyL = [x for x,y in CountDict.items()]
ValL = [y for x,y in CountDict.items()]

ReturnL = doubleSort(ValL, KeyL)
print(ReturnL)