def solution2(n,m):
    if n>m:
        loB = []
        A = n%m
        B = m
        while A != 0:
            loB.append(B)
            A = B%A
            B = loB[-1]
        GCD = loB[-1]
    if m>n:
        loB = []
        A = m%n
        B = n
        while A != 0:
            loB.append(B)
            A = B%A
            B = loB[-1]
        GCD = loB[-1]
    LCM = n*m/GCD
    return [GCD, LCM]