def nDUnf(arr):
    varL = []
    for each in arr:
        if type(each) == list:
            for EV in nDUnf(each):
                varL.append(EV)
        else:
            varL.append(each)
    return varL
def combinations(iterable, r):
    pool = list(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield list(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield list(pool[i] for i in indices)
def solution(orders, course):
    answer = []
    let = []
    for each in orders:
        for eachAlpha in each:
            let.append(eachAlpha)
    let2 = list(set(let))
    comb = [list(combinations(let2, i)) for i in course]
    d = ''
    tempL = []
    reEl = []
    for i in comb:
        for each in i:
            for alpha in each:
                d += alpha
            tempL.append(d)
            d = ''
        reEl.append(tempL)
        tempL = []
    comb = nDUnf(reEl)
    comb2L = []
    cnt = 0
    mbL = []
    for each in comb:
        comb2L.append(''.join(map(str, sorted(each))))
    for each in comb2L:
        cnt = 0
        mb = []
        for eachOrd in orders:
            print(each in eachOrd)
            for eachalpha in each:
                if eachalpha in eachOrd:
                    cnt += 1
                if cnt == len(each):
                    mb.append(1)
                    break
        if sum(mb) >= 2:
            answer.append(each)
            mbL.append(sum(mb))
    return answer
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))