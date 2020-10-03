def deciToQuad(n, TargetNum):
    if 1 > TargetNum > 0:
        if 4**(n) > TargetNum and TargetNum >= 4**(n-1):
            return 10**(n-1) + deciToQuad(0, TargetNum-(4**(n-1)))
        else:
            return deciToQuad(n-1, TargetNum)
    elif TargetNum >= 0:
        if TargetNum == 0:
            return 0
        if 4**(n+1) > TargetNum and TargetNum >= 4**(n):
            return 10**n + deciToQuad(0, TargetNum-(4**(n)))
        else:
            return deciToQuad(n+1, TargetNum)
    elif TargetNum < 0:
        return -1*deciToQuad(0, -TargetNum)
print(deciToQuad(0, float(eval(input()))))