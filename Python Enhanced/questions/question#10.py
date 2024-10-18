
def impQue():
    impL = []
    index = []
    ans = []
    tmp = []
    NoF = int(input())
    for each in range(NoF):
        a, c = map(int, input().split(' '))
        b = list(map(int, input().split(' ')))
        index.append(c)
        impL.append(b)
    for each in range(len(index)):
        j = impL[index[each]]
        tmp.append(j)
        impL[each].sort()
        ans.append(int(len(impL[each])-impL.index(tmp[0][0])))
        tmp = []
    for each in ans:
        print(each)

impQue()