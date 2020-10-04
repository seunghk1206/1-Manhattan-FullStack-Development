import sys
sys.setrecursionlimit(10**6)
L=[]
temL = []
def iterChain(L, List, tempL):
    for each in range(len(List)):
        if str(type(List[each])) == "<class 'list'>":
            tempL.append(List[each])
        else:
            L.append(List[each])
    if len(tempL) != 0:
        List = []
        return iterChain(L, tempL, List)
    return L
print(iterChain(L, [1,[2,[1,2,3,4,5,6,7,8,9,3,1,23,3,1,21,3,1,23,1,32,122,23,1,321,23]]], temL))