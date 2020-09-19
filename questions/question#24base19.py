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
                    for eachInd in range(len(each)):
                        if each[eachInd] == '?' and eachWord not in tempL and eachWord not in removeL:
                            tempL.append(eachWord)
                        elif each[eachInd] == eachWord[eachInd] and eachWord not in tempL and eachWord not in removeL:
                            tempL.append(eachWord)
                        elif each[eachInd] != eachWord[eachInd] and eachWord in tempL and eachWord not in removeL and each[eachInd] != '?':
                            tempL.remove(eachWord)
                            removeL.append(eachWord)
                        elif each[eachInd] != eachWord[eachInd] and eachWord not in tempL and eachWord not in removeL and each[eachInd] != '?':
                            removeL.append(eachWord)
        answer.append(len(tempL))
        tempL = []
        removeL = []
    return answer