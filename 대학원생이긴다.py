import math
printL = []
def slopeInAng(slope):
    return math.atan(slope) * 180/math.pi
inp = int(input())
for _ in range(inp):
    L = list(map(float, input().split()))
    coorL = [[L[2*each], L[2*each+1]]for each in range(len(L)//2)]
    candidates = []
    dist = []
    for each in range(3):
        dist.append((coorL[each-1][0]-coorL[each][0])**2+(coorL[each-1][1]-coorL[each][1])**2)
    scale = math.sqrt(min(dist))/2
    candidates.append(coorL[dist.index(min(dist))])
    candidates.append(coorL[dist.index(min(dist))-1])
    factsL = []
    for it in candidates:
        dxdy = it
        coorB = []
        angL = []
        for each in coorL:
            coorB.append([each[0]-dxdy[0], each[1]-dxdy[1]])
        for each in coorB:
            if each[0] == 0 and each[1] != 0:
                if each[1] < 0:
                    angL.append(-90)
                elif each[1] > 0:
                    angL.append(90)
            elif each[0] == 0 and each[1] == 0:
                pass
            else:
                if slopeInAng(each[1]/each[0]) < 0:
                    angL.append(360 + slopeInAng(each[1]/each[0]))
                else:
                    angL.append(slopeInAng(each[1]/each[0]))
        absAng = [abs(each) for each in angL]
        Rotation = angL[absAng.index(min(absAng))]
        if Rotation < 0:
            Rotation = 360 + Rotation
        factsL.append([scale, Rotation, dxdy[0], dxdy[1]])
    heatTreat = []
    angL = [each[1] for each in factsL]
    for each in range(len(angL)):
        if int(angL[each]) == angL[each]:
            heatTreat.append(factsL[each])
    if angL[0] == angL[1]:
        distL = [each[2]**2+each[3]**2 for each in heatTreat]
        printL.append(heatTreat[distL.index(min(distL))])
    else:
        printL.append(heatTreat[0])
for each in printL:
    print(each[0], each[1], each[2], each[3])