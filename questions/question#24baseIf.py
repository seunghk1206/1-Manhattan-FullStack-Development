def solution(words, queries):
    answer = []
    tempL = []
    removeL = []
    for each in queries:
        if len(set(each.split('?'))) == 1:
            for eachWord in words:
                if len(each) == len(eachWord):
                    tempL.append(eachWord)
        else:
            for eachWord in words:
                if len(each) == len(eachWord):
                    if each[0] == '?':
                        p = each.split('?')[-1]
                        if p in eachWord and eachWord not in tempL:
                            if p == eachWord[len(eachWord)-len(p):]:
                                tempL.append(eachWord)
                    else:
                        p = each.split('?')[0]
                        if p in eachWord and eachWord not in tempL:
                            if 0 == eachWord.index(p):
                                tempL.append(eachWord)
        answer.append(len(tempL))
        tempL = []
        removeL = []
    return answer