def binarityGS(n):
    if n == 1:
        return 2
    if n > 0:
        return 2**n + binarityGS(n-1)