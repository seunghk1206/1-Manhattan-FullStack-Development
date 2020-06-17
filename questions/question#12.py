import math
coorL = []
distL = []
inp = int(input())
for each in range(inp):
    d = list(map(int, input().split(' ')))
    coorL.append(d)
for each in coorL:
    for eachC in coorL:
        xdiff = each[0]-eachC[0]
        ydiff = each[1]-eachC[1]
        pyth = (xdiff * xdiff) + (ydiff * ydiff)
        if xdiff == 0 and ydiff == 0:
            pass
        else:
            distL.append(abs(pyth))

print(min(distL))