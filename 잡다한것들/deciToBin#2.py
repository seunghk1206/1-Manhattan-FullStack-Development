def deciToBin(n, TargetNum):
    if 1 > TargetNum > 0:
        if 2**(n) > TargetNum and TargetNum >= 2**(n-1):
            return 10**(n-1) + deciToBin(0, TargetNum-(2**(n-1)))
        else:
            return deciToBin(n-1, TargetNum)
    elif TargetNum >=0 :
        if TargetNum == 0:
            return 0
        if 2**(n+1) > TargetNum and TargetNum >= 2**(n):
            return 10**n + deciToBin(0, TargetNum-(2**(n)))
        else:
            return deciToBin(n+1, TargetNum)
    elif TargetNum < 0:
        return -1*deciToBin(0, -TargetNum)
print(deciToBin(0, float(eval(input()))))
