def fac(n):
    if n == 0:
        return 0
    elif 1 <= n <= 2: 
        return 1
    else: 
        return fac(n-2) + fac(n-1)
a = int(input())
print(fac(a))
# 0 1 1 2 3 5 8 13