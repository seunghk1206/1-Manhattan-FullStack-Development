#import sys
#sys.setrecursionlimit(10**4)
def deciToBin(n, TargetNum):
    if TargetNum >=0 :
        if TargetNum == 0:
            return 0
        if 2**(n+1) > TargetNum and TargetNum >= 2**(n):
            return 10**n + deciToBin(0, TargetNum-(2**(n)))
        else:
            return deciToBin(n+1, TargetNum)
    elif TargetNum < 0:
        return -1*deciToBin(0, -TargetNum)
print(deciToBin(0, int(eval(input('remember! Only integers are allowed!')))))
