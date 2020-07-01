def solution(skill, skill_trees):
    LoW = []
    answer = 0
    missedCases = 0
    for each in skill_trees:
        for eachInd in range(len(each)):
            for eachVar in skill:
                if each[eachInd] == eachVar:
                    LoW.append(each[eachInd])
        for ind, i in enumerate(skill):
            if ind < len(LoW):
                if LoW[ind] == i:
                    pass
                else: 
                    missedCases -= 1
                    break
            else:
                break
        LoW = []
    answer += len(skill_trees)
    answer += missedCases
    return answer
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))