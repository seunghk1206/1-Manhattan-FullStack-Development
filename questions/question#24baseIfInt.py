def solution(words, queries):
    answer = []
    count = 0
    for each in queries:
        if len(set(each.split('?'))) == 1:
            for eachWord in words:
                if len(each) == len(eachWord):
                    count += 1
        else:
            for eachWord in words:
                if len(each) == len(eachWord):
                    if each[0] == '?':
                        p = each.split('?')[-1]
                        if p in eachWord:
                            if p == eachWord[len(eachWord)-len(p):]:
                                count += 1
                    else:
                        p = each.split('?')[0]
                        if p in eachWord:
                            if 0 == eachWord.index(p):
                                count += 1
        answer.append(count)
        count = 0
    return answer