def factorial(n):
    if n == 0:
        return 1
    else:
        ret = 1
        for each in range(1, n+1):
            ret *= each
        return ret
print(factorial(4))