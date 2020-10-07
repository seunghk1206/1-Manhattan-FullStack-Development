def deciToHexa(n, TargetNum):
    try:
        TargetNum = eval(TargetNum)
    except:
        pass
    ans = ''
    hexaL = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    if TargetNum >= 1:
        intP = str(TargetNum).split('.')[0]
        if 16**(n+1) > int(intP) >= 16**n:
            for each in range(n+1):
                ans += hexaL[int(intP)//(16**abs(each-n))]
                intP = str((int(intP)%(16**abs(each-n))))
            try:
                decP = str(TargetNum).split('.')[1]
                decP = '0.' + decP
                return ans + '.' + deciToHexa(-1, float(decP))
            except:
                return ans
        else:
            return deciToHexa(n+1, TargetNum)
    elif TargetNum < 0:
        return '-' + deciToHexa(0, -TargetNum)
    elif TargetNum == 0 or TargetNum == '0':
        return '0'

    elif 1 > TargetNum > 0:
        if 16**(n+1) > TargetNum >= 16**n:
            if TargetNum%(16**n) == 0:
                return hexaL[int(TargetNum//(16**n))]
            return hexaL[int(TargetNum//(16**n))] + deciToHexa(n-1, TargetNum%(16**n))
        else:
            return '0' + deciToHexa(n-1, TargetNum)
print(deciToHexa(0, 1323+14/16))