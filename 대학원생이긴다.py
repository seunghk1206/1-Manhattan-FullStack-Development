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
            if -0.000001 <= each[0] <= 0.000001 and (0.000001 < each[1] or -0.000001 > each[1]):
                if each[1] < 0:
                    angL.append(-90)
                elif each[1] > 0:
                    angL.append(90)
            elif -0.000001 <= each[0] <= 0.000001 and -0.000001 <= each[1] <= 0.000001:
                pass
            else:
                if slopeInAng(each[1]/each[0]) < 0:
                    angL.append(360 + slopeInAng(each[1]/each[0]))
                else:
                    angL.append(slopeInAng(each[1]/each[0]))
        Rotation = angL[angL.index(min(angL))]
        factsL.append([scale, Rotation, dxdy[0], dxdy[1]])
    heatTreat = []
    angL = [each[1] for each in factsL]
    for each in range(len(angL)):
        if int(angL[each])-0.000001 <= angL[each] <= int(angL[each]) + 0.000001:
            if int(factsL[each][3])-0.000001 <= factsL[each][3] <= int(factsL[each][3])+0.000001 and int(factsL[each][2])-0.000001 < factsL[each][2] < int(factsL[each][2])+0.000001:
                heatTreat.append(factsL[each])
    distL = [each[2]**2+each[3]**2 for each in heatTreat]
    printL.append(heatTreat[distL.index(min(distL))])
for each in printL:
    print(each[0], each[1], each[2], each[3])

'''
3
2 0 1 -2 3 -2
8 -10 16 -6 8 -2
-4 4 -2 5 -2 3

5
-8 -9 -6.585786438 -7.5857864 -8.707106781 -6.878679656
3 3 1 7 -1 3
5 -7 9 1 13 -7
12 -2 8 6 4 -2
5 6 3 5 3 7
'''