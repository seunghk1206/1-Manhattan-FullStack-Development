StrL = ['ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
numL = [each for each in range(len(StrL[0]))]

L = ['Hello', 'World', 'str', 'is', 'awesome']
def findingMech(L):
    StrL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    numL = []
    for each in L:
        a = 0
        for eachStr in each:
            a += StrL.index(eachStr)
        numL.append(a)
    return numL

print(findingMech(L))