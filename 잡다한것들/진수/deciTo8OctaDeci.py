def deciToOct(n, TargetNum):
    if 1 > TargetNum > 0:
        if 8**(n) > TargetNum and TargetNum >= 8**(n-1):
            return 10**(n-1) + deciToOct(0, TargetNum-(8**(n-1)))
        else:
            return deciToOct(n-1, TargetNum)
    elif TargetNum >= 0:
        if TargetNum == 0:
            return 0
        if 8**(n+1) > TargetNum and TargetNum >= 8**(n):
            return 10**n + deciToOct(0, TargetNum-(8**(n)))
        else:
            return deciToOct(n+1, TargetNum)
    elif TargetNum < 0:
        return -1*deciToOct(0, -TargetNum)
print(deciToOct(0, float(eval(input()))))