T = []
P = []
possWay = []
workEff = []
N = int(input())
for i in range(N):
    t,p = map(int, input().split(' '))
    T.append(t)
    P.append(p)
for each in range(len(T)):
    if T.index(T[each]) + T[each] + 1 > N:
        T[each] = 1
        P[each] = 1
for each in range(len(T)):
    workEff.append(float(P[each])/float(T[each]))
def processing(LoT, LoP, LoW, LoPW):
    a = LoT[LoW.index(max(LoW))]
    b = LoT.index(a) + a + 1
    LoPW.append(LoP[LoT.index(a)])
processing(T, P, workEff, possWay)
# python ./tests/SamsungCodingExam

T = []
P = []
N = int(input())
for i in range(N):
    t,p = map(int, input().split(' '))
    T.append(t)
    P.append(p)
for each in range(len(T)):
    if T.index(T[each]) + T[each] + 1 > N:
        T[each] = 0
        P[each] = 0
tempL = []
for each in range(N):
    if len(T) > 0:
        a = T[0]
        tempL.append(P[0])
        for each in range(a):
            try:
                T.remove(T[0])
                P.remove(P[0])
            except:
                pass
tempL.remove(tempL[:-1])
print(sum(tempL))