def solution(genres, plays):
    answer = []
    Dict = {}
    Dict2 = {}
    SetG = list(set(genres))
    maxGen = ['none' for _ in SetG]
    for each in SetG:
        Dict[each] = 0
        Dict2[each] = [[], []]
    for i in range(len(genres)):
        Dict[genres[i]] += plays[i]
        Dict2[genres[i]][0].append(plays[i])
        Dict2[genres[i]][1].append(i)
    valL = sorted(Dict.values(), reverse = True)
    for k, v in Dict.items():
        i = valL.index(v)
        maxGen[i]=k
    for each in maxGen:
        tempL = Dict2[each]
        if len(tempL[1]) >= 2:
            SortGenVal = sorted(tempL[0], reverse = True)
            if SortGenVal[0] == SortGenVal[1]:
                practNum = SortGenVal.count(max(SortGenVal))
                if practNum == 2:
                    ind = tempL[0].index(SortGenVal[0])
                    saving = tempL
                    tempL[0].remove(SortGenVal[0])
                    tempL[1].remove(tempL[1][ind])
                    ind2 = tempL[0].index(SortGenVal[1])
                    if saving[1][ind] < saving[1][ind2]:
                        answer.append(saving[1][ind])
                        answer.append(saving[1][ind2])
                    elif saving[1][ind] > saving[1][ind2]:
                        answer.append(saving[1][ind2])
                        answer.append(saving[1][ind])
                else:
                    indexL = []
                    for e in SortGenVal[0:practNum-1]:
                        ind = tempL[0].index(e)
                        tempL[0].remove(e)
                        indexL.append(tempL[1][ind])
                        tempL[1].remove(tempL[1][ind])
                    sortL = sorted(indexL)
                    answer.append(sortL[0])
                    answer.append(sortL[1])
            else:
                ind = tempL[0].index(SortGenVal[0])
                answer.append(tempL[1][ind])
                ind2 = tempL[0].index(SortGenVal[1])
                answer.append(tempL[1][ind2])
        else:
            answer.append(tempL[1][0])
    return answer

print(solution(["classic", "pop", "classic", "pop", "classic", "classic"], [400, 600, 150, 600, 500, 500]))