H, M = map(int,input().split())
print("Original time", H, ":", M)
Ma = M - 45
if -60 < Ma < 0: 
    A = 60 + Ma
    B = H - 1 
    if B <= 0:
        C = 24 + B
        print("set time:", C, ":", A)
    else:
        print("set time:", B, ":", A)
elif 0 < Ma < 60:
    print("set time:", H, ":", Ma)
    if B <= 0:
        C = 24 + B
        print("set time:", C, ":", A)
    else:
        print("set time:", B, ":", A)