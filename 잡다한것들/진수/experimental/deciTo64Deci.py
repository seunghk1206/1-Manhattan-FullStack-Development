import string
import itertools
def deciTo64deci(n, TargetNum):
    try:
        TargetNum = eval(TargetNum)
    except:
        pass
    a = [str(each) for each in range(10)]
    for each in itertools.chain([string.ascii_lowercase, string.ascii_uppercase]):
        for eachLetter in each:
            a.append(eachLetter)
    a.append('#')
    a.append('@')
    ans = ''
    hexaL = a
    if TargetNum >= 1:
        intP = str(TargetNum).split('.')[0]
        if 64**(n+1) > int(intP) >= 64**n:
            for each in range(n+1):
                ans += hexaL[int(intP)//(64**abs(each-n))]
                intP = str((int(intP)%(64**abs(each-n))))
            try:
                decP = str(TargetNum).split('.')[1]
                decP = '0.' + decP
                return ans + '.' + deciTo64deci(-1, float(decP))
            except:
                return ans
        else:
            return deciTo64deci(n+1, TargetNum)
    elif TargetNum < 0:
        return '-' + deciTo64deci(0, -TargetNum)
    elif TargetNum == 0 or TargetNum == '0':
        return '0'

    elif 1 > TargetNum > 0:
        if 64**(n+1) > TargetNum >= 64**n:
            if TargetNum%(64**n) == 0:
                return hexaL[int(TargetNum//(64**n))]
            return hexaL[int(TargetNum//(64**n))] + deciTo64deci(n-1, TargetNum%(64**n))
        else:
            return '0' + deciTo64deci(n-1, TargetNum)
print(deciTo64deci(0, 256.015625))