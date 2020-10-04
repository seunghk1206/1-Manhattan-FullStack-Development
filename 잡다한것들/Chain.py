def iterChain(List):
    L = []
    for each in range(len(List)):
        if str(type(List[each])) == "<class 'list'>":
            return iterChain(List[each])
        else:
            L.append(List[each])
    return L
print(iterChain([[[1,2,3,4,5,6,7,8,9,3,1,23,3,1,21,3,1,23,1,32,122,23,1,321,23]]]))