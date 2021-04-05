StrL = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
numL = [each for each in range(len(StrL[0]))]

L = ['Hello', 'World', 'str', 'is', 'awesome']

def doubleSort(A, B):
    for i in range(0, len(A)):
        minIndex = i
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                A[j], A[minIndex] = A[minIndex], A[j]
                B[j], B[minIndex] = B[minIndex], B[j]
    return [A, B]

def findingMech(L):
    StrL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    numL = []
    for each in L:
        a = 0
        for eachStr in each:
            a += StrL.index(eachStr)
        numL.append(a)
    return numL

print(doubleSort(findingMech(L), L))