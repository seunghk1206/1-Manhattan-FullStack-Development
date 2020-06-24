import itertools
size = int(input())
def createS(inp):
    b = []
    temp = []
    for each in range(inp):
        for eachNum in range(inp):
            temp.append('*')
        b.append(temp)
        temp = []
    return b
def Blanking(L, inp):
    def tyingX(L, n):
        for i in range(0, len(L), n):
            yield L[i:i + n]
    def tyingY(L, n):
        for eachL in L:
            for i in range(0, len(L), n):
                yield eachL[i:i + n]
    countx = -2
    county = -2
    cnt = 0
    mlx = inp
    for each in range(8):
        mlx /= 3
        if mlx > 1:
            cnt += 1
        else:
            break
    BL = []
    for each in range(1, cnt):
        dividedAll = list(tyingX(list(tyingY(L, 3**each)), 3**each))
        flattened = itertools.chain(dividedAll[0][0])
        for each in flattened:
            BL.append(' ')
        for each in range(int(3)):
            countx = 1
            for eachS in range(int(3)):
                dividedAll[county][countx] = BL
                countx += 3
            county += 3
        county = 1
    SemiList = itertools.chain(dividedAll)
    SemiFinal = list(tyingY(list(tyingX(SemiList, inp)), inp))
    return SemiFinal
square = createS(size)
FinalList = Blanking(square, size)
print('\n'.join([''.join([str(i) for i in row]) for row in FinalList]))
#print('\n'.join([''.join([str(i) for i in row]) for row in FinalList]))
#Y then X