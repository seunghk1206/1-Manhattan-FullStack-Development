import itertools
a = int(input())
b = []
countx = -2
county = -2
temp = []
osx = [' ', ' ', ' ']
def tyingX(L, n):
    for i in range(0, len(L), n):
        yield L[i:i + n]
def tyingY(L, n):
    for eachL in L:
        for i in range(0, len(L), n):
            yield eachL[i:i + n]
for each in range(a):
    for eachNum in range(a):
        temp.append('*')
    b.append(temp)
    temp = []
for each in range(int(a//3)):
    countx = 1
    for eachS in range(int(a//3)):
        b[county][countx] = ' '
        countx += 3
    county += 3
countx = -2
county = -2
b_f = list(tyingX(list(tyingY(b, 3)), 3))
for each in range(int(a//9)):
    for eachS in range(int(a//9)):
        b_f[county][countx] = osx
        countx += 3
    countx = -2
    county += 3
b = list(itertools.chain(b_f))
b_fin = list(tyingX(list(tyingY(b, a)), a))
print('\n'.join([''.join([str(i) for i in row]) for row in b_fin]))