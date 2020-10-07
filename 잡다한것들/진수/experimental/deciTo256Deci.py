import string
import itertools
def deciTo256deci(n, TargetNum):
    try:
        TargetNum = eval(TargetNum)
    except:
        pass
    a = []
    for each in range(256):
        a.append('(' + str(each) + ')')
    ans = ''
    hexaL = a
    if TargetNum >= 1:
        intP = str(TargetNum).split('.')[0]
        if 256**(n+1) > int(intP) >= 256**n:
            for each in range(n+1):
                ans += hexaL[int(intP)//(256**abs(each-n))]
                intP = str((int(intP)%(256**abs(each-n))))
            try:
                decP = str(TargetNum).split('.')[1]
                decP = '0.' + decP
                return ans + '.' + deciTo256deci(-1, float(decP))
            except:
                return ans
        else:
            return deciTo256deci(n+1, TargetNum)
    elif TargetNum < 0:
        return '-' + deciTo256deci(0, -TargetNum)
    elif TargetNum == 0 or TargetNum == '0':
        return '0'

    elif 1 > TargetNum > 0:
        if 256**(n+1) > TargetNum >= 256**n:
            if TargetNum%(256**n) == 0:
                return hexaL[int(TargetNum//(256**n))]
            return hexaL[int(TargetNum//(256**n))] + deciTo256deci(n-1, TargetNum%(256**n))
        else:
            return '0' + deciTo256deci(n-1, TargetNum)
no = 256**2+128/256
print(str(no) + ' in 256 deci, ' + deciTo256deci(0, no))