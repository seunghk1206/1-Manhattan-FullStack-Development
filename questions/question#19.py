def solution(user_id, banned_id):
    answer = 1
    tempL = []
    removeL = []
    doneL = []
    done2L = []
    dictionary = {}
    for each in banned_id:
        if len(set(each.split('*'))) == 1:
            for eachWord in user_id:
                if len(each) == len(eachWord):
                    tempL.append(eachWord)
        else:
            for eachWord in user_id:
                if len(each) == len(eachWord):
                    for eachInd in range(len(each)):
                        if each[eachInd] == '*' and eachWord not in tempL and eachWord not in removeL:
                            tempL.append(eachWord)
                        elif each[eachInd] == eachWord[eachInd] and eachWord not in tempL and eachWord not in removeL:
                            tempL.append(eachWord)
                        elif each[eachInd] != eachWord[eachInd] and eachWord in tempL and eachWord not in removeL and each[eachInd] != '*':
                            tempL.remove(eachWord)
                            removeL.append(eachWord)
                        elif each[eachInd] != eachWord[eachInd] and eachWord not in tempL and eachWord not in removeL and each[eachInd] != '*':
                            removeL.append(eachWord)
        dictionary[each] = [len(tempL), tempL]
        doneL.append(tempL)
        tempL = []
        removeL = []
    for key, item in dictionary.items():
        answer *= (item[0]/banned_id.count(key))
        done2L.append(item[1])
    doneL = []
    print(done2L)
    for each in done2L:
        for eachWord in each:
            doneL.append(eachWord)
    answer -= abs(len(set(doneL)) - len(doneL))
    return answer