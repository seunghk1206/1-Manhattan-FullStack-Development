def deci2Hexadeci(maxn, TargetNum):
    hexaL = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    Ans = ''
    for each in range(maxn):
        if 16**(abs(each-maxn)+1) > TargetNum >= 16**abs(each-maxn):
            Ans += str(hexaL[TargetNum//(16**abs(each-maxn))])
        else:
            Ans += '0'
    return Ans
def deciToHexadeci(n, TargetNum):
    hexaL = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    Ans = ''
    run = True
    if TargetNum != 0:
        while run:
            if 16**(n+1) > TargetNum >= 16**n:
                for each in range(n):
                    if 16**(abs(each-n)+1) > TargetNum >= 16**abs(each-n):
                        Ans += str(hexaL[TargetNum//(16**abs(each-n))])
                    else:
                        Ans += '0'
                return Ans
            n+=1
    elif TargetNum == 0:
        return 0
print(deciToHexadeci(0, 9))