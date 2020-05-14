NInput = int(input())
xcoor = []
ycoor = []
for i in range(NInput):
    x, y = map(int, input().split())
    xcoor.append(x)
    ycoor.append(y)
for i in range(0, len(xcoor)):
    minIndex = i
    for j in range(i+1, len(xcoor)):
        if xcoor[j] < xcoor[minIndex]:
            xcoor[j], xcoor[minIndex] = xcoor[minIndex], xcoor[j]
            ycoor[j], ycoor[minIndex] = ycoor[minIndex], ycoor[j]
for i in range(0, len(xcoor)):
    if i+1 < len(xcoor):
        if xcoor[i] == xcoor[i+1]:
            if ycoor[i] > ycoor[i+1]:
                ycoor[i], ycoor[i+1] = ycoor[i+1], ycoor[i]
for i in range(0, len(xcoor)):
    print(xcoor[i], " ", ycoor[i])