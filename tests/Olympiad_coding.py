NPep = int(input())
NLKgH = []
LKgH = []
rank = []
for each in range(NPep):
    KgH = list(input("The format should be: mass, height ").split(" "))
    LKgH.append(KgH[0])
    LKgH.append(KgH[1])
    NLKgH.append(LKgH)
    LKgH = []

for each in range(1, len(LKgH)):
    rank.append(each)
for each in range(1, len(rank)-1):
    if NLKgH[each][0] > NLKgH[each-1][0] and NLKgH[each][1] < NLKgH[each-1][1]:
        rank[each] = rank[each-1]
    elif NLKgH[each][0] < NLKgH[each-1][0] and NLKgH[each][1] > NLKgH[each-1][1]:
        rank[each] = rank[each-1]
    elif NLKgH[each][0] > NLKgH[each-1][0] and NLKgH[each][1] > NLKgH[each-1][1]:
        pass
for i in rank:
    print(i)